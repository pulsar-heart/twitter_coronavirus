#!/usr/bin/env python3

# command line args
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
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
import matplotlib.font_manager as fm

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)
# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]
df = pd.DataFrame(dict(categories = list(counts[args.key].keys()), tweets = list(counts[args.key].values())))
df_sorted = df.sort_values('tweets', ascending=True)
df_sorted = df_sorted.iloc[-10:]
categories = list(df_sorted['categories'])
tweets = list(df_sorted['tweets'])
fig, ax = plt.subplots()
plt.bar(range(len(categories)), tweets, color='maroon')
plt.xticks(range(len(categories)), categories)
plt.xlabel("Countries")
plt.title('')
plt.ylabel("Tweets")
ax.set_axisbelow(True)
ax.grid(axis='y', color='gray', linestyle='dashed')
plt.savefig('coronacountry.png')
plt.show()
