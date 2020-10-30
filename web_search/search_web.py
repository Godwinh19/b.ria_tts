# -*- coding: utf-8 -*-

from selenium import webdriver #to control browser operations
from assistant_speaks import assistant_speaks

def search_web(input):
    
    #os.system("export PATH=$PATH:/home/godwin/Documents/Python/sr/geckodriver-v0.26.0-linux64")
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()        
    
    if 'youtube' in input.lower():
        
        assistant_speaks("Overture dans youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        url = "https://www.youtube.com/results?search_query=" + '+'.join(query)
        print(url)
        driver.get(url)
        return
    elif 'wikipedia' in input.lower():
        
        assistant_speaks("Overture de Wikipedia")
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:]
        url = "https://fr.wikipedia.org/wiki/" + '_'.join(query)
        driver.get(url)
        return 
    else:
        if 'google' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            print(query)
            url = "https://www.google.com/search?q=" + '+'.join(query)
            driver.get(url)
        
        elif 'recherche' in input:
            indx = input.lower().split().index('google')
            print(indx)
            query = input.split()[indx + 1:]
            url = "https://www.google.com/search?q=" + '+'.join(query)
            driver.get(url)
        else:
            url = "https://www.google.com/search?q=" + '+'.join(input.split())
            driver.get(url)
        return 