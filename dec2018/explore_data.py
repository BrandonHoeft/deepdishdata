#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:36:19 2018

@author: bhoeft
"""


import pandas as pd
import re
import os

cta_tweets = pd.read_feather('/Users/bhoeft/Desktop/deepdishdata/sept2018/cta_tweets_sample.feather')
cta_tweets['text'] = cta_tweets.text.str.lower()

print(cta_tweets.head())
cta_tweets.info()


def find_train_delays(x):
    """identifies if the tweet concerned a train,
    which was delayed|standing due to some problem,
    and 'crews are working to restore service'. These 
    are the typical original train delay tweets."""
    
    pattern = re.compile('(blue|brown|green|orange|purple|pink|red|yellow).*train.*(delay|standing|problem).*crews.*working')
    match = re.search(pattern, x) # match objects are bool=True
    
    if match:
        # return tuple of bool and the name of the train line that was delayed.
        return True, match.group(1)
    else:
        return False, None


print(cta_tweets.text[532])
temp2 = cta_tweets.text[532]

pattern = re.compile('(blue|brown|green|orange|purple|pink|red|yellow).*train.*(delay|standing|problem).*crews.*working')
match = find_train_delays(temp2)
print(match)

type(match)


# apply find_train_delays to tweet text, assign results to 2 new cols
copy_df = cta_tweets.copy(deep=True)

copy_df[['train_delay', 'train']] = (copy_df.text
       .apply(find_train_delays) # returns vector of tuple pairs
       .apply(pd.Series)) # each tuple to Series, which becomes row in a df.  

copy_df = copy_df.drop(['retweet_count', 'favorite_count'], axis=1)

copy_df.info()


# Filter tweets dataframe to original train delay tweets for specific trains
train_delay_df = copy_df[copy_df['train_delay'] == True]
not_delay_df = copy_df[copy_df['train_delay'] == False]
