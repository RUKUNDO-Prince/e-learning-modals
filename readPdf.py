import PyPDF2
import pyttsx3
import pdfplumber

def readPdf(file):
    pdfReader = PyPDF2.PdfReader(file)
    pages = len(pdfReader.pages)

    # for num in range(0, pages):
    #     page = pdfReader.pages[num]
    #     text = page.extract_text()
    #     player = pyttsx3.init()
    #     player.say(text)
    #     # print("the texts are: {}".format(text))
    #     player.runAndWait()

    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            # print(text)
            s = pyttsx3.init()
            s.save_to_file(text, 'file-audio.mp3')
            s.say(text)
            s.runAndWait()

    file.close()