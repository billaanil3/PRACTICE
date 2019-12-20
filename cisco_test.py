# a = 0
# b = 1
# for i in range(4, 40):
#     c = a + b
#     a = b
#     b = c
#     if c > 4 and c <= 40:
#         print "--------", c

# ----------------------------------------------
# arr = [50, 100, 200, 5, 2, 1, 500, 2000, 10, 20]
# tot = 5643
# notes = {}
# rem = 0
# res = 0
# if tot > 0:
#     rem = tot % 10
#     res = res + rem
#     tot = tot // 10
#     notes['1'] = rem
# print tot
# ----------------------------------------
# def countCurrency(amount):

#     notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

#     noteCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     print ("Currency Count -> ", zip(notes, noteCounter))
#     for i, j in zip(notes, noteCounter):
#         print ")))))))))))))))", i
#         if amount >= i:
#             j = amount // i
#             print ",,,,,,,,,,", j
#             amount = amount - j * i
#             print "*************", amount
#             print (i, ":", j)

# amount = 3
# countCurrency(amount)
# ------------------------------------------------------------
# class Notebook():
#     pages = {}
#     page = 0
#     data = ''
#     def add(self, page, data):
#         self.data = data
#         self.page = page
#         self.pages['page'] = page
#         self.pages['data'] = data
#         # print self.page
#         # print self.data

#     def delete(self, data):
#         # print self.page, self.data
#         for dt in data.split():
#             if dt == data:
#                 self.data.replace(dt, "")

#     def search(self, data):
#         for dt in data.split():
#             if dt == data:
#                 print "---page----", self.page
#                 print "============", self.pages

# nt = Notebook()
# nt.add(1, "Hello World")
# nt.add(2, "Anil Billa")
# nt.delete("Anil")
# nt.search('Hello')

# ---------------------------------------------------------
# num = int(input("Enter a number:"))
# res = 0
# xx = num
# while num > 0:
#     rem = num % 10
#     res = res * 10 + rem
#     num = num // 10
# if xx == res:
#     print "Polindrome"
# ------------------------------------------------------
# low = int(input("Enter low value:"))
# high = int(input("Enter high value:"))
# for num in range(low, high):
#     if num > 1:
#         for j in range(2, num // 2):
#             if num % j == 0:
#                 break
#         else:
#             print num

# year = int(input("Enter a year:"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400:
#             print "'%s' is a leap year" % (year)
#         else:
#             print "'%s' is not a leap year" % (year)
#     else:
#         print "'%s' is a leap year" % (year)
# else:
#     print "{0} is not a leap year".format(year)

# num = int(input("Enter a number:"))
# notes = {}
# if num > 0:
#     if num % 2000:
#         notes['2000'] = num // 2000
#         num = num % 2000
#     if num % 500:
#         notes['500'] = num // 500
#         num = num % 500
#     if num % 100:
#         notes['100'] = num // 100
#         num = num % 100
#     if num % 50:
#         notes['50'] = num // 50
#         num = num % 50
#     if num % 20:
#         notes['20'] = num // 20
#         num = num % 20
#     if num % 10:
#         notes['10'] = num // 10
#         num = num % 10
#     if num % 5:
#         notes['5'] = num // 5
#         num = num % 5
#     if num % 2:
#         notes['2'] = num // 2
#         num = num % 2
#     if num % 1:
#         notes['1'] = num // 1
#         num = num % 1
# print notes
from collections import OrderedDict
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
amount = int(input("Enter a number:"))
res_notes = OrderedDict()
for note in notes:
    if amount % note:
        if amount // note > 0:
            res_notes[note] = amount // note
        amount = amount % note
print res_notes
