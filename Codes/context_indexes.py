import csv
import re
import pandas as pd

def extract_final_lines(file,returnfile):
	"""
	This function creates a file in which we stock the location and timr information of choosen contrasts
	"""
	tgt=''
	oth=''
	contx=''
	speakerAB=''
	speakerX=''
	ind_tgt=''
	ind_oth=''
	ind_x=''
	speakerprob=''
	already_in=set()
	with open(returnfile, 'w', newline='') as csvfile:
		spamwriter=csv.writer(csvfile, delimiter='\t')
		lines=[line.strip() for line in open(file)]
		for l1 in lines:
			list_line1=l1.split(' ')
			list_parts1=[i.replace('\n','') for i in list_line1]
			tgt=list_parts1[4]
			contx=list_parts1[5:7]
			speakerAB=list_parts1[7]
			ind_tgt=list_parts1[0]
			for l2 in lines:
				list_line2=l2.split(' ')
				list_parts2=[i.replace('\n','') for i in list_line2]
				if (list_parts1[4],list_parts2[4]) in already_in: #for non repetitive tgt-oth phone couples
					break
				if list_parts1[4:7]==list_parts2[4:7] and speakerAB!=list_parts2[7] and list_parts1[8]==list_parts2[8]:
					speakerX=list_parts2[7]
					ind_x=list_parts2[0]
				if contx==list_parts2[5:7] and tgt!=list_parts2[4] and list_parts1[8]==list_parts2[8] and list_parts2[7]==speakerAB:
					oth=list_parts2[4]	
					ind_oth=list_parts2[0]
			if oth!='' and ind_x!='':
				spamwriter.writerow([tgt, oth, contx, speakerAB, speakerX, ind_tgt, ind_oth, ind_x])
				already_in.add((tgt,oth))
			tgt=''
			oth=''
			contx=''
			speakerAB=''
			speakerX=''
			ind_tgt=''
			ind_oth=''
			ind_x=''
			speakerprob=''



extract_final_lines('1s_english_target_contexts1.item','eng_target_context_index1.csv')