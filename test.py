import pandas as pd
df = pd.read_csv("data/comment_data.csv", converters={'Comments': eval}, header=0)

total = 0
for cmnt_list in df['Comments']:
    total += len(cmnt_list)
print(total)