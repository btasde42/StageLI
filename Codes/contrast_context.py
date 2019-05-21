#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
import csv
import pandas as pd

def contrast_context(file,returnfile):
	"""
	This function takes a csvfile which contains only two specific column to be compared and counted
	Use slice_csv funtion to extract those parts!
	"""

	Dict_contrast_context={}
	with open(file, 'r',encoding='utf-8') as file:
		reader=csv.DictReader(file,delimiter='\t')
		for row in reader:
			#create a dictionnary which have Contrastes column as key
			#and a list of speaker couples extracted from Speaker column as values
			Dict_contrast_context.setdefault(row['Contrastes'],[]).append(row['Context'])

	list_contr=[]
	list_ctx_unique=[]
	list_quantite=[]
	#we extract contrasts and their total number of speaker as two lists
	for k,v in Dict_contrast_context.items():
		list_contr.append(k)
		for i in v:
			#condition for not repetitive context list
			if i not in list_ctx_unique:
				list_ctx_unique.append(i)
		list_quantite.append(len(list_ctx_unique))
		list_ctx_unique=[]


	with open(returnfile,'w',newline='',encoding='utf-8') as f:
		#we rewrite those lists as two column in a new csv file
		fieldnames=['Contrasts','Quantity_Context']
		writer=csv.DictWriter(f,fieldnames=fieldnames,delimiter='\t')
		writer.writeheader()
		for i,j in zip(list_contr,list_quantite):
			writer.writerow({'Contrasts':i,'Quantity_Context':j})

contrast_context('contrast_context_fr.csv','contrast_context_quantity_fr.csv')