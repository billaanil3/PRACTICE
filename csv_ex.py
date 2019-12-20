import csv

with open("file.csv", 'wb+') as myfile:
     mylist = [1,2,4]
     wr = csv.writer(myfile)
     wr.writerow(mylist)
