infile = "/home/anil/PRACTICE/Practices/PYTHON/Programs/elastic.json"
Array = ["6J", "yB", "ss", "11"]

with open(infile, "r") as input_file:
    output_list = []
    for rec in input_file.read().splitlines():
        rec = rec[:-3]
        FBlist = [rec[i:i + 2] for i in range(0, len(rec), 2)]
        output_list.append(FBlist)
        print"------------", FBlist

FBlist_set = set(FBlist)
Array_set = set(Array)

if Array_set & FBlist_set:
    print ("Found")
    exit(0)
else:
    print ("Not Found")
exit(1)
