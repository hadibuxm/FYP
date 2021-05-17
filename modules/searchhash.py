#import tweepyauth
from . import tweepyauth
from textblob import TextBlob

# 23424922 is default id for Pakistan
def get_topics(country_woid = 23424922 , api = tweepyauth.api):
    trends = api.trends_place(id = country_woid) 
    list_trends = list()
    #count = 1
    for value in trends: 
        for trend in value['trends']: 
            list_trends.append(trend['name'])
    return list_trends

def get_tweets(q, api = tweepyauth.api):
    results = api.search(q , count = 100, result_type = 'mixed', tweet_mode = 'extended')
    tweet_list = list()
    
    for tweet in results:
    # printing the text stored inside the tweet object
        tweet_list.append(tweet.user.screen_name +" "+ "Tweeted:"+tweet.full_text)
    return tweet_list


def sentiment(q, api = tweepyauth.api):
    results = api.search(q , count = 100, result_type = 'mixed', tweet_mode = 'extended')
    polarity = list()
    for tweet in results:
        if TextBlob(tweet.full_text).sentiment.polarity > 0:
            polarity.append("Positive")
        elif TextBlob(tweet.full_text).sentiment.polarity < 0:
            polarity.append("Negative")
        else:
            polarity.append("Neutral") 
    return polarity