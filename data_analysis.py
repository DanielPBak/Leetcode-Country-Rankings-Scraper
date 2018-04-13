import pandas
import sys
query_username = sys.argv[1]

df = pandas.read_csv("DUMMY.csv")

nat_rank = df.groupby(['nationality'])['rank'].rank(method='dense').astype(int)

new_df = df.join(nat_rank, how='inner', lsuffix='_orgin', rsuffix='_rank')
print()
user_row = new_df.loc[new_df['username'] == 'uwi']
print(user_row)
#print(user_row)