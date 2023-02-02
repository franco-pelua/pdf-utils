#!/usr/bin/env python

import PyPDF2

# Paths in your machine that point to the files that you want to merge
pdfs_paths = ["", ""]

# Desired output file name
output_file_name = ""

merger = PyPDF2.PdfMerger()

for path in pdfs_paths:
    with open(path, 'rb') as pdf:
        merger.append(pdf)

with open(output_file_name, 'wb') as output:
    merger.write(output)

print('Your pdf has been merged')


