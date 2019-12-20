"""
import pdfcrowd
import sys

try:
    client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
    client.convertUrlToFile('https://www.merchantmaverick.com/reviews/bluepay-processing-review/', 'signup.pdf')
except pdfcrowd.Error as why:
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
    raise
"""


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
from zipfile import ZipFile
import pdfkit
# pdfkit.from_url('https://www.merchantmaverick.com/reviews/bluepay-processing-review/','my_testpdf.pdf')
html_file = '/home/anil/Desktop/Detailed_Reports/Detailed_Report_byLawArea20191024_10-05-02.html'
pdf_file = ''
pdfkit.from_file(html_file, 'output.pdf')
with ZipFile('/home/anil/Desktop/Detailed_Reports/my_python_files.zip', 'w') as zip:
    # writing each file one by one
    # for file in file_paths:
    zip.write('/home/anil/Desktop/Detailed_Reports/output.pdf')
