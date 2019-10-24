
from difflib import SequenceMatcher
from collections import Counter
import sys
import datetime

from main import user # why is this not working reee
bot_class = user.User()

def redHammingMod(s1, s2):
    s1 = s1 + ' ' * (len(s2) - len(s1))
    s2 = s2 + ' ' * (len(s1) - len(s2))
    distance = sum(i == j for i, j in zip(s1, s2))
    norm_distance = distance / float(len(s1))
    return norm_distance

def bot(user_input, data_file, ratio=0.4, adapter = "get_best_match"):
    """Takes the user inpurt and gives it to the bot, also checks for any commands"""
    last_user_input = str(user_input)
    return bot_class.get_response(text=last_user_input, question=False, ratio=ratio, adapter=adapter, data_file=data_file)

if __name__ == "__main__":
    h = True
    print("""
    Commands:
        <quit>
        <time>
        <math>
        <clean_start>""")
    while True:
        while h is True:
            ad = input("what adapter do you want>")
            if ad.lower() != "compare":
                if ad.lower() != "get_best_match":
                    print("Invalid")
                else:
                    h = False
            else:
                h = False
        inp = input("\nyou>")
        response = bot(inp, ad)
        print("bot>", str(response["response"]))
        print("confidence -> ", str(response["confidence"]))
        print("time -> ", str(response["time"]))


# ratio = SequenceMatcher(None, a, b).ratio()



