'''from tabula import read_pdf


tabula.environment_info()

file_path = 'C:/Users/yanbr/OneDrive/Documentos/Engenharia/CEPEL/Conv_PDF_EXCEL/certparticionado.pdf'

df = read_pdf(file_path,pages = 'all')
print(df)
'''
#https://www.pdftoexcelconverter.net/

'''
from tabula import read_pdf
df = read_pdf('../Pdfs/Libro1.pdf',
              guess=False,
              pandas_options={'skiprows':[0,1],'header':None} 
             )
df.head()
headers = ['Mes','Dia','Año','PptSalpo','TempMax','TempMin','Ppt','Wind','Hum','Solar']
df.columns = headers
df.head()
df.to_excel('../Xls/Libro1.xlsx')
'''
'''from PIL import Image
import pytesseract

file = Image.open("C:/Users/yanbr/OneDrive/Documentos/Engenharia/CEPEL/Conv_PDF_EXCEL/certparticionado.pdf")
str = pytesseract.image_to_string(file, lang='eng')

print(str)
'''

import io
from PIL import Image
import pytesseract
from wand.image import Image as wi
import pandas as pd
from openpyxl.workbook import Workbook
import xlsxwriter


filename = 'C:/Users/yanbr/OneDrive/Documentos/Engenharia/CEPEL/Conv_PDF_EXCEL/certparticionado2.pdf'
pdfFile = wi(filename = filename, resolution = 300)
image = pdfFile.convert('jpeg')

imageBlobs = []

for img in image.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

extract = []
PATH_NAME = 'C:/Users/yanbr/OneDrive/Documentos/Engenharia/CEPEL/Conv_PDF_EXCEL/exemplo3.xlsx'
#workbook = xlsxwriter.Workbook(PATH_NAME)
writer = pd.ExcelWriter(PATH_NAME, engine='xlsxwriter')
#lin = 0
#col = 0

for imgBlob in imageBlobs:
	image = Image.open(io.BytesIO(imgBlob))
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	text = pytesseract.image_to_string(image, lang = 'eng')
	extract.append(text)
	#print(extract)

	df = pd.DataFrame(extract)
	df.to_excel(writer, sheet_name='Sheet1')
	#worksheet = workbook.add_worksheet()
	#for items in extract:
		#worksheet.write(lin, col, items)
		#lin+=1
writer.save()
#print(extract)
#workbook.close()
#df1 = pd.DataFrame(extract)
#print(df1)

