import googletrans
from googletrans import Translator
import pyttsx3

def translateText():
    translator = Translator()
    # translate = translator.translate('Hello There How Are You', dest='french')
    # print(translate.text)

    # print(translator.detect('안녕하세요, 잘 지내세요'))

    input_text = input('Input Your Translation Text : ')
    input_language = input('Input Your Translation Language : ')

    translation = translator.translate(input_text, dest=input_language)
    print(translation.text)

    speaker = pyttsx3.init()

    speaker.say(translation.text)
    speaker.runAndWait()
