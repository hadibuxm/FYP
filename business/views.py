"""
creates views for app
"""
from django.shortcuts import render
from modules import business
from modules import searchhash, compareanalysis
from modules import visualize
from . models import CountryList
# Create your views here.

def home(request):
    return render(request, 'business/index.html')

def growbusiness(request):
    return render(request, 'business/growbusiness.html')

def gbfunctions(request):
    if request.method == 'POST':
        print(request.POST)
        try:
            userid = str(request.POST.get('selectbusiness'))
            no_of_tweets = int(request.POST.get('nooftweets'))

            # click show tags button
            if 'showtags' in request.POST and userid != 'Select Business':
                #print(request.POST)
                # get tags
                get_tags = business.get_hashes(userid, no_of_tweets)
                if len(get_tags) != 0:
                    lenofhashtags = len(get_tags)
                    context = {'tags': get_tags, 'userid': userid,
                               'nooftweets': no_of_tweets,
                               'lenofhashtagsmsg': 'total no. of hashtags used:' + str(lenofhashtags) ,
                               'lenofhashtags':int(lenofhashtags / 2),
                              }
                    return render(request, 'business/gbfunctions.html', context)
                else:
                    context = {'nohashtagsmessage': 'No hashtag has been used'}
                    return render(request, 'business/gbfunctions.html', context)

            # click show frequenly used words button
            elif 'showfwords' in request.POST:
                get_words = business.most_common(userid, no_of_tweets)
                return render(request, 'business/gbfunctions.html', {'frequentwords': get_words, 'userid': userid, 'nooftweets': no_of_tweets})
             #click show urls button
            elif 'showurls' in request.POST:
                get_urls = business.get_urls(userid, no_of_tweets)
                context = {'urls': get_urls[0], 'linktitles': get_urls[1],
                           'userid': userid, 'nooftweets': no_of_tweets}
                return render(request, 'business/gbfunctions.html', context)

            elif 'showmentions' in request.POST:
                mentions = business.get_mentions(userid, no_of_tweets)
                context = {'mentions': mentions}
                return render(request, 'business/gbfunctions.html', context)
            # if input boxe/boxes are empty
            elif 'showtestgraph' in request.POST:
                visualize.testplot(userid, no_of_tweets)
                #imagepath = "business/assets/visualize/temp.png"
                imagepath = "business/assets/visualize/temp.png"
                context = {'imagepath': imagepath}
                print(request.POST)
                return render(request, 'business/gbfunctions.html', context)

            else:
                return render(request, 'business/gbfunctions.html', {'errormessage': 'Please Enter Correct Data'})
        except:
            return render(request, 'business/gbfunctions.html', {'errormessage': 'Please enter Correct Data'})
    else:
        return render(request, 'business/gbfunctions.html')


def sentimentanalysis(request):
    return render(request, 'business/sentimentanalysis.html')


def comparativeanalysis(request):
    print(request.POST)
    if request.method=='POST':
        business1 = request.POST.get('business1')
        business2 = request.POST.get('business2')
        if business1!='' and business2!='':
            comparedata = compareanalysis.compare(business1, business2)
            context = {
                'business1name' : comparedata[0],
                'business2name' : comparedata[1],
                'business1description' : comparedata[2],
                'business2description' : comparedata[3],
                'business1followers' : comparedata[4],
                'business2followers' : comparedata[5],
                'business1url' : comparedata[6],
                'business2url' : comparedata[7],
                'input1': business1,
                'input2' : business2
            }
            return render(request, 'business/comparativeanalysis.html', context)

        elif (business1 !='') and (business2 ==''):
            print('in first elif')
            context = {'business2error' : 'Please input Business2 Username'}
            return render(request, 'business/comparativeanalysis.html', context)

        elif (business2!='') and (business1==''):
            print('in 2nd elif')
            context = {'bussiness1error' : 'Please input Business1 Username'}
            return render(request, 'business/comparativeanalysis.html', context)

        else:
            print('in else')
            context = {'bothinputserror' : 'Please enter usernames for Business1 and Business2'}
            return render(request, 'business/comparativeanalysis.html', context)
        
    return render(request, 'business/comparativeanalysis.html')


def topbusiness(request):
    return render(request, 'business/topbusiness.html')


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
            # get selected topic name
            trending_topic = request.POST.get('selecttopic')

            trending_tweets = searchhash.get_tweets(
                request.POST.get('selecttopic'))
            return render(request, 'business/trends.html', {'selected': trending_topic, 'trendingtweets':  trending_tweets})
    # elif request.method =="GET":
    #	return render(request, 'business/hash.html',{'selected': request.Get.get('selectionvalue')})

    else:
        return render(request, 'business/trends.html')

