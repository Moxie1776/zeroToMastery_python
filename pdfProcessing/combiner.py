import sys

import PyPDF2

inputFiles = sys.argv[1:]


def pdfCombiner(pdf_list):
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    print(f'Merged: {pdf}')
    merger.append(pdf)
  merger.write('super.pdf')


pdfCombiner(inputFiles)
