import matplotlib.pyplot as plt
import tweepy
from io import BytesIO
import base64
from nltk.probability import FreqDist
from modules import tweepyauth, business
from nltk.tokenize import regexp_tokenize, TweetTokenizer, word_tokenize
from collections import Counter
from nltk.corpus import stopwords

api = tweepyauth.api

def histplot(userid, no_of_tweets):
    plt.switch_backend('AGG')
    #plt.figure(figsize=(5, 5))
    hashtags = list()
    # make hashpattern 
    hashpattern = r'#\w+'
    # fetch tweets 
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        # get hashtags and save in list named hashtags 
        hashtags += regexp_tokenize(status.full_text, hashpattern)
    len_hashtags = [len(hashtag) for hashtag in hashtags]
    plt.hist(len_hashtags)
    plt.tight_layout()
    graph = get_graph()
    return graph

def barchart(userid, no_of_tweets):
    plt.switch_backend('AGG')
    plt.figure(figsize = (3, 3))
    mentioncount = business.get_mentions(userid, no_of_tweets)
    mentions = list()
    len_mentions = list()
    for each_mention in mentioncount.most_common(5):
        #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
        mentions.append(each_mention[0])
        len_mentions.append(each_mention[1])
    plt.bar(mentions, len_mentions)
    plt.xlabel("Mentions")
    plt.ylabel("No of Times")
    plt.title("Top 5 Mentions")
    plt.xticks(rotation = 5)
    graph = get_graph()
    return graph

def freqplot(userid, no_of_tweets):
    plt.switch_backend('AGG')
    tokens = []
    stop_words = stopwords.words("english")
    # GET TEXT FROM DATAFRAME
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended", include_rts=False).items(no_of_tweets):
        # MAKE TOKENS OF TEXT AFTER CONVERTING IT TO LOWERCASE
        text = status.full_text
        t = word_tokenize(text.lower())
        # ITERATE OVER TOKEN
        for word in t:
            # IF WORD IS ALPHABETICAL
            if word.isalpha():  # IGNORE ALL HASHTAGS
                # IF WORD IS NOT IN STOPWORDS LIST
                if word not in stop_words:
                    tokens.append(word)
    
    fdist = FreqDist(tokens)
    fdist.plot(20, cumulative=False)
    plt.xlabel("commonly used words")
    plt.ylabel("no of times used")
    #plt.xticks(rotation = 45)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_graph():
    # creates memory buffer 
    buffer = BytesIO()
    # save image in buffer in png format
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # get buffer value in string form
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
