import json

data = json.load(open("data.json"))

def translate(str):
    return data[str]  

word = input("Enter word:")

print(translate(word))