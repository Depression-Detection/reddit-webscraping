import pandas as pd
import praw

r = praw.Reddit(
    client_id="wYfGaqBuNA0wA_86ETLRtw",
    client_secret="pEoqJw2uPmCRbYapZSC1dPiwPvVH6Q",
    user_agent="Omicron_life",
)
cmts = list(r.redditor('Chaos_moon0').comments.new(limit=None))
print(cmts)


# df = pd.read_csv("users.csv", header=None) 

# subreddit_data = []
# for username in df[0]:
#     cmts = list(r.redditor('Chaos_moon0').comments.new(limit=None))
#     print(cmts)
#     print("First one in list body:")
#     print(r.comment(id='h8f7snk').body)