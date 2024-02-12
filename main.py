from readPdf import readPdf
from tkinter.filedialog import *

file = askopenfilename()

readPdf(file=file)