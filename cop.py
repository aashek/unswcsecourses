import pandas as pd
import json
import os
import re

url = f"http://www.cse.unsw.edu.au/~teachadmin/alloc/alloc18x1.html"
df = pd.read_html(url)[0].fillna(0)
print(df)
cse = {}
for idx, i in enumerate(df.iterrows()):
    # 1999-2019 : [code, enr, course, person, duty, comment]
    code, enr, course, person, duty, comment = list(i[1])
    enr = int(enr) if enr != '?' else 0
    codes = "/".join(re.findall('[A-Z]{4}[0-9]{4}', code))
    cse[codes] = {'name': course, 'num': enr} # terms : [{0:num_t0,1:num_t1,2:num_t2,3:num_t3}]
# sort dict by total decreasing
print(cse)
sortedcse = sorted(cse.items(), key = lambda x: x[1]['num'], reverse=True)
