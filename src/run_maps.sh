#!/bin/sh
#loop over each file in the dataset and run the map.py command on that file/ Each call to map.py can take up to a day to finish, so you should use the nohup command to ensure the program continues to run after you disconnect and the & operator to ensure that all map.py commands run in parallel.
#HINT: Use the glob * to select only the tweets from 2020 and not all tweets
for file in '/data/Twitter dataset/'geoTwitter20*.zip; do
    ./src/map.py --input_path="$file" &
done
#comment
