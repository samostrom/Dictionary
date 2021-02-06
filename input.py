import json
import difflib

data = json.load(open("data.json"))

def translate(str):
    if str in data:
        return data[str] 
    else:
        return "Word is not in the dictionary" 

word = input("Enter word:").lower()

print(translate(word))

test