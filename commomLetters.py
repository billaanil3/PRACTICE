str1=raw_input("Enter a string1:")
str2=raw_input("Enter a string2:")
a=list(set(str1) & set(str2))
print "The common letters are:"
for i in a:
	print i
