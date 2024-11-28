
# Reddit Stock Sentiment Scraper

## Overview
This script scrapes Reddit posts from subreddits like `r/StockMarket` and `r/WallStreetBets`, focusing on stock-related discussions. It identifies posts mentioning specific stock tickers (e.g., $AAPL, $TSLA) and saves the data to a CSV file.

## Files Included
- **reddit_scraper.py**: The main Python script to scrape Reddit posts.
- **requirements.txt**: List of required Python libraries.
- **README.md**: Instructions for setting up and running the scraper.

## Setup and Usage

### 1. Prerequisites
- Python 3.x installed on your system.

### 2. Install Dependencies
Run the following command to install the required libraries:
```
pip install -r requirements.txt
```

### 3. Get Reddit API Credentials
1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps).
2. Create a new application.
3. Note down your **client_id**, **client_secret**, and **user_agent**.

### 4. Update the Script
Replace the placeholders in `reddit_scraper.py` with your Reddit API credentials:
```python
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="StockSentimentScraper"
)
```

### 5. Run the Script
Execute the following command to run the scraper:
```
python reddit_scraper.py
```

The scraped data will be saved as `reddit_stock_data.csv` in the same directory.

## Notes
- You can modify the subreddits and stock tickers in the script as needed.
- Adjust the `limit` parameter to control the number of posts scraped.
