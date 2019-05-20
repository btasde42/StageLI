
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re
def eliminate(file,patternlist,returnfile):
	"""
	This function takes a csv file and delete all lines which contains a certain pattern.
	Args:
		file:csv file
		pattern:a regex pattern which will be used to eleminate a certain pattern
	returns:
		None
	"""
	f=open(file,"r")
	lines=f.readlines()
	rep=True
	with open(returnfile,'w') as file:
		for line in lines:
			for i in patternlist:
				p=re.compile(i) 
				if(p.search(line)):
					rep=False
			if(rep==True):
				file.write(line)
			rep=True
eliminate("1s_french.item",["a-","ɛː","ɪ","uː","θ","dʒ","əʊ","iː","kː","ʌ","h","œː"],"1s_french_cleaned.item")