#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np 
from scipy.io import wavfile 

def slice_wav(file,begin,end,newfilename):
	"""
	This function slice an array into two values given as begin and end
	Args:
		WavArray: an array obteined by a wav file
		begin: beginnig point for slicing(seconds)
		end:end point for slicing(seconds)
		newfilename:le nom di fichier du retour
	Returns:
		A new wav file which contains extracted part

	"""
	freq, data=wavfile.read(file)
	new_sliced_array=data[(int(begin*freq)):(int(end*freq))]
	wavfile.write(newfilename,freq,new_sliced_array)


#Les tests

if __name__ == "__main__":
	slice_wav('1.wav',0.0,0.5,'1sliced.wav')