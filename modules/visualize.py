import matplotlib.pyplot as plt
import tweepy
from modules import tweepyauth
from nltk.tokenize import regexp_tokenize, TweetTokenizer, word_tokenize
from modules import business

api = tweepyauth.api
def testplot(userid, no_of_tweets):
    hashtags = list()
    # make hashpattern 
    hashpattern = r'#\w+'
    # fetch tweets 
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        # get hashtags and save in list named hashtags 
        hashtags += regexp_tokenize(status.full_text, hashpattern)
    len_hashtags = len(hashtags)
    plt.hist(len_hashtags)
    plt.savefig('business/static/business/assets/visualize/temp')
