from PyPDF2 import PdfFileReader, PdfFileWriter
import pandas as pd

file_path = 'bank44.pdf'
pdf  = PdfFileReader(file_path)

with open('text2.txt', 'w', encoding='utf-8') as f:
    for page_num in range(pdf.numPages):
        #print('{0}'.format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            #print('\n'.center(100, '-'))
        except:
            pass
        else:
            #f.write('{0}\n'.format(page_num+1))
            #f.write(''.center(100, '-'))
            f.write(txt)
    f.close()


fin =  open('text2.txt','rt')

data = fin.read()
 

data = data.replace('Date', '\nDATE\t')
data  = data.replace('Description', 'Description\t')
data  = data.replace('Amount','Amount\t')
data  = data.replace('Type','Type\n')
data = data.replace('Account', '\nAccount')
data = data.replace('DR', '\tDR\n')
data = data.replace('CR', '\tCR\n')
data = data.replace('Transaction', '\nTransaction')
data = data.replace('06-2021', '06-2021\t')
data = data.replace('\t', ',')
#data = data.replace('         ', ',')
fin.close()

fin = open('text2.txt', 'wt')

fin.write(data)
fin.close()
str = " "
x = open('text2.txt', 'rt')
for line in x:
    if line.startswith("This"):
        data = data.replace(line, " ")


x.close()
x = open('text2.txt', 'wt')
x.write(data)
x.close()





  
# readinag given csv file
# and creating dataframe
dataframe1 = pd.read_csv("text2.txt")
  
# storing this dataframe in a csv file
dataframe1.to_csv('text2.csv',index = None)

