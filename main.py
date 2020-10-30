#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:07:47 2020

@author: godwin
"""

import os # to save/open file
from datetime import datetime
from audio.audio import get_audio
from assistant_speaks import assistant_speaks
from text_processing.process_text import process_text


#Driver code
if __name__ == "__main__":
    assistant_speaks("Quel est ton nom, Humain")
    name = 'Humain'
    name = get_audio()
    assistant_speaks("Hello, "+ str(name) + '.')
    
    while(1):
        
        assistant_speaks("Que puis-je faire pour toi?")
        text = get_audio().lower()
        
        if text ==0:
            continue
        
        if "au revoir" in str(text) or "bye" in str(text) or "dormir" in str(text):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if current_time < '12:00:00':
                assistant_speaks("OK bye, "+ name+'.'+" Bonne journée.")
            else:
                assistant_speaks("OK bye, "+ name+'.'+"Bonne soirée.")
            break
        
        #Calling process text to process the query
        process_text(text)
        

#function used to open application present inside the system.
def open_application(input):
    if "chrome" in input:
        assistant_speaks("Google Chrome")
        #os.startfile("")