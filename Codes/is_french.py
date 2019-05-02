#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def is_french(file,returnfile):
	list_french_phones=['i','e','ɛ','a','y','ø','œ','u','o','ɔ','ɑ','ə','ɛ̃','ɔ̃','œ̃','õ','ɑ̃','ɥ','w','j','ʃ','ʒ','m','n','ɲ','ŋ','p','b','t','d','k','g','f','v','l','s','z','ʁ']
	frame=pd.read_csv(file)
	phone_list_file=(frame['Phones'].tolist())

	list_foreign=[]

	for i in phone_list_file:
		if i not in list_french_phones:
			list_foreign.append(i)
	with open(returnfile,'w',encoding='utf-8') as f:
		for i in list_foreign:
			f.write(i +"\n")

is_french('french_all_phones.csv','non_french_phones.csv')