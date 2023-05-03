# Coronavirus twitter analysis
**Project Description**

In this project, I analyzed all geotagged tweets sent in 2020 to investigate the world's reaction to the coronavirus pandemic on social media.

The dataset contained about 1.1 billion tweets. The tweets for each day of the year were stored in a zip file, which itself contained 24 text files, one for each hour of the day. Each text file contained a single tweet per line in JSON format.
Following the MapReduce paradigm, I first used the `map.py` file to analyze the data for each day individually. 
The `map.py` file tracks the usage of various Covid-19 related hashtags by language and by country.
It then stores the results, separate files for each day for both country and language data, in the `outputs` folder. 
I then used the `run_maps.sh` shell script to run `maps.py` on each file in the dataset. 
Finally, I used the `reduce.py` file to merge all of the language files into a single file, and all of the country files into another file. 
The `visualize.py` file was used to generate bar graphs displaying some of the data.

**Tweets Containing #coronavirus**

<img src=coronalang.png width=60% />

<img src=coronacountry.png width=60% />

**Tweets Containing #코로나바이러스**

<img src=klang.png width=60% />

<img src=kcountry.png width=60% />

