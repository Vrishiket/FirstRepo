import csv
from textblob import TextBlob

infile = 'realdonaldtrump_tweets.csv'

with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        sentence = row[2]
        blob = TextBlob(sentence)
        print (blob.polarity)
   
     csvFile = open('%s_tweets.csv' % screen_name, 'w'.csv', 'a')
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