import tweepy
from config.credentials import BEARER_TOKEN

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_latest_tweet(username):
    try:
        # Step 1: Get user ID from username
        user = client.get_user(username=username)
        user_id = user.data.id

        # Step 2: Fetch recent tweets
        tweets = client.get_users_tweets(id=user_id, max_results=1)
        if tweets.data:
            return tweets.data[0].text
        else:
            return "User has no tweets or tweets are protected."
    except Exception as e:
        return f"❌ Error fetching tweet: {e}"