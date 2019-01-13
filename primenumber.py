size =int(input("Enter the range upto which you want to find prime number"))
primeobj = open("C:\\Users\\Jorawar\\Desktop\\Sabudh Work\\Question's ans\\myprimenumber.txt","+w")
for i in range (1, size):
	num = i
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				print(num,"is not a prime number")
				break
		else:
		   print(num,"is a prime number")
		   primeobj.write(str(num)+",")
	else:
		   print(num,"is not a prime number")
