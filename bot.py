import tweepy
import os
import logging
from dotenv import load_dotenv
from random import randrange
import time

load_dotenv()

logger = logging.getLogger()

API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
   API_KEY, API_KEY_SECRET,
   ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

def get_quote():
    # Get a random line from bouqala.csv file 
    with open("bouqala.csv", "r") as f:
        lines = f.readlines()
        random_line = lines[randrange(len(lines)-1)]
        return random_line

def get_last_tweet(file):
    f = open(file, 'r')
    lastId = int(f.read().strip())
    f.close()
    return lastId

def put_last_tweet(file, Id):
    f = open(file, 'w')
    f.write(str(Id))
    f.close()
    logger.info("Updated the file with the latest tweet Id")
    return

def respondToTweet(file='tweet_ID.txt'):
    mentions = api.mentions_timeline() if os.stat(file).st_size == 0 else api.mentions_timeline(since_id=get_last_tweet(file))
    if len(mentions) == 0:
        return

    new_id = 0
    logger.info("someone mentioned me...")

    for mention in reversed(mentions):
        logger.info(str(mention.id) + '-' + mention.text)
        new_id = mention.id

        if 'عقدت' in mention.text:
            logger.info("Responding back with a random bouqala to -{}".format(mention.id))
            try:
                bouqala = get_quote()

                logger.info("liking and replying to tweet")

                api.create_favorite(mention.id)
                api.update_status('@' + mention.user.screen_name + ": " + bouqala)
            except:
                logger.info("Already replied to {}".format(mention.id))

    put_last_tweet(file, new_id)

if __name__=="__main__":
    respondToTweet()
    time.sleep(60)