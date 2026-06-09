import os
import json
from google import genai
from google.genai import types # type: ignore
import time

def get_llm_summary(client, text, instruction):
    """Helper to get a short summary from the LLM"""
    prompt = f"You are a Bitcoin Core developer. {instruction}\n\nContext:\n{text}\n\nOutput only the summary, no markdown headers or extra fluff."
    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text.strip()
        except Exception as e:
            if attempt == 2:
                return f"*(Failed to summarize after retries: {e})*"
            print(f"Rate limit or high demand hit (get_llm_summary). Retrying in {2 ** attempt * 5} seconds... ({e})")
            time.sleep(2 ** attempt * 5)

def get_bulk_llm_summaries(client, items_dict, instruction):
    """
    Takes a dictionary {id: text_to_summarize}
    Returns a dictionary {id: summary} by making ONE API call.
    """
    if not items_dict:
        return {}
        
    prompt = f"""You are a Bitcoin Core developer writing a newsletter.
{instruction}

You MUST return a valid JSON object where the keys are exactly the keys provided, and the values are the summaries. Do NOT wrap in markdown blocks, just raw JSON.

Input Data:
{json.dumps(items_dict, indent=2)}
"""
    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except Exception as e:
            if attempt == 2:
                print(f"Failed bulk summarize after retries: {e}")
                return {}
            print(f"Rate limit or high demand hit (get_bulk_llm_summaries). Retrying in {2 ** attempt * 5} seconds... ({e})")
            time.sleep(2 ** attempt * 5)

def categorize_misc_prs(client, prs, valid_categories):
    """Uses the LLM to categorize PRs that fell into 'Misc / Other'."""
    if not prs:
        return {}
    
    prompt = f"""You are a Bitcoin Core developer. Categorize each of these Pull Requests into one of the following exact categories. 
If it doesn't clearly fit, keep it as '🔄 Misc / Other'.

Valid categories:
{json.dumps(valid_categories, indent=2)}

You MUST return a valid JSON object where the keys are the PR numbers (as strings) and the values are the chosen category strings.

PRs to categorize:
{json.dumps([{ 'pr_number': str(pr['pr_number']), 'title': pr['title'] } for pr in prs], indent=2)}
"""
    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except Exception as e:
            if attempt == 2:
                print(f"Failed to categorize after retries: {e}")
                return {}
            print(f"Rate limit or high demand hit (categorize_misc_prs). Retrying in {2 ** attempt * 5} seconds... ({e})")
            time.sleep(2 ** attempt * 5)

def format_user(username):
    return f"[@{username}](https://github.com/{username})"

def generate_newsletter_data(weekly_data):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set. Please set it in .env file."

    client = genai.Client(api_key=api_key)

    start_date = weekly_data['start_date']
    end_date = weekly_data['end_date']
    categorized_merged = weekly_data.get('categorized_merged_prs', {})
    categorized_hot = weekly_data.get('categorized_hot_prs', {})
    active_threads = weekly_data.get('active_threads', [])
    contributors = weekly_data.get('contributors', [])
    
    total_merged = weekly_data.get('total_merged', 0)
    total_reviews = weekly_data.get('total_reviews', 0)
    total_threads = weekly_data.get('total_threads', 0)
    top_reviewers = weekly_data.get('top_reviewers', [])
    top_authors = weekly_data.get('top_authors', [])
    new_contributors = weekly_data.get('new_contributors', [])

    # Smart Categorization for Misc PRs
    valid_categories = [
        '👛 Wallet & Keys', '⚡ P2P & Network', '🛡️ Consensus & Cryptography', 
        '📡 RPC, APIs & ZMQ', '🖥️ GUI', '🛠️ Build, CI & Testing', '📝 Documentation', '🔄 Misc / Other'
    ]
    misc_prs = categorized_merged.pop('🔄 Misc / Other', [])
    if misc_prs:
        new_cats = categorize_misc_prs(client, misc_prs, valid_categories)
        for pr in misc_prs:
            pr_num_str = str(pr['pr_number'])
            cat = new_cats.get(pr_num_str, '🔄 Misc / Other')
            if cat not in categorized_merged:
                categorized_merged[cat] = []
            categorized_merged[cat].append(pr)

    # Gather TL;DR input
    tldr_input = ""
    for cat, prs in categorized_merged.items():
        for pr in prs:
            tldr_input += f"- Merged PR #{pr['pr_number']}: {pr['title']}\n"
    
    for thread in active_threads:
        tldr_input += f"- Discussed: {thread['subject']}\n"

    # Get TLDR
    tldr_summary = get_llm_summary(client, tldr_input, "Write 2 bullet points summarizing the most important technical shift or discussion from these events.")

    # Get bulk summaries for PRs (Focus on impact)
    pr_items_to_summarize = {}
    for cat, prs in categorized_merged.items():
        for pr in prs:
            pr_items_to_summarize[f"pr_{pr['pr_number']}"] = pr['title']

    pr_summaries = get_bulk_llm_summaries(
        client, 
        pr_items_to_summarize, 
        "For each PR, write exactly 1 short sentence explaining its impact or why it matters to Bitcoin node operators, developers, the broader community, or the overall health of the Bitcoin network."
    )

    # Get bulk summaries for Top 2 Social Threads (Focus on debate)
    top_2_threads = active_threads[:2]
    thread_items = {f"thread_{t['subject'][:20]}": t['subject'] for t in top_2_threads}
    thread_summaries = get_bulk_llm_summaries(
        client,
        thread_items,
        "For each discussion thread, write 1-2 sentences summarizing the core debate, arguments, or proposed solution."
    )
    
    summaries = {**pr_summaries, **thread_summaries}

    # Clean markdown list syntax from TLDR before saving
    tldr_cleaned = []
    if tldr_summary:
        for line in tldr_summary.split('\n'):
            # Remove leading bullets like '* ', '- ', etc.
            cleaned_line = line.lstrip('*- \t')
            if cleaned_line:
                tldr_cleaned.append(cleaned_line)

    # Build the JSON data structure
    newsletter_data = {
        "start_date": start_date,
        "end_date": end_date,
        "stats": {
            "total_merged": total_merged,
            "total_reviews": total_reviews,
            "total_threads": total_threads,
            "new_contributors": len(new_contributors)
        },
        "tldr": tldr_cleaned,
        "categories": {
            "merged": [],
            "hot": []
        },
        "discussions": [],
        "shoutouts": {
            "new_contributors": new_contributors,
            "top_authors": top_authors,
            "top_reviewers": top_reviewers,
            "all_active": contributors
        }
    }

    # Code Categories (Merged)
    for category, prs in categorized_merged.items():
        cat_data = {"name": category, "prs": []}
        for pr in prs:
            summary = summaries.get(f"pr_{pr['pr_number']}", "")
            cat_data["prs"].append({
                "number": pr['pr_number'],
                "title": pr['title'],
                "author": pr['author_obj'],
                "summary": summary
            })
        newsletter_data["categories"]["merged"].append(cat_data)

    # Code Categories (Hot PRs)
    for category, prs in categorized_hot.items():
        cat_data = {"name": category, "prs": []}
        for pr in prs:
            cat_data["prs"].append({
                "number": pr['pr_number'],
                "title": pr['title'],
                "event_count": pr['event_count']
            })
        newsletter_data["categories"]["hot"].append(cat_data)

    # Research & Governance
    for thread in top_2_threads:
        summary = summaries.get(f"thread_{thread['subject'][:20]}", "")
        newsletter_data["discussions"].append({
            "source": thread['source'].title().replace('_', ' '),
            "subject": thread['subject'],
            "link": thread['link'],
            "message_count": thread['message_count'],
            "summary": summary
        })

    return newsletter_data
