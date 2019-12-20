files = {'input.txt':'Anil',
         'code.py':'Reddy',
         'output.txt':'Anil'}
list1 = []
dict = {}
for key,value in files.iteritems():
    if value == "Anil":
        list1.append(key)
        dict[value] = list1

for i,j in files.items():
    if j in files.values() and j not in dict.keys():
        dict[j]=i

print dict
    