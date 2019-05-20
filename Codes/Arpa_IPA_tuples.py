#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import csv
def Arpa_IPA2_tuples(file,returnfile):
	"""
		Second version of IPA-arpabet transformer. 
	Args:
		file:
			a csv file contains pair of arpabet or phonetic symbols
		returnfile:
			csv file whic contains transformed pairs
	Return:
		a file
	"""

	Arpabet_dict=dict({"AA": "ɑ","AE": "æ","AH": "ʌ","AO": "ɔ","AW": "aʊ","AX": "ə","AXR": "ɚ","AY":"aɪ",
 	"EH": "ɛ","ER": "ɝ","EY": "eɪ","IH": "ɪ","IX": "ɨ","IY": "i","OW": "oʊ","OY": "ɔɪ","UH": "ʊ","UW": "u","UX": "ʉ","B": "b","CH": "tʃ",
	"D": "d","DH": "ð","DX": "ɾ","EL": "l̩","EM": "m̩","EN": "n̩","F": "f","G": "ɡ","HH": "h","JH": "dʒ","K": "k",
	"L": "l","M": "m","N": "n","NG": "ŋ","NX": "ɾ̃","P": "p","Q": "ʔ","R": "ɹ","S": "s","SH": "ʃ","T": "t",
	"TH": "θ","V": "v","W": "w","WH": "ʍ","Y": "j","Z": "z","ZH": "ʒ",})
	data=np.genfromtxt(file,delimiter=',',dtype=str)
	column1=data[:,0].tolist()
	column2=data[:,1].tolist()
	column1_API=[]
	column2_API=[]

	for symbol in column1:
		for key, value in Arpabet_dict.items():
			if symbol.lower()==key.lower():
				column1_API.append(value)
				break
			if symbol==value:
				column1_API.append(key)
	for symbol2 in column2:
		for key, value in Arpabet_dict.items():
			if symbol2.lower()==key.lower():
				column2_API.append(value)
				break
			if symbol2==value:
				column2_API.append(key)

	list_fusion=zip(column1_API,column2_API)


	with open(returnfile, 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(list_fusion)
	csvFile.close()

Arpa_IPA2('english_all_phones.csv','english_all_phones_IPA.csv')