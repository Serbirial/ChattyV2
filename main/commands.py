import string
import sys
import datetime
import ast



def check(to_check):
	text = to_check.lower()
	if text.startswith("<quit>"):
		sys.exit(0)
	elif text.startswith("<time>"):
		return f"The time is {datetime.datetime.now()}"
	elif text.startswith("<math>"):
		split = text.split("<math>")
		try:
			done = ast.literal_eval(split[1])
			return done
		except:
			return "That was not valid"
	elif text.startswith("<clean_start>"):
		return "Sorry, this feature is not done yet"
	else:
		pass