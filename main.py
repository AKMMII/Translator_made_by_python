import googletrans              #pip install googletrans
import speech_recognition as sr   #pip install speech_recognition
import gtts                       #pip install gtts
import playsound                 #pip install playsoud

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'fr-FR'
output_lang = 'en'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('File name')
playsound.playsound('File name')
# print(googletrans.LANGUAGES)
