import PyPDF2
from tkinter.filedialog import *
from googletrans import Translator

file = askopenfilename()
reader = PyPDF2.PdfReader(file)
num_pages = len(reader.pages)

for p in range(num_pages):
    page=reader.pages[p]
    text=page.extract_text()
    # print(text)
    translator=Translator()
    translate_text=translator.translate(text, dest='spanish')
    print(translate_text)