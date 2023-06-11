# Importing Tweepy and time
import tweepy
import time

# Credentials (INSERT YOUR KEYS AND TOKENS IN THE STRINGS BELOW)
api_key = "bmaY1W5DgTByjV4UwYD9BNPk6"
api_secret = "PmCyn2U2ietSgor19aXE7L2vNg1RD4zPQ1ynvPYQv5Pblk3RXK"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAACUgoAEAAAAA5J8DIMVUp9hMQFSAsgJiNDxruvE%3D6h0qFrTSPRKcrWn2FYVDcKiNj2EkZo0bEwzl3TUZzDY0LZXkAx"
access_token = "1388897091716476929-dHjnxI5v79dyAAlvqrObIFsE3SNR57"
access_token_secret = "qU7VXFlzywJR1cci1Ss5lIu9H6QCeAtU0N1vNeXcNvlNT"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

search_terms = ["python", "programming", "coding"]

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when the stream is working
    def on_connect(self):

        print("Connected")


    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        # Displaying tweet in console
        if tweet.referenced_tweets == None:
            print(tweet.text)
            client.like(tweet.id)

            # Delay between tweets
            time.sleep(0.5)
        

# Creating Stream object
stream = MyStream(bearer_token=bearer_token)

# Adding terms to search rules
# It's important to know that these rules don't get deleted when you stop the
# program, so you'd need to use stream.get_rules() and stream.delete_rules()
# to change them, or you can use the optional parameter to stream.add_rules()
# called dry_run (set it to True, and the rules will get deleted after the bot
# stopped running).
for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

# Starting stream
stream.sample()
stream.filter(tweet_fields=["referenced_tweets"])
