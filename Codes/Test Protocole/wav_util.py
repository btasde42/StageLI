#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np 
from scipy.io import wavfile
from pydub import AudioSegment
from pydub.playback import play

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
	
	
def play_wav(file):
	"""
	This function plays a given wav file
	Pydub package should be uploded before execution
	Args:
		file: a wav file
	"""
	sound=AudioSegment.from_wav(file)
	play(sound)