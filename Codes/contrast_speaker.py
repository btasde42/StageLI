#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
import csv
import pandas as pd

def couple_speaker(file,returnfile):
	"""
	This function takes a csv file and creates a dictionnary from chosen column information and
	extract quantity of speaker information for each contrasts and write them in a new file.
	Args:
		file: a csv file which contains only 'Contrastes' and 'Speaker' columns
		returnfile: a csv file
	Returns:
		a csv file
	"""
	sliced_file=slice_csv(file)
	Dict_contx_speaker={}

	with open(file, 'r') as file:
		reader=csv.DictReader(sliced_file,delimiter='\t')
		for row in reader:
			#create a dictionnary which have Contrastes column as key
			#and a list of speaker couples extracted from Speaker column as values
			Dict_contx_speaker.setdefault(row['Contrastes'],[]).append(row['Speakers'])

	list_cont=[]
	list_sp_unique=[]
	list_quantite=[]
	#we extract contrasts and their total number of speaker as two lists
	for k,v in Dict_contx_speaker.items():
		list_cont.append(k)
		for i in v:
			#condition for not repetitive context list
			if i not in list_sp_unique:
				list_sp_unique.append(i)
		list_quantite.append(len(list_sp_unique))
		list_sp_unique=[]

	with open(returnfile,'w',newline='',encoding='utf-8') as f:
		#we rewrite those lists as two column in a new csv file
		fieldnames=['Contraste','Quantite_Speaker']
		writer=csv.DictWriter(f,fieldnames=fieldnames,delimiter='\t')
		writer.writeheader()
		for i,j in zip(list_cont,list_quantite):
			writer.writerow({'Contraste':i,'Quantite_Speaker':j})


