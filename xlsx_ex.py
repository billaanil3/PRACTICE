'''
# Onboard company using XSL
import argparse
import os
import sys
import json
import xlrd

book = xlrd.open_workbook("CMT_Onboarding_ThemisAssociates_20022018.xlsx")
conditions , categories = {} , []
for sheet in book.sheets():
   if sheet.name.lower() == 'categories':
      for rownum in range(sheet.nrows):
         if sheet.row(rownum)[0].value.strip():
            categories.append(sheet.row(rownum)[0].value.strip())
      print "----------",categories
   if sheet.name.lower() == 'company_category_conditions_map':
      print sheet.name
      for rownum in range(1, sheet.nrows):
	 #print rownum
         if sheet.row(rownum)[0].value.strip():
	    #print sheet.row(rownum)[0].value.strip()
	    #print sheet.row(rownum)[1].value.strip()
	    #print conditions[(sheet.row(rownum)[0].value.strip())]
            conditions[str(sheet.row(rownum)[0].value.strip())] = str(sheet.row(rownum)[1].value.strip())
            print "#########################",conditions[sheet.row(rownum)[0].value.strip()]
   if sheet.name.lower() == "companies":
      if sheet.row(1)[0].value.strip():
	 name = sheet.row(1)[0].value.strip()
         abbr = sheet.row(1)[1].value.strip()
	 print name,"----------",abbr   

'''
import xlrd
workbook = xlrd.open_workbook("CMT_Onboarding_ThemisAssociates_20022018.xlsx")
print workbook.nsheets  #print No.Of sheets
print workbook.sheet_names()    #print sheet names

worksheet = workbook.sheet_by_index(10) #select 1oth sheet,We can give any index here like 0,1,2,3,4..........
print worksheet.nrows   # No.of rows
print worksheet.ncols   # No.of cols

print worksheet.row_values(0) # print First row
print worksheet.col_values(1) # and second column

#get slice of column=2 for rows=1....6
a = worksheet.col_values(2,1,6)
print a

# get value of cell
# d = worksheet.cell(2,3).value
# print d
# print sum(d)

# # to convert value od date to tuple

# dt = xlrd.xldate_as_tuple(d,workbook.datemode)
# print dt