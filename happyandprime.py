happyobj= open("C:\\Users\\Jorawar\\Desktop\\Sabudh Work\\Question's ans\\myhappynumber.txt","+r")
s_happynumber=happyobj.read()
happylist=s_happynumber.split(",")
print(happylist)
happyobj.close()

primeobj = open("C:\\Users\\Jorawar\\Desktop\\Sabudh Work\\Question's ans\\myprimenumber.txt","+r")
s_primenumber=primeobj.read()
primelist=s_primenumber.split(",")
print((happylist))
primeobj.close()

noinboth=set([])
for y in range(0 , len(happylist)-1):
	for x in range(0 ,len(primelist)-1):
		if( happylist[y] == primelist[x]):
			print("The number in both list is:- " ,happylist[y])
			noinboth.add(happylist[y])

print("enter in both file",noinboth)


