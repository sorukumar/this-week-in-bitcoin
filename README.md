# This Week in Bitcoin (TWIB)

> A curated, weekly executive summary of the Bitcoin development ecosystem.

**This Week in Bitcoin (TWIB)** is an automated weekly newsletter designed to track the pulse of Bitcoin development. By aggregating and summarizing data from Bitcoin Core pull requests, mailing lists, and discussions, TWIB provides a sleek, high-level executive summary for developers, researchers, and enthusiasts looking to stay up to date with the ecosystem.

## Overview

TWIB is part of the Orange Dev suite of tools, alongside [Orange Dev Tracker](https://github.com/sorukumar/orange-dev-tracker) and [Orange Dev Network](https://github.com/sorukumar/orange-dev-network).

It automatically fetches data, processes it into insightful metrics, and generates a static website hosted on GitHub Pages.

## Features

- **Automated Data Fetching**: Retrieves recent PRs from the Bitcoin Core repository and other key data sources.
- **Executive Summaries**: Generates high-level, readable summaries of dense technical discussions.
- **Developer Metrics**: Highlights top authors, contributors, and reviewers of the week.
- **Static Site Generation**: Compiles the data into a clean, modern HTML interface.

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/sorukumar/this-week-in-bitcoin.git
   cd this-week-in-bitcoin
   ```
2. Set up your virtual environment and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set up your `.env` file for any necessary API keys.
4. Run the main pipeline to fetch data and build the latest edition:
   ```bash
   python main.py
   ```
