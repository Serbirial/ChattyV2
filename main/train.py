import time
import ujson

allTrainingEntries = {"data":[]}

def save(text, text2, q = "no"):
    with open("stored/data.json", "a") as f:
		ujson.dump(allTrainigEntries, f)
		f.close()
        

#print("""
#""") i forgot what i put here lol
#time.sleep(5)

class trainingEntry:
	"""Class that is used to train chatbot. Attributes:\n
	usrInp->str, a string containing the user's input
	botInp->str, a string containing what the bot should say (is temporary to __init__)
	question->bool, is the user's input a question
	responseList->list, list of appropriate responses
	"""
	@staticmethod
	def fromDict(dicte):
		temp = trainingEntry(dicte["usrInp"], dicte["botInp"])
		temp.__dict__ = dicte
		return temp

	@staticmethod
	def fromInput():
		usrInput = input("Enter user input")
		response = input("Enter bots response")
		isQues = input("Is it a question?")
		temp = trainingEntry(usrInput, response, question=isQues)
		return temp

	def __init__(self, usrInp, botInp, question=True):
		global allTrainingEntries
		allTrainingEntries["data"].append(self.json)
		self.usrInp = usrInp
		self.responseList = []
		self.responseList.append(botInp)
		self.question = question

	@property
	def responseCount():
		return len(self.responseList)

	def __str__(self):
		formattedResponses = "<<@$>>".join(self.responseList)
		return self.usrInp + "||@$||" + formattedResponses
	
	@property
	def json(self):
		return ujson.dumps(self.__dict__)

	def __eq__(self, other):
		return str(self) == str(other)
