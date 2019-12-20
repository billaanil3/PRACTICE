n=int(input("Enter the no.of elements to be inserted:"))
a=[]
for i in range(0,n):
	elem=int(input("Enter the elements:"))
	a.append(elem)
	avg=sum(a)/n
print ("Average of elements of the list:",avg)

