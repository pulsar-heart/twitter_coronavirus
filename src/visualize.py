#!/usr/bin/env python3

# command line args
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import pandas as pd
import seaborn as sns
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
#items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#for k,v in items:
#    print(k,':',v)
df = pd.DataFrame(dict(languages = list(counts[args.key].keys()), tweets = list(counts[args.key].values())))
df_sorted = df.sort_values('tweets', ascending=False)
df_sorted = df_sorted.iloc[:10]
print(df_sorted)
#top_ten_keys = list(itemsdict.keys())[:10]
#top_ten_counts = [itemsdict[k] for k in top_ten_keys]
fig = plt.figure(figsize = (10, 5))
#plt.bar(top_ten_keys, top_ten_counts, color ='maroon', width = 0.4)
sns.barplot(x='languages', y='tweets', data=df_sorted)
plt.title("Languages with Most #coronavirus Tweets in 2020")
#plt.xlabel("Languages")
#plt.ylabel("Tweets")
plt.savefig('plot.png')
plt.show()
