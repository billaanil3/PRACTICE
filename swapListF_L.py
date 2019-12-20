a=[]
n=int(input("Enter the no.of elements in a list:"))
for i in range(0,n):
	elem=int(input("Enter element " + str(i+1) +":"))
	a.append(elem)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print ("The new list is :",a)

