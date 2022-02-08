from dotenv.main import find_dotenv
import tweepy
import time
import random
from dotenv import load_dotenv
import os
import requests

load_dotenv(find_dotenv())
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


auth = tweepy.OAuthHandler(API_KEY,
                           API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,
                      ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication successful!\n")
except:
    print("Unable to authenticate...")

for i in range(0, 1000):
    try:
        response = requests.get(
            "https://api.spaceflightnewsapi.net/v3/articles")
        res = response.json()

        rand_no = random.randint(0, 9)
        tweet = res[rand_no]["summary"]+" "+res[rand_no]["url"]
        if(len(tweet) > 280):
            tweet = res[rand_no]["title"]+". "+res[rand_no]["url"]
            print("\nSummary longer than 280 so tweeted title")

        api.update_status(tweet)
        print(tweet+" Tweeted\n")
        i = i+1
        time.sleep(86400)
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break
