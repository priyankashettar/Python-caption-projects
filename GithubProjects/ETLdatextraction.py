""" 
Pre-requisites:
pip install pandas
pip install tweepy (package to acess data)
pip install s3fs(store/read/write from amazon S3 bucket)
"""

import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def etl_twitterdataextraction():
    access_key= "O8DGMr5G6qYFw9Pk69WzUJ2rn"
    access_secret= "CCyMRr7bklWDgbhQwtdImhsnyppweBYNA0pnyLp2886ysP1LVc"
    consumer_key= "383281261-r2Ntz2Ck7Yvo0N3ME0z823r5NTlW8Z9ttTV5EiVW"
    consumer_secret= "86mGvNbLQU9RYnkiO1YrvsgAAY9KmEnBQUI3KdjO9ti8d"

    #Twitter authentication
    auth=tweepy.OAuthHandler(access_key,access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    #Creat the api object
    api=tweepy.API(auth)
    tweets= api.user_timeline(screen_name='@elonmusk',
                            count=200, #max allowed
                            include_rts=False, #To extract retweets keep this true
                            tweet_mode='extended'            
                            )

    tweet_list=[]
    for tweet in tweets:
        text=tweet._json["full_text"]

        filtered_tweet={
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at
        }
        tweet_list.append(filtered_tweet)

    df=pd.DataFrame(tweet_list)
    df.to_csv("user_tweets.csv")  #specify the path to be stored
    
