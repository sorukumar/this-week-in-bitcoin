import os
from dotenv import load_dotenv
from src.fetch_data import get_weekly_activity
from src.generate_report import generate_newsletter_data
import json

def main():
    # Load environment variables from .env
    load_dotenv()
    
    print("Fetching weekly activity...")
    weekly_data = get_weekly_activity(days_back=7)
    
    merged_count = sum(len(prs) for prs in weekly_data.get('categorized_merged_prs', {}).values())
    print(f"Fetched {merged_count} PRs and {len(weekly_data['active_threads'])} discussions.")
    print("Generating newsletter data with Gemini...")
    
    newsletter_data = generate_newsletter_data(weekly_data)
    
    # Ensure archive directory exists
    os.makedirs("archive", exist_ok=True)
    
    # Save the report as JSON for the web
    # We use today_str (which is now Sunday's date) to brand all files
    today_str = (pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
    os.makedirs("docs/data", exist_ok=True)
    json_filename = f"docs/data/newsletter_{today_str}.json"
    latest_json = "docs/data/latest.json"
    archive_index_file = "docs/data/archive_index.json"
    
    with open(json_filename, "w") as f:
        json.dump(newsletter_data, f, indent=2)
        
    with open(latest_json, "w") as f:
        json.dump(newsletter_data, f, indent=2)
        
    # Maintain archive index
    archive_index = []
    if os.path.exists(archive_index_file):
        with open(archive_index_file, "r") as f:
            try:
                archive_index = json.load(f)
            except json.JSONDecodeError:
                pass
                
    # Add if not exists
    entry = {"date": today_str, "file": f"newsletter_{today_str}.json"}
    if entry not in archive_index:
        archive_index.insert(0, entry) # Insert at beginning so newest is first
        
    # Sort descending just in case
    archive_index = sorted(archive_index, key=lambda x: x["date"], reverse=True)
    
    with open(archive_index_file, "w") as f:
        json.dump(archive_index, f, indent=2)
        
    print(f"Newsletter JSON generated successfully: {json_filename} and {latest_json}")
    
    # Generate the Markdown file from the JSON
    from src.build_markdown import build_markdown_from_json
    md_filename = f"archive/newsletter_{today_str}.md"
    markdown_report = build_markdown_from_json(newsletter_data)
    with open(md_filename, "w") as f:
        f.write(markdown_report)
    print(f"Newsletter Markdown generated successfully: {md_filename}")

if __name__ == "__main__":
    main()
