# def company_UIN_generate(c_name):
#     skip_values = ['Pvt', 'Ltd', 'Sons', 'In', 'Of']
#     # c_name = "One Delta Technologies Solutions Pvt Ltd"
#     words = c_name.split(" ")
#     valid_list = []
#     print words
#     for word in words:
#         if word not in skip_values:
#             valid_list.append(word)
#     com_abbrv = ''
#     for abbrv in valid_list:
#         com_abbrv = abbrv

    # return dict(comp_name=valid_list, comp_abbrv=com_abbrv)


# def company_UIN_generate(c_name):
#     skip_values = ['Pvt', 'Ltd', 'Sons', 'In', 'Of']
#     c_name = "One Delta Technologies Solutions Pvt Ltd"
#     c_name = c_name.split(" ")
#     c_name = c_name[0:3]
#     print c_name
#     name1 = c_name[0]
#     name2 = c_name[1]
#     name3 = c_name[2]
#     # for i in range(len(name3)):
#     com_abbrv = name1[0] + name2[0] + name3[0]
#     all_comp_abbrv = db(db.company.abbreviation == com_abbrv).select().first()
#     print com_abbrv
#     print all_comp_abbrv

def company_UIN_generate(c_name):
    skip_values = ['Pvt', 'Ltd', 'Sons', 'In', 'Of']
    vowels = ['a', 'e', 'i', 'o', 'u']
    c_name = "One Delta Technologies Solutions Pvt Ltd"
    c_name = c_name.split(" ")
    c_name = c_name[0:3]
    print c_name
    name1 = c_name[0]
    name2 = c_name[1]
    name3 = c_name[2]
    # for i in range(len(name3)):
    com_abbrv = name1[0] + name2[0] + name3[0]
    all_comp_abbrv = ['ODT', 'ODG']
    # all_comp_abbrv = db(db.company.abbreviation == com_abbrv).select().first()
    print com_abbrv.split()
    # print all_comp_abbrv
    if com_abbrv in all_comp_abbrv:
        for third in name3[1:]:
            if third not in vowels:
                com_abbrv = com_abbrv[0:2] + third
                print "-----------------", com_abbrv.upper()
                if com_abbrv.upper() in all_comp_abbrv:
                    print "********************"
                    continue
                print dict(abbrv=com_abbrv.upper())


company_UIN_generate("One Delta Technologies Solutions Pvt Ltd")
