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
	return Dict_contrast_unique_context

	def same_context(file,returnfile):
		"""
		This function extracts contrast pairs with at least 3 contexts in common with their symétric contrast
		"""
		same_context={}
		dict_cont=contrast_context(file)
		same_cont=[]
		for k,v in dict_cont.items():
			for k2,v2 in dict_cont.items():
				if k[::-1]==k2:
					for i in v:
						for j in v2:
							if i==j:
								same_cont.append(i)
					if len(same_cont)>=3 and k[::-1] not in same_context: #not repetitive key consition
						same_context.setdefault(k,same_cont)
					same_cont=[]
		

	with open(returnfile,'w',newline='',encoding='utf-8') as f:
		#we rewrite those lists as two column in a new csv file
		fieldnames=['Contrasts','Quantity_Context']
		writer=csv.DictWriter(f,fieldnames=fieldnames,delimiter='\t')
		writer.writeheader()
		for i,j in zip(list_contr,list_quantite):
			writer.writerow({'Contrasts':i,'Quantity_Context':j})

contrast_context('contrast_context_fr.csv','contrast_context_quantity_fr.csv')