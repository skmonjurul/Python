#read a file and print 1st characters
file=open("bear.txt")
content=file.read()
print(content[:20])

#read the no of occurances of a particular char:
def occurancesOfChar(character, filePath):
    file=open(filePath)
    fileStr=file.read()
    count=0
    for i in fileStr:
        if(i==character):
            count+=1
    return count
#or
def foo(character, filepath="bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)
	
#write to a file:
with open("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\file2.txt","w") as myFile:
    myFile.write("hi sabyasachi")

myFile=open("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\file2.txt","w")
contentStr=myFile.write("hi sabyasachi")
myFile.close()

#read the first 90 chars from a file and write to a new file:
file= open("bear.txt","r")
firstContent= file.read()
first90=firstContent[0:90]
newFile=open("first.txt","w")
newFile.write(first90)
newFile.close()
#or
with open("bear.txt") as file:
    content = file.read()

with open("first.txt", "w") as file:
    file.write(content[:90])
	
	
with open("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\file1.txt","r") as bear1File:
    print(bear1File.read())
	
textFile1= open("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\file1.txt","a+")
text1Content= textFile1.read()
print(text1Content)
textFile2=open("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\file2.txt","a+")
textFile2.write("\ntext1Content")
textFile2.seek(0)
print(textFile2.read())
textFile2.close()

#copy the file n times:
datafile=open("data.txt","r")
datafileCont=datafile.read()
newDataFile=open("data.txt","a")
for i in range(2):
    newDataFile.write(datafileCont)
newDataFile.close()