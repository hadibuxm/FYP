# import re
import tweepy
# import reurl
# from nltk.probability import FreqDist
from nltk.tokenize import regexp_tokenize, word_tokenize
# from collections import Counter
from modules import tweepyauth
from modules import reurl, linktitle
from collections import Counter
from nltk.corpus import stopwords

API = tweepyauth.api

def compare(business1, business2, api = API):
    user1 = api.get_user(screen_name = business1)
    user2 = api.get_user(screen_name = business2)
    business1name = user1.name
    business2name = user2.name
    business1description = 'Description: ' + user1.description
    business2description = 'Description: ' + user2.description
    business1followers = 'Followers: ' + str(user1.followers_count)
    business2followers = 'Followers: ' + str(user2.followers_count)
    business1url = 'URL: ' + user1.entities['url']['urls'][0]['expanded_url']
    business2url = 'URL: ' + user2.entities['url']['urls'][0]['expanded_url']
    return business1name, business2name, business1description, business2description, business1followers, business2followers, business1url, business2url
    
