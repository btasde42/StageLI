#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pandas as pd

def get_lists(file):
	"""
	This function extracts context parts from Context row
	"""
	list_line=[]
	list_contx=[]
	dict_contx={}
	df=pd.read_csv(file,delimiter='\t',names=['Contrasts','Context'],skiprows=1)
	for i in df.Context:
		list_line.append(i.split(', '))
		list_contx+=list_line
		list_line=[]
	
	return list_contx


def most_common(listt,returnfile):
        """
        This function extracts a most common contrast list for all of the contrast pairs and
        writes it to an csv file
        """
	dict_final={}
	final=set()
	for i in listt:
		if(len(i)==3):
			for j in i:
				final.add(j)
	count=0

	for m in listt:
		while count<3:
			for n in m:
				if n in final: #if already in set, count+1
					count+=1 #elts in set before addition of news
				else:
					final.add(n)
					count+=1
		count=0
	print(final)

	file=open(returnfile,'w',encoding='utf-8')
	for i in final:
		file.write(i+'\n')


#listt=get_lists('Min_3_contrast_context_eng.csv')

#most_common(listt,'common_contexts_eng.csv')
