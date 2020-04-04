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

# Search Key Terms - "word1 OR word2 OR ..."
search_term = "комендант OR бишкек OR коронавирус OR чп OR карантин OR нетхудибезбобра OR HackCoronaForKG"

# Update geocode for area of interest
geo="42.882004,74.582748,75mi" # This is currently a 75mi radius around Bishkek, Kyrgyzstan

# Update count as needed
count=100

# Function to Pull tweets
public_tweets = api.search(search_term, geocode=geo, tweet_mode='extended', count=count)

# Export Tweets as JSON file
with open("kyr_tweet_4-4-20.json", "w") as JSONfile:
    json.dump(public_tweets, JSONfile)