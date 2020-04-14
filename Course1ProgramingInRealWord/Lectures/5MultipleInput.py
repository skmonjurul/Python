#non keyword arguments
def avgFunc(*args):
    return sum(args)/len(args)
	
avgFunc(1,2,3,4,5)

#return as a list with sorted and upper converted, and then list comprehend
def sortStrings(*args):
    new_list=[]
    for i in args:
        new_list.append(i.upper())
    return sorted(new_list)

def SortStringComprehend(*args):
	newList=[i.upper() for i in args]
	return sorted(newList)
	
#pass multiple keyword arguments at a time
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=5,b=4))
ans: 9

#note:
def func(a,b): -> a,b are parameters
.
.

func(10,30)-> 10,30 are arguments
2 types of arguments:
1. non keyword arguments
2. keyword arguments