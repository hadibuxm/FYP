import tweepy
from tweepy import OAuthHandler
from tweepy import API
from django.contrib.auth.models import User
# consumer key
consumer_key = 'iArebIhsuxBQzoG4GAU19oi4d'

# consumer secret
consumer_secret = 'FfHulTVF3SFqinYOmfhhEP94h6YVDXhKS0u2jeozuSnyQT7wHd'
# Consumer key authentication
auth = OAuthHandler(consumer_key, consumer_secret)

# access token
access_token = '3231450572-F9UTzJhx7z0Ty4BPi7x90L66dE0868jhXtKcPVq'

access_token_secret = '0iXDqD1OaJJRkiM9ctN6Go9B87JByBjY0Oj7gfvKPrmr6'

# Access key authentication
auth.set_access_token(access_token, access_token_secret)

# Set up the API with the authentication handler
api = API(auth)
authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticate.set_access_token(access_token, access_token_secret)
# API
api = tweepy.API(authenticate, wait_on_rate_limit = True)