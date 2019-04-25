#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import csv


def extract_pairs(csvfile,returnfile):
	"""
	This function reads a cvs file and extract phone1, phone2 information.
	Args:
		file: a cvs file which contains phone pairs and their contexts.
		returnfile: a cvs file which will be created in the end of the proccess for saving phone pairs.
	Returns:
		None
	"""

	frame=pd.read_csv(csvfile,sep="\t")
	#we transform these two columns to the lists
	phone1=(frame['phone_1'].tolist())

	phone2=(frame['phone_2'].tolist())
	#we zip these two lists to create one with duplicant pairs
	list_phones= (zip(phone1,phone2))
	#creating set of tuples for each phone pair
	s=set()
	for pair in list_phones:
		pair=tuple(pair)
		#we eleminate the duplicant and reverse duplicant pairs
		if pair not in s and pair[::-1] not in s:
			s.add(pair)


	#we open a file in given name at arguments and write our list of pairs in that csv file
	with open(returnfile, 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(s)

	csvFile.close()
	
