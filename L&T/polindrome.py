num = int(input("Enter a number:"))

temp = num
res = 0
while num > 0:
    rem = num % 10
    res = (res * 10) + rem
    num = num // 10
print res
if res == temp:
    print "Polindrome"
else:
    print "Not a Polindrome"
