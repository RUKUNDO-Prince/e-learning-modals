from readPdf import readPdf
from speechToText import speechToText
from translatePdf import translatePdf
from translation import translateText
# from voiceAssistant import assistant
from tkinter.filedialog import *

while True:
    print("Choose the operation(type help for available operations, or exit to quit): ")
    operation = input().strip().lower()

    if operation == "help":
        print("Available operations are: readPdf, translatePdf, translateText, speechToText, assistant, and generateSubtitles")
    elif operation == "readpdf":
        file = askopenfilename()
        readPdf(file=file)
    elif operation == "translatepdf":
        file = askopenfilename()
        translatePdf(file=file)
    elif operation == "translatetext":
        translateText()
    elif operation == "speechtotext":
        speechToText()
    elif operation == "assistant":
        assistant()
    elif operation == "exit":
        print("Exiting program...")
        break
    else:
        print("Operation not found, type help for available operations")
