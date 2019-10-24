import string
from difflib import SequenceMatcher
from string import ascii_letters, punctuation, whitespace
import ujson

class Response(object):
    def __init__(self, **kwargs):
        self.response = kwargs.get('response')
        self.confidence = kwargs.get('confidence')


class Logic:
    def __init__(self):
        pass
    def already_exists(self, to_check):
        """
        Checks the file to see if the text or response and input combo is already there
        To check:
            The text to check for in the file"""
        try:
            with ujson.load(open("stored/data.json", "r")) as f:
                for text in f["data"]:
                    if to_check in text or type(text)==str and to_check == text:
                        return True
                return False # if it gets here, it didnt find anything
        except:
            return True

    def compare(self, user_input, text_to_search, ratio = 0.6):
        """Compare {user_input} to {text_to_search}
        Ratio is the confidence needed to pass and give True
        Picks the first response"""
        responses = []
        for line in text_to_search:
            split = line.split(" | ")
            responses.append(split[0] + ' | ' + split[1])
        for word in responses:
            split = word.split(" | ")
            if str(SequenceMatcher(None, user_input, split[0]).ratio()) > f'{ratio}':
                
                return split[1]

    def compare_old(self, user_input, text_to_search, ratio = 0.6):
        if str(SequenceMatcher(None, user_input, text_to_search).ratio()) > f'{ratio}':
            return True
        else:
            return False

    def get_best_match_old(self, user_input, text_to_search, ratio = 0.6):
        """
        Gets the best match out of multiple responses
        User input:
            The users input, this should be a string
        Text to search:
            The text to search, this should be a list
        Ratio:
            The ratio that confidence should be near to continue"""
        responses = []
        response = {"output": "None", "confidence": "None"}
        for word in text_to_search:
            if str(SequenceMatcher(None, word.split(" | ")[0], user_input).ratio()) > str(ratio):
                responses.append(word) # add each response to a list if it matches the conf ratio

        last_res = []
        didnt_find = True
        for res in responses:
            split = res.split(" | ")
            conf = compare_old(user_input, split[0], ratio + 0.3)
            if conf is True:
                if conf != "":
                    
                    response["output"] = split[1] # returns the one that matches the given ratio + 0.3
                    didnt_find = False
        if didnt_find is True:
            for res in responses:
                split = res.split(" | ")
                conf = compare_old(user_input, split[0], ratio + 0.2)
                if conf is True:
                    if conf != "":
                        
                        response["output"] = split[1] # returns the one that matches the given ratio + 0.2
                        didnt_find = False
        if didnt_find is True:
            return None 
            
            #return "Sorry, i dont understand that"
        response["confidence"] = str(SequenceMatcher(None, split[0], user_input).ratio())
        return response

    def get_best_match(self, user_input, text_to_search, ratio = 0.6):
        last_highest = None
        for line in text_to_search:
            check = SequenceMatcher(None, line.split(" | ")[0], user_input).ratio()
            if str(check) > str(ratio):
                if last_highest is None:
                    last_highest = Response(confidence=check, response=line.split(" | ")[1])
                else:
                    if check > last_highest.confidence:
                        last_highest = Response(confidence=check, response=line.split(" | ")[1])
        return last_highest


    def adapter(self, adapter_chosen, user_input, line, ratio = 0.5):
        """
        Finds the adapter and then uses it with the given input, line and ratio
        Adapters:
            Compare:
                Grabs the first response that has a high confidence. deprecated
            Best Match:
                Grabs all responses that have high confidence and selects the one with the highest"""
        adapters = ['compare', 'get_best_match', 'test']
        adapters_func = {'compare': self.compare, 'get_best_match': self.get_best_match, 'get_best_match_old': self.get_best_match_old}
        for option in adapters:
            if option == adapter_chosen:
                return adapters_func[adapter_chosen](user_input, line, ratio)