'''
str = input("Enter Main String:")
sub = input("Enter sub string:")

flag = False
pos = -1
n = len(str)

while True:
   pos = str.find(sub,pos+1,n)
   if pos == -1:
      break
   print "Found at position :",pos+1
if flag == False:
   print "Not Found"   '''

"*******************************************************************************************"

