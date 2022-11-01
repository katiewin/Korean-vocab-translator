import PyPDF2

#change pdf to txt
pdffileobj = open(r'C:\Users\katie\OneDrive\Documents\Korean\Intermediate reading/gk0302_unit02.pdf', 'rb')

pdfreader = PyPDF2.PdfFileReader(pdffileobj)

x = pdfreader.numPages

pageobj = pdfreader.getPage(x+1) 

text=pageobj.extractText()

file1=open(r'C:\Users\katie\OneDrive\Documents\Korean\Intermediate reading\test2.txt',"a")
file1.writelines(text)
