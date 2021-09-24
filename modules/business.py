# import re
import tweepy
import requests
# import reurl
# from nltk.probability import FreqDist
from nltk.tokenize import regexp_tokenize, word_tokenize
# from collections import Counter
from modules import tweepyauth, reurl
from collections import Counter
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

def get_title(link):
    url = link
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    if soup.title:
        return soup.title.string
    else:
        return 'COULD NOT GET TITLE, YOU CAN OPEN LINK TO SEE WHAT IS IN IT'

API = tweepyauth.api

"""
# function for releasing memory
def release_list(a):
   del a[:]
   del a
"""
# GET FREQUENTLY USED WORDS
def most_common(userid, no_of_tweets, api = API):
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
    #titles = list()
    #for link in urls:
    #    titles.append(get_title(link))
    return list(set(urls))
    
# RETURN HASHTAGS
def get_hashes(userid, no_of_tweets, api = API):
    user = api.get_user(screen_name=userid)
    user_description = user.description
    user_followers = user.followers_count
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
    new_hash = list()
    for each_hash in hashcount:
    #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
        new_hash.append(each_hash[0] + ' : ' + str(each_hash[1]))
    return new_hash, user_description, user_followers

# MENTIONS FUNCTION
def get_mentions(userid, no_of_tweets, api = API):
    user = api.get_user(screen_name=userid)
    user_description = user.description
    user_followers = user.followers_count
    mentions = list()
    # make hashpattern 
    mentionspattern = r'@\w+'
    # fetch tweets 
    for status in tweepy.Cursor(api.user_timeline, screen_name=userid, tweet_mode="extended").items(no_of_tweets):
        # get hashtags and save in list named hashtags 
        mentions += regexp_tokenize(status.full_text, mentionspattern)
    mentioncount = Counter(mentions)
    return mentioncount, user_description, user_followers
    """
    new_mentions = list()
    for each_mention in mentioncount:
    #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
        new_mentions.append(each_mention + ' : ' + str(mentioncount[each_mention]))
    return new_mentions
    """
