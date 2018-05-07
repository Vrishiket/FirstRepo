import tweepy
import csv
import pandas as pd
from textblob import TextBlob
####input your credentials here
consumer_key = '12UCbopLPIyQ3S32G0bf6kNYX'
consumer_secret = '54KRYBa0gOUNxA0Ex1YWQqdTkyEL067MY7ed8ZC3j7kCELBLbt'
access_token = '4901534286-V4aGGswcis4xgK4VGZ5ns5lyjTJZtdDmmWRJ540'
access_token_secret = 'qR1QroqxEQW5kQTUaYNcZtPKDgkL3iYJdwudBgEsZishR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('uuuu.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#telco",count=100,
                           lang="en",
                           since="2018-04-05").items():
    
    analysis= TextBlob(tweet.text)
    sent=""
    if analysis.polarity>0 :
        sent="Positive"
    elif analysis.polarity==0:
        sent=("nuetral")
    else:
        sent=("negative")
    print (tweet.created_at, tweet.text,analysis.polarity)

    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),analysis.polarity,sent])
    
    