x=0
a=[]
strng = "Nara"
for i in range(len(strng)):
    if strng[i] in ['a','e','i','o','u']:
        a.append(i)
        x += 1
        if x == 2:
            break
# print a

print strng[a[0]+1:a[1]]