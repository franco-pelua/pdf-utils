#!/usr/bin/env python

import PyPDF2

# Paths in your machine that point to the files that you want to merge
pdfs_paths = ["", ""]

# Desired output file name
output_file_name = ""

merger = PyPDF2.PdfFileMerger()

for path in pdfs_paths:
        merger.append(PyPDF2.PdfFileReader(path, 'rb'))

with open(output_file_name, 'wb') as output:
    merger.write(output)

print('Your pdf has been merged')


