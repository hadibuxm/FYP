# import re
import tweepy
# import reurl
# from nltk.probability import FreqDist
from nltk.tokenize import regexp_tokenize, word_tokenize
# from collections import Counter
from modules import tweepyauth, business
#from modules import reurl
# from collections import Counter
# from nltk.corpus import stopwords

API = tweepyauth.api


def compare(business1, business2, numberoftweets, api=API):
    user1 = api.get_user(screen_name = business1)
    user2 = api.get_user(screen_name = business2)
    business1name = user1.name
    business2name = user2.name
    business1description = user1.description
    business2description = user2.description
    business1followers = user1.followers_count
    business2followers = user2.followers_count
    business1url = user1.entities['url']['urls'][0]['expanded_url']
    business2url = user2.entities['url']['urls'][0]['expanded_url']
    business1likes = int()
    business2likes = int()
    business1retweets = int()
    business2retweets = int()
    #business1mostlikedltweetikes = list()
    #business2mostlikedltweetikes = list()
    for status in tweepy.Cursor(api.user_timeline, screen_name=business1, tweet_mode="extended", include_rts=False).items(numberoftweets):
        business1likes += status.favorite_count
        business1retweets += status.retweet_count
        #business1mostlikedltweetikes.append(business1likes)
    for status in tweepy.Cursor(api.user_timeline, screen_name=business2, tweet_mode="extended", include_rts=False).items(numberoftweets):
        business2likes += status.favorite_count
        business2retweets += status.retweet_count
        #business2mostlikedltweetikes.append(business2likes)
    # latest tweet
    business1firstweet = api.user_timeline(screen_name = business1, tweet_mode = "extended")[0]
    business2firstweet = api.user_timeline(screen_name = business2, tweet_mode = "extended")[0]

    business1latestpostdate = business1firstweet._json["created_at"]
    business2latestpostdate = business2firstweet._json["created_at"]
    business1latesttweettext = business1firstweet._json["full_text"]
    business2latesttweettext = business2firstweet._json["full_text"]
    # first tweet likes
    try: 
        #business1firstweet._json['retweeted_status']
        business1latesttweetlikes = business1firstweet._json['retweeted_status']["favorite_count"]
    except:
        business1latesttweetlikes = business1firstweet._json["favorite_count"]
    
    try:
        #business2firstweet._json['retweeted_status']
        business2latesttweetlikes = business2firstweet._json['retweeted_status']["favorite_count"]
    except:
        business2latesttweetlikes = business2firstweet._json["favorite_count"]

    #business2latesttweetlikes = business2firstweet._json["favorite_count"]
    business1latesttweetretweets = business1firstweet._json['retweet_count']
    business2latesttweetretweets = business2firstweet._json['retweet_count']
    
    return business1name, business2name, business1description, business2description, business1followers, business2followers, business1url, business2url, business1likes, business2likes, business1retweets, business2retweets, business1latestpostdate, business2latestpostdate, business1latesttweettext, business2latesttweettext, business1latesttweetlikes, business2latesttweetlikes, business1latesttweetretweets, business2latesttweetretweets
    
