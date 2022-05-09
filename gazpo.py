import pandas as pd
import requests


r = requests.get('http://www.cse.unsw.edu.au/~teachadmin/alloc/alloc17x1.html')
print(r.text)
df = pd.read_html('17x1.html')
df = df[0].fillna(0)

for i in df.iterrows():
    print(i)
# df_list = pd.read_html('17x1.html') # this parses all the tables in webpages to a list
# df = df_list[0].fillna(0)
# print(df.head())

# for i in df.iterrows():
#     print(i)