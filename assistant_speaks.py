# -*- coding: utf-8 -*-

from gtts import gTTS # google text to speech
from playsound import playsound  #to play saved mp3 file
import os

num =1
def assistant_speaks(output):
    global num
    
    # num to rename every audio file
    # with different name to remove ambiguity
    num+=1
    print("Biria : ", output)
    
    #toSpeak = gTTS(text= output, lang='fr', slow=False)
    #Saving the audio file given by google text to speech
    #file = str(num)+".mp3"
    #toSpeak.save(file)
    #playsound(file)
    #os.system("vlc  --play-and-exit "+file)
    
