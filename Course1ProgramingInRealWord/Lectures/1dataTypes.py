#simple datatypes
#To find out what Python builtin functions there are: dir(__builtins__)
#all attributes/methods of str: dir(str)
#type of the atttribute received from dir: help(attribute_type)
x=10
y="sabby"
z=10.5
print(x,y,z)

mood="my mood"
strength= 100.00
rank=1
print(type(mood),mood, type(strength), strength, type(rank), rank)

#complex datatypes: datatypes made of multiple objects
#1.list
list=[1,2,3,4]
list2= range(1,10)
list3= range(10)
list4= range(1,10,2)

rainfall = [10.0,10,"rainfall",[10.0,10,"rainfall"]]

print(list,list2,list3,list4)
print(rainfall)

#exercises

#find 
#length of list, 
#index_no of element, 
#append element to list
#remove element from list
#clear the list
l=[10.0,9.6,1.8]
len(l)
l.index(10.0)
l.append(8.5)
l.remove(8.5)
l.clear()

#calculate maximum: help(max)
student_grades = [9.1, 8.8, 7.5,10]
max_values= max(student_grades)

#find of count of 10.0's in student_grades
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
dir(student_grades)
help(student_grades.count)
print(student_grades.count(10.0))

#find lower of Python3
username = "Python3"
dir(username)#to find all possible attributes with tusername object
help(username.lower)#to find the syntax of lower
username.lower

#2dictionary:

#find the average of dict values
student_grades={"anirban":9.0,"sayan":8.5,"sabya":7.0}
sum= sum(student_grades.values())
length= student_grades.__len__()
len(student_grades)
#diff betwn __len__() and len()
#__len__(): methiod of the object student_grades
#len(): function

#3.tuples:

#tuple vs list:
#tuple: t= (1,2,3) list: l= [1,2,3]
#tuple: immutable, faster list: mutable, slower

#exercises:
#create a dictionary of 3 items, values = tuple
day_temperatures ={"morning":(4.0,6.0,12.0),"noon":(1.0,3.0,5.0),"evening":(7.0,9.0,11.0)}


#summary:

Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
And a negative index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']
First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 
Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 
A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'
