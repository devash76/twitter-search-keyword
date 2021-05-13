from django.shortcuts import render,HttpResponse

import tweepy


# Authenticate to Twitter
auth = tweepy.OAuthHandler("xxxxxxxxxxxxxx", "xxxxxxxxxxxxxx")
auth.set_access_token("xxxxxxxxxxxxxx", "xxxxxxxxxxxxxx")
# Create API object

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

def index(request):
    return render(request,'index.html')

def search(request):
    if request.method == 'POST':
        keyword=request.POST.get("keyword")
        number=request.POST.get("number")
        usernames=[]
        texts=[]
        links=[]
        for tweet in api.search(q=keyword, lang="en", rpp=number):
            link="https://twitter.com/{}/status/{}".format(tweet.user.name,tweet.id)
            link=link.replace(" ","_");
            texts.append(tweet.text)
            links.append(link)
            usernames.append(tweet.user.name)
        context= {
            'usernames': usernames,  
            'texts': texts, 
            'links': links,
            }
    return render(request,'index.html',context)