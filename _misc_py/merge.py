

# merge 2019-2022 so far into one json
import json, os, re

files = [f for f in os.listdir('data') if re.match(r'\d{4}.json', f)]

print(files)
cse = {}
for i in files:
    # load json
    with open('data/'+i) as f:
        data = json.load(f)

    # add to total if exists
    # create name if does not exist
    for k, v in data.items():
        cse[k] = cse.get(k, {})
        cse[k]['name'] = cse[k].get('name', v['name'])
        cse[k]['total'] = cse[k].get('total', 0) + v['total']

sortedcse = sorted(cse.items(), key = lambda x: x[1]['total'], reverse=True)



# normalise dict

# new_dic = {}
# ind_code = []
# i = 0
# for key, value in dict(sortedcse).items():   # iter on both keys and values
    
#     if key[:8] in seen:
#         new_dic[
#     else:
#         new_dic[key] = value
#         ind_code.append((key[:8], i))
#     i += 1


with open(f"data/complete.json", 'w') as fp:
    json.dump(dict(sortedcse), fp, indent=2)
