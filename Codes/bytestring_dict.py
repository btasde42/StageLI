#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This file contains an bytestring to utf-8 dictionnary"""

def bytestring_dict(symbol):
	"""
	This function takes a bytestring symbol and return its utf-8 value
	Args:
		symbol: an bytestring symbol
	Returns:
		a char representing utf-8 value
	"""
	Dict_byte={'\xc9\x9b':'ɛ','\xc9\x99':'ə','\xc9\x94\xcc\x83':'ɔ̃','\xc9\xb2':'ɲ','\xc3\xb8':'ø','\xca\x83':'ʃ','\xca\x81':'ʁ','\xc9\x91\xcc\x83':'ɑ̃','\xca\x92':'ʒ','\xc5\x93\xcc\x83':'œ̃','\xc9\x94':'ɔ','\xc5\x93':'œ','\xc9\xa1':'g','\xc9\x9b\xcc\x83':'ɛ̃','\xcb\x90':'ː'}
	
	for key,value in Dict_byte:
		if symbol == key:
			return value
		else:
			return symbol
