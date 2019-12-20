phone_numbers = ['9480994808', '9538301391', '8970019053', '9886709190', '9164599985',
                 '9916397139', '9900236250', '9959926677', '9882729062', '8814885255',
                 '8553842283', '9620101222', '8075889847']
phone_numbers_dict = {}
for ph_num in phone_numbers:
    for num in ph_num:
        if num in phone_numbers_dict.keys():
            phone_numbers_dict[num] = phone_numbers_dict[num] + 1
        else:
            phone_numbers_dict[num] = 1
print phone_numbers_dict

# xx = {k: d1[k] for k, v in d1 for num in ph_num for ph_num in phone_numbers d1[num]=num if num not in d1.keys()}

map(lambda x:x if '9' in phone_numbers)