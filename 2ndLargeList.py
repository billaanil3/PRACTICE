n=int(input("Enter the no.of elements:"))
a=[]
#for i in range(0,n):
for i in range(1,n+1):
	elem=int(input("Enter a number:"))
	a.append(elem)
	a.sort()
print ("The second largest number is :",a[n-2])
