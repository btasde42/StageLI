#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def is_english(file,returnfile):
	english_phones=["aa","ɑ","ae","æ","ah","ʌ","ao","ɔ","aw","aʊ","ax","ə","axr","ɚ","ay","aɪ","eh","ɛ","er","ɝ","ey","eɪ","ih","ɪ","ix","ɨ","iy","i","ow","oʊ","oy","ɔɪ","uh","ʊ","uw","u","ux","ʉ","b","ch","tʃ","d","dh","ð","dx","ɾ","el","l̩","em","m̩","en","n̩","f","ɡ","hh","h","jh","dʒ","k","l","m","n","ng","ŋ","nx","ɾ̃","p","q","ʔ","r","ɹ","s","sh","ʃ","t","th","θ","v","w","wh","ʍ","y","j","z","zh","ʒ"]
	frame=pd.read_csv(file)
	phone_list_file=(frame['Phones'].tolist())
	list_foreign=[]

	for i in phone_list_file:
		if i not in english_phones:
			list_foreign.append(i)
	with open(returnfile,'w',encoding='utf-8') as f:
		for i in list_foreign:
			f.write(i +"\n")

is_english('english_all_phones.csv','non_english_phones.csv')