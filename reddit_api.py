# coding: utf-8

import pandas as pd
import praw
from datetime import datetime

r = praw.Reddit(
    client_id="wYfGaqBuNA0wA_86ETLRtw",
    client_secret="pEoqJw2uPmCRbYapZSC1dPiwPvVH6Q",
    user_agent="Omicron_life",
)

df = pd.read_csv("data/users.csv", header=None) 
new_col = []

for username in df[0]:
    subreddit_data = []
    comment_list = list(r.redditor(username).comments.new(limit=None))
    for comment in comment_list:
        ts = r.comment(id=comment.id).created_utc
        dt = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
        year = dt[:4]
        month = dt[5:7]
        day = dt[-2:]

        if int(year) == 2021:
            if int(month) == 7:
                if int(day) >= 12:
                    subreddit_data.append(r.comment(id=comment.id).body)
                else:
                    break
            elif int(month) == 8:
                if int(day) <= 12:
                    subreddit_data.append(r.comment(id=comment.id).body)
                else:
                    break
        else:
            break
    print(subreddit_data)
    new_col.append(subreddit_data)

df['new'] = new_col
df.columns = ['Username', 'Gender', 'Age', 'Depressed?', 'Comments']
df.to_csv('data/comment_data.csv', index=False)