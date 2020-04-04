# Dependencies
import tweepy
import json

# Twitter API Keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# User Account
target = "Mirsuljan"

# Update count as necessary
count=100

# Function to Pull User's Most recent Tweets
user_tweet = api.user_timeline(id=target, count=count)

# View Most recent tweet
user_tweet[0]

# Export Tweets as JSON file
with open("Mirsuljan_tweet_4-4-20_9-20PM.json", "w") as JSONfile:
    json.dump(user_tweet, JSONfile)