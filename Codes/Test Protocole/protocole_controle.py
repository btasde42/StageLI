#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pandas as pd
import sys
from wav_util import slice_wav, play_wav

"""
This protocole serves as a test for choosing right annotated phones.
Reference file to be used as data should be given in command line after the function call.
Ex: python3 protocole_controle.py "exemple.item"

"""

input("You will see a phone and its couple of context. Then you'll listen this part in his wv file. In any moment you can quit by typing 'Q'. Press Enter to continue..."+"\n")


input("If seen data is matching with sound type 'Y' for yes, otherwise type 'N' for no.Press Enter to continue..."+"\n")

filename=sys.argv[1] #for getting the filename 

if __name__=="__main__":
	with open(filename, "r") as f:
		with open("phones_OK.csv","w") as f_ok, open("phones_nope.csv","w") as f_nope, open("phones_non_aligned.csv","w") as f_aligned:
			next(f) #skip fist line which contains headers
			for line in f:
				datas=line.split(' ')
				wav_file=str(datas[0])+".wav" #file which contains the wav file
				onset=float(datas[1]) #onset time
				offset=float(datas[2]) #offset time
				print("phone: "+ datas[3])
				print("context: "+ datas[4] +' '+ datas[5])
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

				rep4=input("Type enter to continue or 'Q' for quitting.")
				if rep4=="Q": #if want to quit
					break

			






