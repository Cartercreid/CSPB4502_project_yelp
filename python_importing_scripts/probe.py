# -*- coding: utf-8 -*-
#import simplejson as json
import os
import pandas as pd

#k = 0
#with open('business.json') as json_file:
#	data = json.load(json_file_
#	for i in data['name']:
#		print('Name: ' + i['name'])
#		if (k >=100):
#			break;
#parsed_json = (json.loads(business.json)
#print(json.dumps(parsed_json, indent=4, sort_keys=True))
"""
filn = 'tip.json'
with open(filn, 'r') as f:
	if os.stat(filn).st_size !=0:
		business_dict = json.load(f)
	else:
		bisiness_dict = {'user_id' : 0}
	
for business in business_dict:
	print(business['user_id'])
"""
def read(file_name):
    try:
	#with open(file_name, 'rb' ) as csv_file:
	#reader = csv.reader(csv_file, delimiter=',')
	#c_pd = pd.DataFrame(list(reader))	
        c_pd = pd.read_csv(file_name, iterator=True, chunksize=10000)
        #g_c_pd = pd.concat(c_pd)
        return (1,c_pd);
    except:
        print("error reading file: ", file_name)
        print("make sure the file is named and formatted correctly. Read the instructions if unclear")
        return (0,0);

def main():
	while(True):
		print("enter file name you wish to sample or q to quit")
		user_in = input("Please enter your input>")
		if (user_in == "q"):
			print("q registered")
			break;
		elif (user_in != ""):
		#	user_in = 'tip.csv'
			(check, dataf) = read(user_in)
			if (check == 1):
				print("read successful")
				#print(dataf.head(10))
				for df in dataf:
					print(df.head())
					break;
				break;
			elif (check == 0):
				print("error, try again or q to quit")
			
		


if __name__== '__main__': #run main
    main()
