import PyPDF2
import pyttsx3
from tkinter.filedialog import *

file = askopenfilename()

pdfReader = PyPDF2.PdfReader(file)
# pages = pdfreader.numPages
pages = len(pdfReader.pages)

for num in range(0, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    print("the texts are: {}".format(text))
    player.runAndWait()

