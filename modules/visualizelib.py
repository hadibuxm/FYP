import matplotlib.pyplot as plt
import seaborn as sns
import tweepy
from io import BytesIO
import base64
import nltk
import warnings
warnings.filterwarnings("ignore")
import itertools
import re
import pandas as pd
import networkx as nx
from nltk.probability import FreqDist
from modules import tweepyauth, business
from nltk.tokenize import regexp_tokenize, TweetTokenizer, word_tokenize
from collections import Counter
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
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

def mentionsbarchart(userid, no_of_tweets):
    plt.switch_backend('AGG')
    #plt.figure(figsize = (3, 3))
    mentioncount = business.get_mentions(userid, no_of_tweets)[0]
    mentions = list()
    len_mentions = list()
    for each_mention in mentioncount.most_common(10):
        #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
        mentions.append(each_mention[0])
        len_mentions.append(each_mention[1])
    sns.barplot(y = mentions, x = len_mentions)
    plt.xlabel("No. of times mentioned")
    #plt.ylabel("No of Times")
    plt.title(userid)
    plt.tight_layout()
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


def wordfrequencywordcloud(userid, no_of_tweets):
    plt.switch_backend('AGG')
    tweets = str()
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        tweets += status.full_text
    stopwords = set(STOPWORDS)
    stopwords.update(['t.co', 't', 'co'])
    # Create and generate a word cloud image:
    wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white").generate(tweets)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout()
    graph = get_graph()
    return graph


def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    no_url = url_pattern.sub(r'', txt)

    return no_url


def bigrams(userid, no_of_tweets):
    plt.switch_backend('AGG')
    tweets = list()
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        tweets.append(status.full_text)
    tweets_no_urls = [remove_url(tweet) for tweet in tweets]
    words_in_tweet = [tweet.lower().split() for tweet in tweets_no_urls]
    stop_words = set(STOPWORDS)
    tweets_nsw = [[word for word in tweet_words if not word in stop_words]
              for tweet_words in words_in_tweet]
    terms_bigram = [list(nltk.bigrams(tweet)) for tweet in tweets_nsw]
    bigrams = list(itertools.chain(*terms_bigram))
    # Create counter of words in clean bigrams
    bigram_counts = Counter(bigrams)
    bigram_df = pd.DataFrame(bigram_counts.most_common(20),
                             columns=['bigram', 'count'])

    d = bigram_df.set_index('bigram').T.to_dict('records')
    # Create network plot
    G = nx.Graph()
    # Create connections between nodes
    for k, v in d[0].items():
        G.add_edge(k[0], k[1], weight=(v * 10))

    #G.add_node(userid, weight=100)
    fig, ax = plt.subplots(figsize=(10, 8))
    pos = nx.spring_layout(G, k=2)

    # Plot networks
    nx.draw_networkx(G, pos,
                     font_size=14,
                 width=3,
                 edge_color='grey',
                 node_color='green',
                 with_labels=False,
                 ax=ax)
    
    # Create offset labels
    for key, value in pos.items():
        x, y = value[0]+.135, value[1]+.045
        ax.text(x, y,
            s=key,
            bbox=dict(facecolor='yellow', alpha=0.8),
            horizontalalignment='center', fontsize=13)
    plt.tight_layout()
    graph = get_graph()
    return graph
def likeschart(userid, no_of_tweets):
    plt.switch_backend('AGG')
    tweets = api.user_timeline(userid, count=no_of_tweets,  tweet_mode="extended")
    dates = [tweet.created_at for tweet in tweets]
    likes = [tweet.favorite_count for tweet in tweets]
    plt.style.use("fivethirtyeight")
    data = {'Dates': dates, 'likes': likes}
    df = pd.DataFrame(data)
    df = df.set_index('Dates')
    ax = df.plot(color='blue')
    ax.set_ylabel('likes')
    ax.set_title(str(no_of_tweets) + "tweets")
    plt.tight_layout()
    graph = get_graph()
    return graph

# RETURN HASHTAGS
def get_hashes(userid, no_of_tweets, api=api):
    user = api.get_user(screen_name=userid)
    #user_description = user.description
    #user_followers = user.followers_count
    # make empty list
    hashtags = list()
    # make hashpattern
    hashpattern = r'#\w+'
    # fetch tweets
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        # get hashtags and save in list named hashtags
        hashtags += regexp_tokenize(status.full_text, hashpattern)
    # return list of unique hashtags with no. of times they have been used
    hashcount = Counter(hashtags).most_common()
    hashes = list()
    hash_freq = list()
    for each_hash in hashcount:
        #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
        hashes.append(each_hash[0])
        hash_freq.append(each_hash[1])
    return hashes, hash_freq

def hashtagsbarchart(userid, no_of_tweets):
    plt.switch_backend('AGG')
    #plt.figure(figsize=(5,5))
    hashtags = get_hashes(userid, no_of_tweets)
    if len(hashtags[0]) <= 10 and len(hashtags[0]) != 0:
        hashes = hashtags[0]
        hash_freq = hashtags[1]
        sns.barplot(x=hash_freq[0:], y=hashes[0:])
        plt.title(userid)
        plt.tight_layout()
        graph = get_graph()
        return graph
    elif len(hashtags[0]) >= 10 and len(hashtags[0]) != 0:
        hashes = hashtags[0]
        hash_freq = hashtags[1]
        sns.barplot(x=hash_freq[0:10], y=hashes[0:10])
        plt.title(userid)
        plt.tight_layout()
        graph = get_graph()
        return graph
    else:
        return int(0)

        
def retweetschart(userid, no_of_tweets):
    plt.switch_backend('AGG')
    tweets = api.user_timeline(
        userid, count=no_of_tweets,  tweet_mode="extended")
    dates = [tweet.created_at for tweet in tweets]
    retweets = [tweet.retweet_count for tweet in tweets]
    plt.style.use("fivethirtyeight")
    data = {'Dates': dates, 'retweets': retweets}
    df = pd.DataFrame(data)
    df = df.set_index('Dates')
    ax = df.plot(color='blue')
    ax.set_ylabel('Retweets')
    ax.set_title(str(no_of_tweets) + " tweets")
    #ax.axvline(df.index[df['retweets'] == df['retweets'].max()], color = 'red', linestyle='--')
    #ax.axhline(df['retweets'].max(), color = 'green',linestyle = '--')
    plt.tight_layout()
    graph = get_graph()
    return graph

def hashtagspiechart(userid, no_of_tweets):
    plt.switch_backend('AGG')
    hashtags = get_hashes(userid, no_of_tweets)
    if len(hashtags[0]) <= 5 and len(hashtags[0]) != 0:
        hashes = hashtags[0][0:]
        hash_freq = hashtags[1][0:]
        fig = plt.figure()
        plt.tight_layout()
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        ax.pie(hash_freq, labels=hashes, autopct='%1.2f%%')
        graph = get_graph()
        return graph
    elif len(hashtags[0]) >= 5 and len(hashtags[0]) != 0:
        hashes = hashtags[0][0:5]
        hash_freq = hashtags[1][0:5]
        fig = plt.figure()
        plt.tight_layout()
        #plt.title(userid)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.axis('equal')
        ax.pie(hash_freq, labels=hashes, autopct='%1.2f%%')
        graph = get_graph()
        return graph
    else:
        return 0

def mentionspiechart(userid, no_of_tweets):
    plt.switch_backend('AGG')
    mentioncount = business.get_mentions(userid, no_of_tweets)[0]
    mentions = list()
    len_mentions = list()
    for each_mention in mentioncount.most_common(10):
        #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
        mentions.append(each_mention[0])
        len_mentions.append(each_mention[1])
    fig = plt.figure()
    plt.tight_layout()
    #plt.title(userid)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    ax.pie(len_mentions, labels=mentions, autopct='%1.2f%%')
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
