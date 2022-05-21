import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
waterMark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(waterMark.getPage(0))
  output.addPage(page)

  with open('wtrOutput.pdf', 'wb') as newFile:
    output.write(newFile)
