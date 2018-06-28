from tweepy import *
from textblob import *
import matplotlib.pyplot as plt
import re
positive=0
negative=0
neutral=0
p_tweets=[]
n_tweets=[]
neutral_tweets=[]
consumer_key='*************************************'
consumer_secret='*************************************'
access_token='*********************************************'
access_token_secret='********************************************'
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=API(auth)
tweets=api.search("DonaldTrump")

for tweet in tweets:
    analysis=TextBlob(tweet.text)
    if(analysis.sentiment.polarity>0):
        positive=positive+1
        p_tweets.append(tweet.text)
    elif(analysis.sentiment.polarity==0):
        neutral=neutral+1
        neutral_tweets.append(tweet.text)
    else:
        negative=negative+1
        n_tweets.append(tweet.text)
        
total=positive+negative+neutral
print("Positive tweets percentage:",float(positive*100//total))
print("Postive tweets are:",p_tweets)
print("\n\n\n\n\n")
print("Negative tweeets percentage:",float(negative*100//total))
print("Negative tweets are:",n_tweets)
print("\n\n\n\n\n")
print("Neutral tweets percentage:",float(neutral*100//total))
print("Neutral tweets are:",neutral_tweets)
print(TextBlob("Hi hello i am a bad person").sentiment)

lis1=[positive,negative,neutral]
plt.plot(lis1)
plt.show()

