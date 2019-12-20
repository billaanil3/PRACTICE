num=int(input("Enter a number:"))
sum=0
while num>0:
	rem=num%10
	sum=sum+rem
	num=num//10
print ("The sum of Digits of a given number is:",sum) 
