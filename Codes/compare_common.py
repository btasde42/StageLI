#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
import csv
import pandas as pd

def compare_common_elts(file1,file2,returnfile):
        """
        This function compares two csv file and returns for each contrast pairs 4 common context that matches in two files
        """
	data1=pd.read_csv(file1,delimiter='\t',usecols=["Contrasts","Context"])
	data2=pd.read_csv(file2,delimiter='\t').values
	dict_data1=pd.Series(data1.Context.values,index=data1.Contrasts).to_dict()
	list_val=[]
	dict_final={}
	for k,v in dict_data1.items():
		for i in v.split(', '):
			for j in data2:
				if i==j and i not in list_val and len(list_val)<4:
					list_val.append(i)
						
		dict_final[k]=list_val
		list_val=[]

	with open(returnfile, 'w', encoding='utf-8',) as f:
		for k,v in dict_final.items():
			alist=[k]+[str(r) for r in v]#alist=['a','1','2','3']
			line='\t'.join(alist)+"\n"#line="a  1 2 3\n"
			f.write(line)


#compare_common_elts('Min_3_contrast_context_fr.csv','all_most_common_contexts_fr.csv','common_contexts_dict_fr.csv')
