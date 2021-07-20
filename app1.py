import json
from difflib import get_close_matches

data= json.load(open("data.json"))

def define(w):
    w= w.lower() 

    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif w.upper() in data:
        return data[w.upper()]


    elif len(get_close_matches(w, data.keys())) > 0:
        yn= input("Did you mean %s instead? Enter Y if YES or N if NO: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn =="y" :
            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N" or yn =="n":
            return "The word doesn't exist. Please double check it."

        else:
            return "We didn't understand your entry."


    else:
        return "The word doesn't exist. Please double check it."



while True:
    word= input("Enter a word : ")
    if word == "/end":
        break
    else:
        output= define(word)
        if type(output) == list:
            for i in output:
                print(i)
        else:
            print(output)

