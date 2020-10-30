# -*- coding: utf-8 -*-

import wolframalpha # to calculate strings into formula 
from web_search.search_web import search_web
from assistant_speaks import assistant_speaks
from audio.audio import get_audio
from utils import database as db
from datetime import datetime

def process_text(input):
    
    try:
        if 'recherche' in input or 'jouer' in input or 'joue moi' in input:
            #a basic web crawler using selenium
            search_web(input)
            return 
        elif "qui es tu" in input or "defini toi" in input:
            speak = '''Bonjour, je m'appelle Biria. Votre assistant personnel. Je suis là pour vous faciliter la vie. Vous pouvez me commander d'effectuer diverses tâches telles que la recherche sur internet, le calcul de sommes ou l'ouverture d'applications, etc.'''
            assistant_speaks(speak)
            return
        elif "qui t'a créé" in input or "te créé" in input:
            speak = "J'ai été créé par Godwin"
            assistant_speaks(speak)
            return
        elif "calcule" in input.lower():
            
            app_id = "VJX66G-4Q3UL298UU"
            client = wolframalpha.Client(app_id)
            
            indx = input.lower().split().index('calcule')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("La réponse est " + answer)
            return
        elif "open" in input:
            
            # another function to open
            #different application availaible
            #open_application(input.lower())
            speak = "La fonction d'ouverture d'application n'est pas disponible actuellement."
            assistant_speaks(speak)
            return
        elif "fatigué" in input and "suis" in input:
            speak = '''Comment veux tu que je t-aide ?'''
            assistant_speaks(speak)
            return
        elif ("moi" in input or "me" in input) and ("cuisine" in input):
            speak = '''Verse de l'eau sur moi. Et je commencerai.'''
            assistant_speaks(speak)
            return
        elif "love" in input or "amour" in input:
            speak = '''C'est quoi l'amour en réalité '''
            assistant_speaks(speak)
            return
        elif ("fait" in input or "est" in input or "quelle" in input) and "heure" in input:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            assistant_speaks("Il est : "+current_time)
            
        else:
            get_db_response = db.get_response(input)
            if get_db_response:
                assistant_speaks(get_db_response)
                return
            
            assistant_speaks("Je peux faire la recherche sur Google pour toi. Veux tu continuer ?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans) or 'oui' in str(ans):
                search_web(input)
            else:
                assistant_speaks("Que devrais-je repondre?")
                response = get_audio()
                if 'oublie ça' in str(response) or 'laisse' in str(response):
                    return
                elif response =='0':
                    return 
                else:
                    db.create_data_text_table()
                    db.add_text(input, response)
                    
    except:
        assistant_speaks("Je peux faire la recherche sur Google pour toi. Veux tu continuer ?") 
        ans = get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans) or 'oui' in str(ans): 
            search_web(input)
        else:
            assistant_speaks("Que devrais-je repondre?")
            response = get_audio()
            if 'oublie ça' in str(response) or 'laisse' in str(response):
                return
            elif response == '0':
                return
            else:
                db.create_data_text_table()
                db.add_text(input, response)
