"""
creates views for app
"""
import re
from django.shortcuts import render
from modules import business
from modules import searchhash, compareanalysis
from modules import visualizelib
from . models import CountryList
# Create your views here.
# HOME PAGE
def home(request):
    return render(request, 'business/index.html')

# GROWBUSINESS HOME PAGE
def growbusiness(request):
    return render(request, 'business/growbusiness.html')

# GROWBUSINESS FUNCTIONS PAGE
def gbfunctions(request):
    if request.method == 'POST': # check if user has clicked on submit button
        userid = str(request.POST.get('selectbusiness')) # get business name
        businesscategory = str(request.POST.get('selectcategory')) # get business category
        nooftweets = int(request.POST.get('nooftweets')) # get no. of tweets
        if "showtags" in request.POST:
            try:
                get_tags = business.get_hashes(userid, nooftweets)
                if len(get_tags) != 0:
                    lenofhashtags = len(get_tags[0])
                    context = {
                               'tags': get_tags[0],
                               'userid': userid,
                               'nooftweets': nooftweets,
                               'lenofhashtagsmsg': 'Unique Hashtags: ' + str(lenofhashtags),
                               'lenofhashtags': int(lenofhashtags / 2),
                               'userdesription': get_tags[1],
                               'userfollowers': get_tags[2],
                               'display_message': 'yes',
                                'mostusedhashtag': get_tags[0][0],
                               }
                    return render(request, 'business/gbfunctions.html', context)
                else:
                            context = {'nohashtagsmessage': 'No hashtag has been used'}
                            return render(request, 'business/gbfunctions.html', context)
            except:
                context = {
                    'errormessage': 'ohh,server not responding, try again in some time'
                }
                return render(request, 'business/gbfunctions.html', context)

        elif 'showfwords' in request.POST:
            try:
                get_words = business.most_common(userid, nooftweets)
                return render(request, 'business/gbfunctions.html', {'frequentwords': get_words, 'userid': userid, 'nooftweets': nooftweets})
            except:
                context = {
                    'errormessage': 'ohh,server not responding, try again in some time'
                }
                return render(request, 'business/gbfunctions.html', context)
        
        elif 'showurls' in request.POST:
            try:
                get_urls = business.get_urls(userid, nooftweets)
                    #print(get_urls)
                context = {'urls': get_urls,
                                   'userid': userid, 'nooftweets': nooftweets}
                return render(request, 'business/gbfunctions.html', context)
            except:
                context = {
                            'errormessage': 'Server not responding, try again in some time'
                        }
                return render(request, 'business/gbfunctions.html', context)
        elif 'showmentions' in request.POST:
            try:
                mentioncount = business.get_mentions(userid, nooftweets)
                mentions = list()
                for each_mention in mentioncount:
                            #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
                    mentions.append(
                                each_mention + ' : ' + str(mentioncount[each_mention]))
                    context = {'mentions': mentions}
                    return render(request, 'business/gbfunctions.html', context)
            except:
                context = {'errormessage': 'server not responding, try again in some time'}
                return render(request, 'business/gbfunctions.html', context)
        """
        try:
            # USER HAS SELECTED NO OF TWEETS
            no_of_tweets = int(nooftweets)
            if userid == 'Select Business' and businesscategory != 'Select Business Category':
                context = {'errormessage': 'You forgot to select Business Name',
                }
                return render(request, 'business/gbfunctions.html', context)

            elif userid == 'Select Business' and businesscategory == 'Select Business Category':
                context = {'errormessage' : 'You Forgot to select Business Name and Category'}
                return render(request, 'business/gbfunctions.html', context)

            elif userid == 'Select Business' and businesscategory != 'Select Business Category':
                context = {'errormessage': 'You Forgot to select Business Category'}
                return render(request, 'business/gbfunctions.html', context)

             # USER HAS SELECTED EVERY OPTION
            else: # go for functions
                if 'showtags' in request.POST: #and userid != 'Select Business' and businesscategory != 'Select Business Category':    
                    try:
                        get_tags = business.get_hashes(userid, no_of_tweets)
                        
                        if len(get_tags) != 0:
                            lenofhashtags = len(get_tags[0])
                            context = {
                               'tags': get_tags[0], 
                               'userid': userid,
                               'nooftweets': no_of_tweets,
                               'lenofhashtagsmsg': 'Unique Hashtags: '+ str(lenofhashtags),
                               'lenofhashtags': int(lenofhashtags / 2),
                               'userdesription' : get_tags[1],
                               'userfollowers' : get_tags[2],
                               'display_message' : 'yes',
                                'mostusedhashtag' : get_tags[0][0],
                               }
                            return render(request, 'business/gbfunctions.html', context)
                        else:
                            context = {'nohashtagsmessage': 'No hashtag has been used'}
                            return render(request, 'business/gbfunctions.html', context)
                    except:
                        context = {
                            'errormessage': 'ohh,server not responding, try again in some time'}
                        return render(request, 'business/gbfunctions.html', context)
            # click show frequenly used words button
                elif 'showfwords' in request.POST:
                    try:
                        get_words = business.most_common(userid, no_of_tweets)
                        return render(request, 'business/gbfunctions.html', {'frequentwords': get_words, 'userid': userid, 'nooftweets': no_of_tweets})
                    except:
                        context = {
                            'errormessage': 'ohh,server not responding, try again in some time'}
                        return render(request, 'business/gbfunctions.html', context)
                        
             #click show urls button
                elif 'showurls' in request.POST:
                    try:
                        get_urls = business.get_urls(userid, no_of_tweets)
                    #print(get_urls)
                        context = {'urls': get_urls,
                           'userid': userid, 'nooftweets': no_of_tweets}
                        return render(request, 'business/gbfunctions.html', context)
                    except:
                        context = {
                            'errormessage' : 'Server not responding, try again in some time'
                        }
                        return render(request, 'business/gbfunctions.html', context)

                elif 'showmentions' in request.POST:
                    try:
                        mentioncount = business.get_mentions(userid, no_of_tweets)
                        mentions = list()
                        for each_mention in mentioncount:
                        #new_hash.append(each_hash[0] + ': ' + str(each_hash[1]))
                            mentions.append(each_mention + ' : ' + str(mentioncount[each_mention]))
                        context = {'mentions': mentions}
                        return render(request, 'business/gbfunctions.html', context)
                    except:
                        context = {'errormessage' : 'server not responding, try again in some time'}
                        return render(request, 'business/gbfunctions.html', context)
            # if input boxe/boxes are empty
                elif 'showtestgraph' in request.POST:
                    try:
                        visualizelib.testplot(userid, no_of_tweets)
                        return render(request, 'business/gbfunctions.html')
                    
                    except:
                        context = {
                            'errormessage': 'server not responding, try again in some time'}
                        return render(request, 'business/gbfunctions.html', context)
                #imagepath = "business/assets/visualize/temp.png"
                    imagepath = "business/assets/visualize/temp.png"
                    context = {'imagepath': imagepath}
                    print(request.POST)
                    return render(request, 'business/gbfunctions.html', context)

        except:
            if userid == 'Select Business' and businesscategory != 'Select Business Category' and nooftweets != 'Select No of Tweets':
                context = {
                    'errormessage': 'Please Select Business Name',
                    'nooftweets' : nooftweets,
                    'businesscategory' : businesscategory,
                }
                return render(request, 'business/gbfunctions.html', context)
            
            elif userid != 'Select Business' and businesscategory != 'Select Business Category' and nooftweets == 'Select No of Tweets':
                context = {
                    'errormessage': 'You Forgot to Select No. of Tweets'}
                return render(request, 'business/gbfunctions.html', context)

            #elif userid != 'Select Business' and businesscategory == 'Select Business Category' and nooftweets == 'Select No of Tweets':
            #    context = {
            #        'errormessage': 'You Forgot to Select Business Category and No. of Tweets'}
            #    return render(request, 'business/gbfunctions.html', context)

            elif userid == 'Select Business' and businesscategory != 'Select Business Category' and nooftweets == 'Select No of Tweets':
                context = {
                    'errormessage': 'You Forgot to Select Business Name and No. of Tweets'}
                return render(request, 'business/gbfunctions.html', context)

            elif userid == 'Select Business' and businesscategory == 'Select Business Category' and nooftweets == 'Select No of Tweets':
                context = {'errormessage': 'You have not selected any option'}
                return render(request, 'business/gbfunctions.html', context)
        """
    else:
        return render(request, 'business/gbfunctions.html')

def sentimentanalysis(request):
    return render(request, 'business/sentimentanalysis.html')

def sfunctions(request):
    return render(request, 'business/sfunctions.html')

def comparativeanalysis(request):
    return render(request, 'business/comparativeanalysis.html')
    
def cfunctions(request):
    #print(request.POST)
    if request.method == 'POST':
        business1 = request.POST.get('business1')
        business2 = request.POST.get('business2')
        numberoftweets = int(request.POST.get('numberoftweets'))
        if business1 != '' and business2 != '':
            comparedata = compareanalysis.compare(business1, business2, numberoftweets)
            context = {
                'business1name': comparedata[0],
                'business2name': comparedata[1],
                'business1description': comparedata[2],
                'business2description': comparedata[3],
                'business1followers': comparedata[4],
                'business2followers': comparedata[5],
                'business1url': comparedata[6],
                'business2url': comparedata[7],
                'business1likes' : comparedata[8],
                'business2likes' : comparedata[9],
                'business1retweets' : comparedata[10],
                'business2retweets' : comparedata[11],
                'input1': business1,
                'input2': business2,
                'numberoftweets' : numberoftweets,
                'business1latestpostdate': comparedata[12],
                'business2latestpostdate' : comparedata[13],
                'business1latesttweettext': comparedata[14],
                'business2latesttweettext': comparedata[15],
                'business1latesttweetlikes' : comparedata[16],
                'business2latesttweetlikes': comparedata[17],
                'business1latesttweetretweets' : comparedata[18],
                'business2latesttweetretweets' : comparedata[19],
            }
            return render(request, 'business/cfunctions.html', context)

        elif (business1 != '') and (business2 == ''):
            context = {'business2error': 'Please input Business2 Username'}
            return render(request, 'business/comparativeanalysis.html', context)

        elif (business2 != '') and (business1 == ''):
            context = {'bussiness1error': 'Please input Business1 Username'}
            return render(request, 'business/cfunctions.html', context)

        else:
            context = {
                'bothinputserror': 'Please enter usernames for Business1 and Business2'}
            return render(request, 'business/cfunctions.html', context)

    return render(request, 'business/cfunctions.html')

def topbusiness(request):
    return render(request, 'business/topbusiness.html')

def tbfunctions(request):
    return render(request, 'business/tbfunctions.html')

def trends(request):
    # check if user has submitted form
    if request.method == "POST":

        # user has filled country name
        if 'countryname' in request.POST and 'seetweets' not in request.POST:
            # get trending topics
            # get country name
            country_name = str(request.POST.get('countryname')).capitalize()
            try:
                # VALIDATE FORM DATA
                if CountryList.objects.get(name=country_name):
                    # get country id
                    country = CountryList.objects.get(name=country_name)

                    trending_topics = searchhash.get_topics(country.countryid)

                    # make context for web page
                    context = {'topics': trending_topics,
                               'countryname': country_name}
                    print(request.POST)
                    # render web page
                    return render(request, 'business/trends.html', context)

            # if form is not valid
            except:
                return render(request, 'business/trends.html', {'error': 'Please Enter Correct Name'})

        # if user has selected trending topoic and want to see tweets
        elif 'selecttopic' and 'seetweets' in request.POST:
            country_name = str(request.POST.get('countryname')).capitalize()
            # get selected topic name
            trending_topic = request.POST.get('selecttopic')

            trending_tweets = searchhash.get_tweets(request.POST.get('selecttopic'))
            context = {'selected': trending_topic,
                       'trendingtweets':  trending_tweets,
                        'countryname' : country_name}
            return render(request, 'business/trends.html', context)
    # elif request.method =="GET":
    #	return render(request, 'business/hash.html',{'selected': request.Get.get('selectionvalue')})

    else:
        return render(request, 'business/trends.html')

def visualize(request):
    return render(request, 'business/visualize.html')

def vfunctions(request):
    if request.method == 'POST':
        try:

            # get business name
            userid = str(request.POST.get('selectbusiness'))
            nooftweets = int(request.POST.get('nooftweets'))  # get no. of tweets
            if 'hashtags' in request.POST:
            # get business name
                hash_chart = visualizelib.histplot(userid, nooftweets)
                return render(request, 'business/vfunctions.html', {'hashchart' : hash_chart, 'testmessage' : 'in if'})
            elif 'frequency' in request.POST:
                 # get business name
                freq_chart = visualizelib.freqplot(userid, nooftweets)
                return render(request, 'business/vfunctions.html', {'freqchart' : freq_chart})
            
            elif 'barchart' in request.POST:
                barchart = visualizelib.barchart(userid, nooftweets)
                return render(request, 'business/vfunctions.html', {'barchart' : barchart})
        except:
            context = {
                    'errormessage': 'api server not responding, try again in some time'}
            return render(request, 'business/vfunctions.html', context)

    else:    
        return render(request, 'business/vfunctions.html')

def allfunctions(request):
    return render(request, 'business/allfunctions.html')
