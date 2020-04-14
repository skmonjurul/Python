#read csv
import pandas
df1= pandas.read_csv("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\supermarkets.csv")

#read json
df2= pandas.read_json("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\supermarkets.json")

#read excel
#pip3 install xlrd
from pandas import read_excel
df3= read_excel("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\supermarkets.xlsx",sheet_name=0)

#read text
#default textfile with comma
df4=pandas.read_csv("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\supermarkets-commas.txt")

#textfile with other delimiters
df5=read_csv("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\supermarkets-semi-colons.txt",sep=";")

#read data without header and name header
df6=read_csv("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\file2.txt",header=None)
df6.columns=["description"]

#name index:
#note: index should be among columns
df6.set_index("description",inplace=True, drop=False)




# access parts of dataframe:
df1=read_csv("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\supermarkets-semi-colons.txt",sep=";",index_col="ID")

	Address	City	State	Country	Name	Employees
ID						
1	3666 21st St	San Francisco	CA 94114	USA	Madeira	8
2	735 Dolores St	San Francisco	CA 94119	USA	Bready Shop	15
3	332 Hill St	San Francisco	California 94114	USA	Super River	25
4	3995 23rd St	San Francisco	CA 94114	USA	Ben's Shop	10
5	1056 Sanchez St	San Francisco	California	USA	Sanchez	12
6	551 Alvarado St	San Francisco	CA 94114	USA	Richvalley	20

#1.label based indexing
df1.loc["3":"5","State":"Name"]

#2.position based indeing
df1.iloc[2:5,2:5]


#deleting parts of dataframe:
#label based:
df1.drop(2,0)

#index based:
df1.drop(df1.index[0:3],0) -> for rows
df1.drop(df1.columns[0:3],1) -> for columns

df1.columns
df1.index

#adding rows and columns to dataframes:
#1.adding column:
df1["new_column"]=df1.shape[0]*["sabby"]
or
df1["new_column"]="sabby"
or
df1["full_address"]=df1["State"]+", "+df1["Country"] -> with existing columns' values

#2.adding rows:
#transpose, then make new column and add data, then transpose= 1 row added
df1_t=df1.T
df1_t["7"]=["my street","my city","my State","my Country","my Name","my Employees","my full_address"]
df1=df1_t.T