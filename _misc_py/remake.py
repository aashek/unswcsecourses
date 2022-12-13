import pandas as pd
import json
import os
import re

def conv_int(s):
    try:
        x = int(s)
        return x
    except:
        return 0


def jsonify(year):
    url = f"https://www.cse.unsw.edu.au/~teachadmin/alloc/courses{year}.html"
    df = pd.read_html(url)[0].fillna(0)

    lis = [list(i[1]) for i in df.iterrows()]
    tnames = lis[0]
    total_courses = lis[-1]
    res = []

    for i in lis[1:-1]:
        # format = ['code|subj',T0,T1,T2,T3,Total]
        code_subj, t0, t1, t2, t3, total = i
        code, subj = code_subj.split(" ", 1)
        
        res.append({
            "code" : code,
            "subj" : subj,
            # "t0" : conv_int(t0),
            # "t1" : conv_int(t1),
            # "t2" : conv_int(t2),
            # "t3" : conv_int(t3),
            "total" : conv_int(total)
        })

    with open(f"{year}.json", 'w') as fp:
        json.dump(res, fp, indent=1)
    # for idx, i in enumerate(df.iterrows()):
    #     if idx == 0: continue
    #     combin, num_t0, num_t1, num_t2, num_t3, total_num = list(i[1])
    #     code, subj = combin.split(' ', 1)
    #     if code == 'Total': continue
    #     cse[code] = {
    #         'course': subj,
    #         'total': int(total_num)
    #     } # terms : [{0:num_t0,1:num_t1,2:num_t2,3:num_t3}]
    # # sort dict by total decreasing
    # sortedcse = sorted(cse.items(), key = lambda x: x[1]['total'], reverse=True)
    # with open(f"{year}.json", 'w') as fp:
    #     json.dump(dict(sortedcse), fp, indent=2)



url = """https://www.cse.unsw.edu.au/~teachadmin/alloc/courses2022.html"""
df = pd.read_html(url)[0].fillna(0)

jsonify(2022)