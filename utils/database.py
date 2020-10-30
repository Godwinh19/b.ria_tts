# -*- coding: utf-8 -*-

from typing import List, Dict, Union
from .database_connection import DatabaseConnection

#Book = Dict(str, Union(str,int))

def create_data_text_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
    
        cursor.execute('CREATE TABLE IF NOT EXISTS data_text(question text primary key,response text)')
    
       
def add_text(question: str,response: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('INSERT INTO data_text VALUES(?,?)',(question,response))
        except:
            print ('Vous avez deja ajouté cette question.')
    #except sqlite3.OperationalError:
    #    print('Internal error.')
     


def get_response(question) ->str:
   with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM data_text WHERE question=?',(question,))
        respsonses =[{'question': row[0], 'response': row[1]} for row in cursor.fetchall()]
        
   return respsonses[0]['response']
