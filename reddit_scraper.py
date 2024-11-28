
import praw
import pandas as pd
import re
from datetime import datetime

# Step 1: Reddit API Authentication
reddit = praw.Reddit(
    client_id="P8Oh9ZSxHALZFNAqBA_LmQ",         # Replace with your Reddit API Client ID
    client_secret="gDPA0oX6X_a86o2nhNxsx5IlQij0bw", # Replace with your Reddit API Client Secret
    user_agent="StockSentimentScraper"  # Name your script
)

# Step 2: Define the subreddits and keywords to scrape
subreddits = ["StockMarket", "WallStreetBets"]
keywords = [
    r"\$AAPL", r"\$TSLA", r"\$GOOG", r"\$AMZN", r"\$META", r"\$MSFT", 
    r"\$NVDA", r"\$AMD", r"\$SPY", r"\$SPX", r"\$QQQ", r"\$NFLX", 
    r"\$BA", r"\$DIS", r"\$TSM", r"\$INTC", r"\$BTC", r"\$ETH", 
    r"\$SOL", r"\$XRP", r"\$DOGE", r"\$LTC", r"bullish", r"bearish", 
    r"market crash", r"recession", r"short squeeze", r"IPO", r"dividends",
    r"earnings report", r"options trading", r"stocks to buy", r"buying the dip",
    
    # Technology-related keywords:
    r"5G", r"AI", r"Artificial Intelligence", r"VR", r"Virtual Reality", r"AR", 
    r"Augmented Reality", r"Cloud Computing", r"IoT", r"Internet of Things", 
    r"Semiconductors", r"Blockchain", r"Robotics", r"Cybersecurity", r"Quantum Computing",
    r"Autonomous vehicles", r"Wearables", r"Tech IPO", r"Tech Mergers", r"Tech Acquisitions",
    r"Tech Earnings", r"Tech Stocks", r"Tech Disruption", r"Tech Innovation",
    
    # Sports-related keywords:
    r"NFL", r"NBA", r"MLB", r"NHL", r"FIFA", r"NASCAR", r"WWE", r"ATP", r"WTA",
    r"$LAL", r"$GSW", r"$NYK", r"$DODGERS", r"$Yankees", r"$CAVS", r"$Cowboys",
    r"$Patriots", r"$Barca", r"$RealMadrid", r"$LeBronJames", r"$CristianoRonaldo", 
    r"$Messi", r"$TigerWoods", r"$RogerFederer", r"Sports Sponsorships", 
    r"Sports Broadcasting Rights", r"Sports Ticketing", r"Fantasy Sports", r"Sports Betting",
    r"E-Sports", r"Sports Marketing", r"Athlete Endorsements"
]


# Step 3: Function to clean text
def clean_text(text):
    text = re.sub(r"http\\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z0-9\\s\\$]", "", text)  # Remove special characters
    text = text.lower().strip()  # Lowercase and strip whitespace
    return text

# Step 4: Scrape data from Reddit
def scrape_reddit(subreddit, keywords, limit=100):
    scraped_data = []
    subreddit_obj = reddit.subreddit(subreddit)
    
    # Fetch posts from the subreddit
    for post in subreddit_obj.hot(limit=limit):  # Change 'hot' to 'new' or 'top' as needed
        if any(re.search(keyword, post.title, re.IGNORECASE) for keyword in keywords):
            data = {
                "subreddit": subreddit,
                "title": clean_text(post.title),
                "text": clean_text(post.selftext),
                "created_utc": datetime.utcfromtimestamp(post.created_utc),
                "upvotes": post.score,
                "comments": post.num_comments
            }
            scraped_data.append(data)
    
    return scraped_data

# Step 5: Scrape and save data
if __name__ == "__main__":
    all_data = []
    for subreddit in subreddits:
        data = scrape_reddit(subreddit, keywords, limit=100)
        all_data.extend(data)

    # Convert to a DataFrame
    df = pd.DataFrame(all_data)

    # Save to CSV
    df.to_csv("reddit_stock_data.csv", index=False)
    print(f"Scraped {len(df)} posts. Data saved to 'reddit_stock_data.csv'.")
