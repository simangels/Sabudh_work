happyobj= open("C:\\Users\\Jorawar\\Desktop\\Sabudh Work\\Question's ans\\myhappynumber.txt","+w")

def squ(n):
	list=[int(x)**2 for x in str(n)]
	result=0
	for i in list:
		result = result+i
	return result


global saveno
saveno=0
for n in range(1,1000):
	a=0
	while(not (n==1 or n ==10 or n ==100 or n==1000 or n ==10000 )):
		if(a==0):
			saveno=n
		a=a+1
		print(a)
		n=squ(n)
		print(n)		
		if(a==10):
			break
		if n==1 or n ==10 or n ==100 or n==1000 or n ==10000:
			happyobj.write(str(saveno)+",")
