import string
import sys
import datetime
import ast
from main import logic

def strip_and_lower(string_input):
	"""
	Will remove punctuation from an inputted string and
	return the lowercase version of that parsed string.
	Any innuendo is unintentional.
	"""
	#table = string_input.maketrans(
	#    {symbol: None for symbol in string.punctuation}
	#    )
	#string_wo_punc = string_input.translate(table)
	return string_input.lower() # was causing problems

def temp(stuff):
	"""
	Writes to the temp file
	Stuff:
		What you want to write to the temp file"""
	with open("stored/tmp.txt", "w") as f:
		f.write(f"{stuff}")
		f.close()

def get_temp():
	"""
	Gets the temp file"""
	with open("stored/tmp.txt", "r") as f:
		for line in f:
			if line != '':
				return line
				f.close()

def log(text):
	"""
	Writes to the log file
	Text:
		What you want to log"""
	with open("stored/logs.txt", "a") as f:
		f.write(f"{text}")
		f.close()

def save_response(text):
	"""
	Saves the response and input to the data file to use later, checks to see if its already there"""
	if logic.already_exists(text) is False:
		with open("stored/data.txt", "a") as savedata:
			if text.endswith("?"):
				savedata.write(f"\n{text} | {split[1]} | yes")
			else:
				savedata.write(f"\n{text} | {split[1]} | no")
			savedata.close()

