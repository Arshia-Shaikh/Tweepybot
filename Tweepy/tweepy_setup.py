import tweepy

# Credentials
api_key = "bmaY1W5DgTByjV4UwYD9BNPk6"
api_secret = "PmCyn2U2ietSgor19aXE7L2vNg1RD4zPQ1ynvPYQv5Pblk3RXK"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAACUgoAEAAAAA5J8DIMVUp9hMQFSAsgJiNDxruvE%3D6h0qFrTSPRKcrWn2FYVDcKiNj2EkZo0bEwzl3TUZzDY0LZXkAx"
access_token = "1388897091716476929-dHjnxI5v79dyAAlvqrObIFsE3SNR57"
access_token_secret = "qU7VXFlzywJR1cci1Ss5lIu9H6QCeAtU0N1vNeXcNvlNT"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Creating a tweet to test the bot
client.create_tweet(text="Hello World")