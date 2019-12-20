import csv
new_cond = 'Uploaded By'
count = 0
with open("imp_conds_exist_contr.csv", "r") as f_input:
    csv_input = csv.reader(f_input)
    for row in csv_input:
	#print row[0]
	imp_conds = row[1]
	if new_cond in imp_conds:
	   pass
	    



