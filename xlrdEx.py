import xlsxwriter

workbook = xlsxwriter.Workbook("xlsxEx.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write('A1','Country')
worksheet.write('B1','Population')
worksheet.write('A2','India')
worksheet.write('B2','20000000000')
worksheet.write('A3','Chia')
worksheet.write('B3','10000000000')

workbook.close()
