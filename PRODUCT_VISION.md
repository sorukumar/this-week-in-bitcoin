# This Week in Bitcoin (TWIB) — Product Vision & Strategic Roadmap

> **Mission:** Transform raw Bitcoin development noise (PRs, IRC logs, mailing lists, Discourse threads) into high-velocity, executive-grade intelligence for developers, researchers, and ecosystem leaders.

---

## 🎯 Core Value Pillars

### 1. The Executive Briefing (Weekly Digest)
- **Primary Audience:** Founders, investors, lead engineers, ecosystem executives.
- **Core Value:** 60-second clarity on merged PRs, active consensus debates, and community shoutouts.
- **Vibe:** Clean, authoritative, newspaper/journalistic elegance.

### 2. The Decision Record (Weekly Core Meeting Archive)
- **Primary Audience:** Core developers, protocol researchers, node operators, grant evaluators.
- **Core Value:** Searchable, permanent record of tactical decisions, PR blockers, and consensus discussions in `#bitcoin-core-dev`.
- **Vibe:** Institutional-grade protocol ledger.

---

## 🚀 Backend & Intelligence Roadmap (Upcoming Focus)

### Item 1: Enhanced AI Summarization Schema (`orange-dev-data`)
- **Headline Verdict Extraction:** Update `generate_meeting_summary.py` Gemini JSON prompt to output a 10–15 word high-signal executive verdict (`headline_verdict`) for every IRC meeting.
- **Categorized Key Decisions:** Distinguish between consensus decisions, soft consensus/debates, and explicit blocker flags.
- **Historical Re-Index:** Force-rebuild historical meeting summaries across 200+ indexed meetings.

### Item 2: Cross-Meeting Topic Lineage Engine
- **Concept:** Track major initiatives (e.g. *QML GUI*, *Kernel Split*, *Cluster Mempool*, *Package Relay*) across multiple meetings over 6–12 months.
- **Data Strategy:** Build an automated script in `orange-dev-data` to cluster meetings by topic keywords/PR IDs and generate a unified `topic_lineage.json`.
- **UX Goal:** Allow users to click any topic badge (e.g. `[Cluster Mempool]`) to view a chronological evolution of discussions and decisions.

### Item 3: Developer Action Attribution
- **Concept:** Automatically attribute action items and decisions to developer handles (`@handle`).
- **Integration:** Link directly with **Orange Dev Network** (`network.bitcoindatalabs.org`) to map meeting contributions to developer profiles and influence scores.

### Item 4: Automated Social & Newsletter Syndication
- **X / Twitter Thread Generator:** Auto-format weekly TWIB digests into engaging X threads with permalinks.
- **Markdown / Substack Exporter:** Provide single-click export formats for newsletter distributors.

---

## 🎨 Visual & Experience Guidelines
- **Color Palette:** Warm cream parchment (`#FAF8F5`), Terracotta accent (`#E8916B`), Charcoal text (`#1A1D24`).
- **Typography:** Newsreader (Serif) for headings & editorial drop-caps; Inter (Sans) for UI controls & metadata.
- **Ergonomics:** Fast keyboard shortcuts (`/`, `j`, `k`, `Esc`), 1-click Markdown copying, zero fluff.
