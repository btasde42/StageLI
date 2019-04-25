#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Arpa_IPA():
 	"""
 	This function takes a phon which contains Arpabet or IPA encoding and transforms it to versus 
 	Args:
 		None.
 	Return:
 		a string with IPA or arpabet encoding
 	"""

 	print("Please type an arpabet symbol or an IPA symbol.")
 	symbol=str(input())
 	# we ask to the utilisator to give a symbol to transform

 	Arpabet_dict=dict({"AA": "ɑ","AE": "æ","AH": "ʌ","AO": "ɔ","AW": "aʊ","AX": "ə","AXR": "ɚ","AY":"aɪ",
 	"EH": "ɛ","ER": "ɝ","EY": "eɪ","IH": "ɪ","IX": "ɨ","IY": "i","OW": "oʊ","OY": "ɔɪ","UH": "ʊ","UW": "u","UX": "ʉ","B": "b","CH": "tʃ",
	"D": "d","DH": "ð","DX": "ɾ","EL": "l̩","EM": "m̩","EN": "n̩","F": "f","G": "ɡ","HH": "h","JH": "dʒ","K": "k",
	"L": "l","M": "m","N": "n","NG": "ŋ","NX": "ɾ̃","P": "p","Q": "ʔ","R": "ɹ","S": "s","SH": "ʃ","T": "t",
	"TH": "θ","V": "v","W": "w","WH": "ʍ","Y": "j","Z": "z","ZH": "ʒ",})
 	for key, value in Arpabet_dict.items():
 		if symbol==key:
 			return value
 		if symbol==value:
 			return key
#Les tests
if __name__ == "__main__":
	print(Arpa_IPA())
	