import matplotlib.pyplot as plt
import tweepy
from io import BytesIO
import base64
from modules import tweepyauth
from nltk.tokenize import regexp_tokenize, TweetTokenizer, word_tokenize
from modules import business

api = tweepyauth.api
def histplot(userid, no_of_tweets):
    plt.switch_backend('AGG')
    plt.figure(figsize=(3, 3))
    hashtags = list()
    # make hashpattern 
    hashpattern = r'#\w+'
    # fetch tweets 
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        # get hashtags and save in list named hashtags 
        hashtags += regexp_tokenize(status.full_text, hashpattern)
    len_hashtags = len(hashtags)
    plt.hist(len_hashtags)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

"""
def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(3, 3))
    plt.title("testing")
    plt.plot(x, y)
    plt.xlabel('item')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph
"""