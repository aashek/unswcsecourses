import pandas as pd
import json
import os
import re

# 2020-2022 
# format string
# 2020 - 2022 : ['code|subj',T0,T1,T2,T3,Total]
# 1999-2019 : [code, enr, course, person, duty, comment]
# edge cases
# 99-01 has no x1
#
# updates 13/12/2022
# works for 2017-2023


def get_data(year):
	year = str(year)
	file = f'pkl/{year}.pkl'
	if not os.path.exists(file):
		url = "http://www.cse.unsw.edu.au/~teachadmin/alloc/courses"+year+".html"
		df = pd.read_html(url)[0].fillna(0)
		# create copy as pkl
		df.to_pickle(file)
	return pd.read_pickle(file)

def get_term_data(year, term):
	year = str(year)
	file = f"pkl/{year}{term}.pkl"
	if not os.path.exists(file):
		url = f"http://www.cse.unsw.edu.au/~teachadmin/alloc/alloc{year[2:]}{term}.html"
		df = pd.read_html(url)[0].fillna(0)
		# create copy as pkl
		df.to_pickle(file)
	return pd.read_pickle(file)

def create_json_year(year):
	'''
		Creates a JSON from Code and Course for years 2020- onwards.
		
		Input:
		- year : int
	'''
	df = get_data(year)

	# format = ['code|subj',T0,T1,T2,T3,Total]
	# sort table by total number of participants
	cse = {}
	for idx, i in enumerate(df.iterrows()):
		if idx == 0: continue
		combin, num_t0, num_t1, num_t2, num_t3, total_num = list(i[1])
		code, subj = combin.split(' ', 1)
		if code == 'Total': continue
		cse[code] = {'name': subj, 'total': int(total_num)} # terms : [{0:num_t0,1:num_t1,2:num_t2,3:num_t3}]
	# sort dict by total decreasing
	sortedcse = sorted(cse.items(), key = lambda x: x[1]['total'], reverse=True)
	with open(f"json/{year}.json", 'w') as fp:
		json.dump(dict(sortedcse), fp, indent=2)

def create_term_json(year, tm):
	df = get_term_data(year, tm)
	print(df.head())
	cse = {}
	for i in df.iterrows():
		# 1999-2019 : [code, enr, course, person, duty, comment]
		code, enr, course, person, duty, comment = list(i[1])
		enr = int(enr) if enr != '?' else 0
		codes = "/".join(re.findall('[A-Z]{4}[0-9]{4}', code))
		cse[codes] = {'name': course, 'num': enr} # terms : [{0:num_t0,1:num_t1,2:num_t2,3:num_t3}]
	# sort dict by total decreasing
	sortedcse = sorted(cse.items(), key = lambda x: x[1]['num'], reverse=True)
	with open(f"json/{year}{tm}.json", 'w') as fp:
		json.dump(dict(sortedcse), fp, indent=2)

def create_json(year):
	if year >= 2020:
		create_json_year(year)
	elif year == 2019:

		# for i in ['T'+str(_) for _ in range(4)]:
		# 	create_term_json(year, i)
		
		# create json from terms
		files = [f for f in os.listdir('json') if re.match(rf'{year}T', f)]
		cse = {}
		for i in files:
			# load json
			with open('json/'+i) as f:
				data = json.load(f)

			# add to total if exists
			# create name if does not exist
			for k, v in data.items():
				cse[k] = cse.get(k, {})
				cse[k]['name'] = cse[k].get('name', v['name'])
				cse[k]['total'] = cse[k].get('total', 0) + v['num']
	
		sortedcse = sorted(cse.items(), key = lambda x: x[1]['total'], reverse=True)
		with open(f"json/{year}.json", 'w') as fp:
			json.dump(dict(sortedcse), fp, indent=2)


	elif year >= 2002:
		for i in ['x1', 's1', 's2']:
			create_term_json(year, i)
		

	# elif year >= 1999:
	# 	for i in ['s1', 's2']:
	# 		create_term_json(year, i)

# website rarely gets updated, we can static call

## call by year
# create_json(2023)
# create_json(2022)
# create_json(2021)
# create_json(2020)
# create_json(2019)
# create_json(2018)
# call by term (no total)
# create_json(2015)

create_json(2016)

# for i in range(1999,2023):
	# create_json(i)