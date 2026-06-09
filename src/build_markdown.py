def format_user(user_obj):
    if not isinstance(user_obj, dict):
        # Fallback for old data
        return f"[@{user_obj}](https://github.com/{user_obj})"
    
    username = user_obj.get("username")
    uuid = user_obj.get("uuid")
    if uuid:
        return f"[@{username}](https://sorukumar.github.io/orange-dev-network/profile.html?uuid={uuid})"
    return f"[@{username}](https://github.com/{username})"

def build_markdown_from_json(data):
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    stats = data.get("stats", {})
    tldr = data.get("tldr", [])
    categories = data.get("categories", {})
    discussions = data.get("discussions", [])
    shoutouts = data.get("shoutouts", {})

    doc = [
        f"# This Week in Bitcoin ({start_date} to {end_date})",
        "",
        f"> 📈 **This Week's Pulse:** **{stats.get('total_merged', 0)}** PRs Merged | **{stats.get('total_reviews', 0)}** Review Events | **{stats.get('new_contributors', 0)}** First-time Contributors | **{stats.get('total_threads', 0)}** Active Discussions",
        "",
        "## The TL;DR"
    ]
    
    for line in tldr:
        doc.append(line)
        
    doc.extend([
        "",
        "## Core Code: Merged This Week"
    ])

    for cat in categories.get("merged", []):
        doc.append(f"### {cat['name']}")
        for pr in cat.get("prs", []):
            summary = pr.get("summary", "")
            doc.append(f"*   [#{pr['number']}](https://github.com/bitcoin/bitcoin/pull/{pr['number']}) **{pr['title']}** (by {format_user(pr['author'])})")
            if summary:
                doc.append(f"    * {summary}")
        doc.append("")

    doc.append("## Core Code: Under Review (Hot PRs)")
    for cat in categories.get("hot", []):
        doc.append(f"### {cat['name']}")
        for pr in cat.get("prs", []):
            doc.append(f"*   [#{pr['number']}](https://github.com/bitcoin/bitcoin/pull/{pr['number']}) **{pr['title']}** ({pr.get('event_count', 0)} review events)")
        doc.append("")

    doc.append("## Research & Governance")
    for thread in discussions:
        doc.append(f"*   **[{thread['source']}]** [{thread['subject']}]({thread['link']}) ({thread['message_count']} messages)")
        if thread.get('summary'):
            doc.append(f"    * {thread['summary']}")
    doc.append("")

    doc.append("## Contributor Shoutouts")
    doc.append("A huge thanks to everyone who contributed code or reviewed PRs this week!")
    
    new_contributors = shoutouts.get("new_contributors", [])
    if new_contributors:
        doc.append("\n🎉 **Welcome First-Time Contributors!**")
        doc.append("* " + ", ".join([format_user(u) for u in new_contributors]))

    top_authors = shoutouts.get("top_authors", [])
    if top_authors:
        doc.append("\n🥇 **Top Authors (Merged PRs)**")
        doc.append("* " + ", ".join([f"{format_user(u['user'])} ({u['count']})" for u in top_authors]))
        
    top_reviewers = shoutouts.get("top_reviewers", [])
    if top_reviewers:
        doc.append("\n🏆 **Top Reviewers**")
        doc.append("* " + ", ".join([f"{format_user(u['user'])} ({u['count']})" for u in top_reviewers]))

    all_active = shoutouts.get("all_active", [])
    doc.append("\n**All Active Contributors:**")
    if all_active:
        chunked = [all_active[i:i+5] for i in range(0, len(all_active), 5)]
        for chunk in chunked:
            doc.append("* " + ", ".join([format_user(u) for u in chunk]))
    else:
        doc.append("* No active contributors tracked this week.")

    return "\n".join(doc)
