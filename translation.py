# ------------------------------------------------------------------------------
# Imports
import googletrans
from googletrans import Translator
import pyttsx3

# ------------------------------------------------------------------------------
# Setup
translator = Translator()
# ------------------------------------------------------------------------------
# Part 1:
translate = translator.translate('Hello There How Are You', dest='french')
print(translate.text)

# ------------------------------------------------------------------------------
# Part 2:
print(translator.detect('안녕하세요, 잘 지내세요'))

# ------------------------------------------------------------------------------
# Part 3:

input_text = input('Input Your Translation Text : ')
input_language = input('Input Your Translation Language : ')

translation = translator.translate(input_text, dest=input_language)
print(translation.text)
# ------------------------------------------------------------------------------
# Part 4:
speaker = pyttsx3.init()
translate_speech = translator.translate('Hello There How Are You, I am proud of you', dest='spanish')

speaker.say(translate_speech.text)
speaker.runAndWait()
