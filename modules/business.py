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


def release_list(a):
   del a[:]
   del a

# GET FREQUENTLY USED WORDS
def most_common(userid, no_of_tweets, api = API):
    tokens = []
    stop_words = stopwords.words("english")
    # GET TEXT FROM DATAFRAME
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended", exclude_replies=True, include_rts=False).items(no_of_tweets):
        # MAKE TOKENS OF TEXT AFTER CONVERTING IT TO LOWERCASE
        text = status.full_text
        t = word_tokenize(text.lower())
        # ITERATE OVER TOKEN
        for word in t:
            # IF WORD IS ALPHABETICAL
            if word.isalpha(): # IGNORE ALL HASHTAGS 
                # IF WORD IS NOT IN STOPWORDS LIST
                if word not in stop_words:
                    tokens.append( word)
    fwords = []
    countwords = Counter(tokens)
    #release_list(tokens), it takes 5 more seconds 
    for word in countwords.most_common(10):
        fwords.append(word[0] + ':' + " used " + str(word[1]) + ' times')
    return fwords
    
# GET URLS
def get_urls(userid, no_of_tweets, api = API):
    urls = list()
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended", include_rts = False).items(no_of_tweets):
        urls += regexp_tokenize(status.full_text , reurl.url_validate)
    titles = list()
    for link in urls:
        titles.append(linktitle.get_title(link))
    return list(set(urls)), titles
    
# RETURN HASHTAGS
def get_hashes(userid, no_of_tweets, api = API):

    # make empty list 
    hashtags = list()
    # make hashpattern 
    hashpattern = r'#\w+'
    # fetch tweets 
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        # get hashtags and save in list named hashtags 
        hashtags += regexp_tokenize(status.full_text, hashpattern)

    # return list of hashtags
    hashcount = Counter(hashtags)
    new_hash = list()
    for each_hash in hashcount:
    #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
        new_hash.append(each_hash + ' : ' + str(hashcount[each_hash]))
    return new_hash

# MENTIONS FUNCTION
def get_mentions(userid, no_of_tweets, api = API):
    mentions = list()
    # make hashpattern 
    mentionspattern = r'@\w+'
    # fetch tweets 
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        # get hashtags and save in list named hashtags 
        mentions += regexp_tokenize(status.full_text, mentionspattern)
    mentioncount = Counter(mentions)
    new_mentions = list()
    for each_hash in mentioncount:
    #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
        new_mentions.append(each_hash + ' : ' + str(mentioncount[each_hash]))
    return new_mentions
