#function that takes parameter as list and returns only integers
def onlyNumsList(input):
    list=[]
    for i in input:
        if(isinstance(i,int)>0):
            list.append(i)
    return list
#or using list comprehension
def onlyNumsList(input):
    newList=[i for i in input if isinstance(i,int)==True]
    return newList	
	
#list comprehend the below func:
def onlyPositives(user_input):
    only_positive=[]
    for i in user_input:
        if(isinstance(i,int)==True):
            if(i>0):
                only_positive.append(i)
    return only_positive

def onlyPositivesApprehend(user_input):
	new_List=[i for i in user_input if (isinstance(i,int)==True and i>
	)]
	return new_List
	
#list comprehend the below func:
def modifiedList(user_input):
    new_list=[]
    for i in user_input:
        if(isinstance(i,int)==True):
            new_list.append(i)
        else:
            new_list.append(0)
    return new_list

#"if else" before "for loop" in this case, as "else" is here 
def modifiedListComprehend(user_input):
	newList=[i if (isinstance(i,int)==True) else 0 for i in user_input]
	return newList
	
#list comprehend the below func:
def sumOfNumbers(user_input):
    sum=0
    for i in user_input:
        if(isinstance(i,float)==True):
            sum+=i
        elif(isinstance(i,str)==True):
            sum+=float(i)
        else:
            sum+=0
    return sum

def sumOfNumbersComprehended(user_input):
	return sum([float(i) for i in user_input])