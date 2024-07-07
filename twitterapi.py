import tweepy 
import configparser
import json


# read configs 
config = configparser.ConfigParser()
config.read('config.txt')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication 
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

#integrating the data to a global source

tweets_dict = [tweet._json for tweet in public_tweets]

with open('api_data.json', 'a') as file:  #open the file in append mode
    file.write(json.dumps({"source": "twitter", "data": tweets_dict}))  #write the JSON data to the file
    file.write('\n')  #write a newline character to the file