# -*- coding: utf-8 -*-

import speech_recognition as sr
from assistant_speaks import assistant_speaks

    
def get_audio():
    
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak....")
        
        # Recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit= 3)
    print("Stop.")  #limit 5 seconds
    #text = input("text : ")
    try:
        
        text = rObject.recognize_google(audio, language='fr-FR')
        print("Vous : ", text)
        return text
    except:
        text = '0'
        assistant_speaks("J'arrive pas à comprendre l'audio. Réessayez !")
        return text


