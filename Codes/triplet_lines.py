#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re

def prepare_triplet_dict(file):
	dict_contx={}
	with open(file,"r") as f:
		next(f)
		for line in f:
			line_list=line.split("\t")
			line_list_cleaned=[i.replace('\n','') for i in line_list]
			dict_contx[line_list[0]]=[] 
			for j in range(len(line_list_cleaned)):
				if j==0:
					continue
				list_contx=[(line_list_cleaned[j].split(',')[0],line_list_cleaned[0].split(',')[0],line_list_cleaned[j].split(',')[1]),(line_list_cleaned[j].split(',')[0],line_list_cleaned[0].split(',')[1],line_list_cleaned[j].split(',')[1])]
				dict_contx[line_list_cleaned[0]].append(list_contx)

	return dict_contx

def extract_common_lines(file,dictt,returnfile):
	lines_to_keep=set()
	indice=''
	with open(file,"r") as f1:
		for lines in f1:
			list_parts=lines.split(' ')
			for k,v in dictt.items():
				indice=k
				for i in v:
					for j in i:
						if j[0]==list_parts[4] and j[1]==list_parts[3] and j[2]==list_parts[5]:
							lines_to_keep.add((lines.replace('\n',''),indice))
				
							


	with open(returnfile,'w',encoding='utf-8') as f:
		for i in lines_to_keep:
			f.write(i[0]+'\t'+i[1])
			f.write('\n')


extract_common_lines('1s_english_cleaned-second.item',prepare_triplet_dict('3_contexts_each_fr1.csv'),'1s_french_target_contexts1.csv')
