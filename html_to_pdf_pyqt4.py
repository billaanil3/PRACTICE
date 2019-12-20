# from PyQt4.QtGui import QTextDocument, QPrinter, QApplication

# import sys
# app = QApplication(sys.argv)

# doc = QTextDocument()
# location = "/home/anil/Desktop/Detailed_Reports/Detailed_Report_byLawArea20191024_10-05-02.html"
# html = open(location).read()
# doc.setHtml(html)

# printer = QPrinter()
# printer.setOutputFileName("foo.pdf")
# printer.setOutputFormat(QPrinter.PdfFormat)
# printer.setPageSize(QPrinter.A4)
# printer.setPageMargins(15, 15, 15, 15, QPrinter.Millimeter)
# doc.print_(printer)
# print "done!"

# ///////////////////////////////////////////////////////////////////////
"""import pdfcrowd
import sys

try:
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    # run the conversion and write the result to a file
    html_file = '/home/anil/Desktop/Detailed_Reports/Detailed_Report_byLawArea20191024_10-05-02.html'
    pdf_file = 'MyLayout.pdf'
    client.convertFileToFile(html_file, pdf_file)
except pdfcrowd.Error as why:
    # report the error
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

    # handle the exception here or rethrow and handle it at a higher level
    raise"""
# ////////////////////////////////////////////////////////////////////////

import pdfcrowd
import sys

try:
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
    html_file = '/home/anil/Desktop/Detailed_Reports/Detailed_Report_byLawArea20191024_10-05-02.html'
    pdf_file = 'MyLayout_New.pdf'
    # create output file for conversion result
    output_file = open(pdf_file, 'wb')

    # run the conversion and store the result into a pdf variable
    pdf = client.convertFile(html_file)

    # write the pdf into the output file
    output_file.write(pdf)

    # close the output file
    output_file.close()
except pdfcrowd.Error as why:
    # report the error
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

    # handle the exception here or rethrow and handle it at a higher level
    raise
