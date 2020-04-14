if __name__=='__main__':
	from sys import argv
	print(len(argv))
	sum=0
	for i in range(4, len(argv)):
		print(argv[i])
		sum+= float(argv[i])
	print(sum)