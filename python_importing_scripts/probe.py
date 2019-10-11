# -*- coding: utf-8 -*-
#import simplejson as json
import os
import pandas as pd
"""read returns a tuple, first value is a bool, 1 for success, 0 for failure, and the second value is a list of large dataframes. It can take a while to run."""
def read(file_name):
    try:
		#need to iterate through, because some of the csv files are too large and kill the program (Error: killed)
        c_pd = pd.read_csv(file_name, iterator=True, chunksize=10000)
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
				#dataf is not a dataframe, but a nonindexable list of dataframes. This just prints the head of the first one so we can see column names/attributes
				for df in dataf:
					print(df.head())
					break; #break from the for loop as we only need the first head
				#break;
			elif (check == 0):
				print("error, try again or q to quit")
			
		


if __name__== '__main__': #run main
    main()
