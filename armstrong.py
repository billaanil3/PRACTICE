num=int(input("Enter a number:"))
arm=0
temp=num
while num>0:
	rem=num%10
	arm=arm+(rem*rem*rem)
	num=num//10
print arm
if temp==arm:
	print "Armstrong Number"
else:
	print "Not an Armstrong Number"
