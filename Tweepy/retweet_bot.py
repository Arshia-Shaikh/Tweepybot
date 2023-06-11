# Importing Tweepy and time
import tweepy
import time

# Credentials
api_key = "bmaY1W5DgTByjV4UwYD9BNPk6"
api_secret = "PmCyn2U2ietSgor19aXE7L2vNg1RD4zPQ1ynvPYQv5Pblk3RXK"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAACUgoAEAAAAA5J8DIMVUp9hMQFSAsgJiNDxruvE%3D6h0qFrTSPRKcrWn2FYVDcKiNj2EkZo0bEwzl3TUZzDY0LZXkAx"
access_token = "1388897091716476929-dHjnxI5v79dyAAlvqrObIFsE3SNR57"
access_token_secret = "qU7VXFlzywJR1cci1Ss5lIu9H6QCeAtU0N1vNeXcNvlNT"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        # Retweeting the tweet
        try:
            # Retweet
            client.retweet(tweet.id)

            # Printing Tweet
            print(tweet.text)

            # Delay
            #time.sleep(1)

        except Exception as error:
            # Error
            print(error)


# Creating Stream object
stream = MyStream(bearer_token=bearer_token)

# Adding terms to search rules
rule = tweepy.StreamRule("(#Python OR #programming) (-is:retweet -is:reply)") 
stream.add_rules(rule, dry_run=True)

# Starting stream
stream.sample()
stream.filter()