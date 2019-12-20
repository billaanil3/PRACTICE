import xlrd
book = xlrd.open_workbook("/home/anil/Downloads/CMT_BBZ_BBI.xls")
print (book.nsheets)
