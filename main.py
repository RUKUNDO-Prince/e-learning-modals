from readPdf import readPdf
from translatePdf import translatePdf
from tkinter.filedialog import *

print("choose the operation: ")
operation = input()
if str(operation) == "readPdf":
    file = askopenfilename()
    readPdf(file=file)
elif str(operation) == "translatePdf":
    file = askopenfilename()
    translatePdf(file=file)




