#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
from bytedict import bytestring_dict
import csv

def all_phones(file,returnfile):
	"""
	This function takes a csv file and returns a list of phones from phone1, phone2 and by columns.
	Args:
		file: a csv file
	Returns:
		a list of characters
	"""
	all_phones=[]
	frame=pd.read_csv(file,sep="\t")
	#we transform these two columns to the lists
	phone1=(frame['phone_1'].tolist())
	phone2=(frame['phone_2'].tolist())
	#we separate the column which contains two phones as context
	by_sep=frame['by'].str.split(",",n=1,expand=True)
	by1=by_sep[0].tolist()
	by2=by_sep[1].tolist()
	#we assemble all four lists
	all_phones=phone1+phone2+by1+by2
	#we transform the list to dictionnary for eleminate the duplicant ones and we reconvert it to a list
	all_phones=list(dict.fromkeys(all_phones))

	for i in all_phones:
		i=bytestring_dict(i)
	
	with open(returnfile, 'w', encoding='utf-8') as f:
		for i in all_phones:
			f.write(i +"\n")
	
