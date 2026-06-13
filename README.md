# Web Scraper - Quotes

A Python web scraper that extracts quotes from all 10 pages of [quotes.toscrape.com](https://quotes.toscrape.com) and saves them to a JSON file.

## Features
- Scrapes all 10 pages automatically using pagination
- Error handling for network, timeout and HTTP errors
- Saves output to quotes.json with proper Unicode support

## Libraries Used
- requests
- beautifulsoup4

## How to Run
pip install requests beautifulsoup4
python webscapper.py

## Output
Creates quotes.json with 100 quotes containing quote text and author name