#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pandas as pd
import sys
from wav_util import slice_wav, play_wav

"""
This protocole serves as a test for choosing right annotated phones.
Reference file and index files to be used as data should be given in command line after the function call.
Ex: python3 protocole_controle.py "exemple.csv" "exeple.item"

Protocole file, wav-util file, index csv file and .item files should be in the same file with wav files.

"""

input("You will see a phone and its couple of context. Then you'll listen this part in his wv file. In any moment you can quit by typing 'Q'. Press Enter to continue..."+"\n")


input("If seen data is matching with sound type 'Y' for yes, otherwise type 'N' for no.Press Enter to continue..."+"\n")

filename1=sys.argv[1] #for getting the filename of csv index file
filename2=sys.argv[2] #target .item file
if __name__=="__main__":
	f1=[line.strip() for line in open(filename1)]
	f2=[line.strip() for line in open(filename2)]
	with open("phones_OK.csv","w") as f_ok, open("phones_nope.csv","w") as f_nope, open("phones_non_aligned.csv","w") as f_aligned:
		for line in f1[1:]:
			data1=line.split('\t')
			indTGT=data1[5]
			indOTH=data1[6]
			indX=data1[7]
			for line2 in f2[1:]:
				data2=line2.split(' ')
				if data2[0]==indTGT or data2[0]==indOTH or data2[0]==indX:
					wav_file=str(data2[1])+".wav" #file which contains the wav file
					onset=float(data2[2]) #onset time
					offset=float(data2[3]) #offset time
					print("phone: "+ data2[4])
					print("context: "+ data2[5] +' '+ data2[6])
					print(str(onset) +' ' + str(offset))
					sliced_wav=slice_wav(wav_file,onset,offset,'sliced.wav')
					play_wav('sliced.wav')
					rep=input('Is the sound mathing with the data?(Y/N)')
					if rep=="Y":
						f_ok.write(line)
					else:
						rep2=input('Is the data is definitely wrong and need to be deleted?(Y/N)')
						if rep2 == "Y":
							f_nope.write(line)
						else:
							onset=onset-float(onset/2) #refix onset time 
							offset=offset+float(1.0-offset)
							sliced_wav=slice_wav(wav_file,onset,offset,'sliced.wav')
							play_wav('sliced.wav')
							rep3=input('You want to keep data as no aligned?(Y/N)')
							if rep3 =="Y":
								f_aligned.write(line)
							else:
								f_nope.write(line)

					rep4=input("Type enter to continue or '0' for quitting.")
					if rep4=="0": #if quits
						sys.exit(0)

			






