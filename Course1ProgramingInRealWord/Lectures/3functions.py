# a prog that takes user inputs and makes a complete sentence
def SentenceMaker(input):
	keyWords=("how","where","when")
	if(input.lower().startswith(keyWords)):
		return "{}?".format(input.capitalize())
	else:
		return "{}.".format(input.capitalize())

list=[]
while True:
	user_inp= input("enter the sentence")
	if(user_inp=="\end"):
		break
	else:
		list.append(SentenceMaker(user_inp))

final_str=" ".join(list)
	
print(final_str)