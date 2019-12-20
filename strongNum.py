num=int(input("Enter a number:"))
sum=0
temp=num
while num:
	i=1
	f=1
	r=num%10
	while i<=r:
		f=f*i
		i=i+1
	sum=sum+f
	num=num//10
if sum==temp:
	print "Strong Number"
else:
	print "Not a Strong Number"
