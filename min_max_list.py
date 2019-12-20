list = [7, 5, 7, 2, 8, -2, 25, 25]
temp = []
for i in range(len(list)):
    if min(list) != max(list):
        temp.append(max(list))
        list.remove(max(list))
        temp.append(min(list))
        list.remove(min(list))
    else:
        if max(list) not in temp:
            temp.append(max(list))
print temp
