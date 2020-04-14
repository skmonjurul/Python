import json
from difflib import get_close_matches
dictFile= open("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\data.json","r")
dictData= json.load(dictFile)

keysLower=[]
for i in dictData.keys():
	keysLower.append(i.lower())

def wordMeanings(user_input):
		if user_input in keysLower:
			return dictData[user_input]
		elif (len(get_close_matches(user_input,keysLower))>0):
			yn=input("did you mean %s , please ans in Y or N: " % get_close_matches(user_input,keysLower)[0])
			if yn == "Y":
				return dictData[get_close_matches(user_input,keysLower)[0]]
			elif yn == "N":
				return "sorry, does not exist"
			else:
				return "does not exist"
		else:
			return "does not exist"

user_input=input("enter the word: ")
meaning=wordMeanings(user_input.lower())
if(isinstance(meaning,list)==True):
	for i in meaning:
		print(i)
else:
	print(meaning)
