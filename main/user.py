from difflib import SequenceMatcher

from collections import Counter

from . import logic

import time

count = Counter()
count["is_first_try"] = 0

class User(logic.Logic):
	def __init__(self):
		super().__init__()
		pass

	def get_response(self, text, question, ratio = 0.5, adapter = "compare", data_file="stored/data.txt"):
		"""
		Get a response to input (text)
		Ratio is the confidence level needed for the bot to return a response 1.0 - 0.1
		Question will mark it as a question and it will try to find a answer (deprecated)
		Adapter:
			Based on the adapter you choose it will highly affect the bot
			Adapters:
				Compare:
					Grabs the first response that has a high confidence
				Best Match:
					Grabs all responses that have high confidence and selects the one with the highest"""
		
		return self._get_response(text, adapter, ratio, data_file)


	def _get_response(self, text, adapter, ratio, data_file="stored/data.txt"):
		"""
		Feeds the input (text) into the bot
		Adapter:
			See 'get_response' so see about adapters"""
		start = time.monotonic()
		nothing_found = False
		response = {"response": "None", "time": "None", "confidence": "None"}
		start = time.monotonic()
		with open(data_file, "r", encoding="utf-8") as f:
			lines = []
			for line in f:
				if line != "":
					lines.append(line)
			adapter = self.adapter(adapter, text, lines, ratio)
			if adapter is not None:
				response["response"] = adapter.response
				response["confidence"] = adapter.confidence
				
			else: return -1
		if nothing_found:
			response["response"] = "I dont quite understand that"
			response["confidence"] = "0"
		end = (time.monotonic() - start) * 1000
		response["time"] = end
		return response



