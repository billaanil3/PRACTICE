import xlrd
book = xlrd.open_workbook("/home/anil/Downloads/CMT_BBZ_BBI.xlsx")
print (book.nsheets)
print (book.sheet_names())
#for sheet in book.sheets():
   
