# -*- coding: utf-8 -*-
from assistant_speaks import assistant_speaks
from audio.audio import get_audio
from utils import database as db


while(1):
    question  = input()
    if question != '0':
        assistant_speaks("La question est : "+question)
        assistant_speaks("Que dois-je repondre ?")
        response = input()
    
        assistant_speaks(f"Question : {question}\nResponse : {response}")
        assistant_speaks("Dois je l'enregistrer ?")
        ans = input()
        
        if 'oui' in str(ans) or 'yeah' in str(ans):
            db.create_data_text_table()
            db.add_text(question, response)

