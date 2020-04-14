#looping over dict:
#need to mention whether iterate over items, keys or values

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for i,j in phone_numbers.items():
    print("{}: {}".format(i,j))


For loops are useful for executing a command over a large number of items.\
You can create a for loop like so:

for letter in 'abc':
    print(letter.upper())
Output:

A
B
C

You can loop over dictionary keys:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
Output:

John Smith
Marry Simpsons

You can loop over dictionary values:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
Output:

+37682929928
+423998200919

You can loop over dictionary items:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
Output: 

('John Smith', '+37682929928')

('Marry Simpons', '+423998200919')

While loops will run as long as a condition is true:

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
The loop above will print out the string inside print() over and over again until the 20th of August, 2090.