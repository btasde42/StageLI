#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
import csv
import pandas as pd

def slice_csv(file,returnfile):
	"""
	This function takes a csv file and extract chosen columns to another csv file
	Args:
		file: a csv file
		returnfile: a csv file contains the extracted columns
	Return:
		a csv file 
	"""
	df=pd.read_csv(file, sep="\t")
	"""
	#Should change paramters to extract speaker columns:
	speaker_2=df['speaker_2']
	speaker_1=df['speaker_1']
	#we concatenate two speaker column and two Contrast columns to have two column in the
	#end: Speakers and Contrastes
	df['Speakers']=df['speaker_2'].map(str)+ ' ' + df['speaker_1'].map(str)
	Speakers=df['Speakers']
	"""
	df['Context']=df['by']
	df['Contrastes']=df['phone_2'].map(str)+ ' ' +df['phone_1'].map(str)
	header=["Context","Contrastes"]
	#We eject these columns to a new csv file
	df.to_csv(returnfile, sep='\t', columns=header, index=False)

slice_csv('french_1s_across_cleaned.csv','contrast_context_fr_cleaned.csv')