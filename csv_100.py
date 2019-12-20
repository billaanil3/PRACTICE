import csv
cond = 'Sylvia Foulston'
count = 0
with open("SampleCSVFile.csv", "r") as f_input:
#with open("imp_conds_exist_contr.csv", "r") as f_input:
    csv_input = csv.reader(f_input)
    print csv_input.next()
    print csv_input.next()
    for row in csv_input:
	list1 = row[0]
	list2 = row[1]
	list3 = row[2]
	list4 = row[3]
	list5 = row[4]
	list6 = row[5]
	list7 = row[6]
	list8 = row[7]
	list9 = row[8]
	list10 = row[9]
	print list1,list2
#print count
	



