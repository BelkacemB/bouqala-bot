import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

oauth1_user_handler = tweepy.OAuth1UserHandler(
    API_KEY, API_KEY_SECRET,
    callback="oob"
)

print(oauth1_user_handler.get_authorization_url())

verifier = input("Input PIN: ")

access_token, access_token_secret = oauth1_user_handler.get_access_token(
    verifier
)

print("Access token:", access_token)
print("Access token secret:", access_token_secret)
