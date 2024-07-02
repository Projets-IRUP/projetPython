import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
from scrap import *
from urllib.parse import quote
from soup3 import *

# Bases des url
BASE_URL_API_MAREE="http://127.0.0.1:5000/" 
BASE_URL_API_SMS = "https://smsapi.free-mobile.fr/sendmsg?user=49185763&pass=3y7dWE7iULpE0Z&msg="

def envoie_sms(message):
    """"Envoie un sms au portable Anthony Barriol"""
    requests.post(BASE_URL_API_SMS+message)

def recup_liste_port():
    """Retourne la liste des ports"""
    # Appel API Maree, méthode GET pour obtenir les ports
    response = requests.get(BASE_URL_API_MAREE+"port")
    if response.status_code == 200:
        liste_port = json.loads(response.text)
        return liste_port
    else:
        raise Exception("Statut code api différent de 200")


def enregistrement_maree(marees,port):
    """Enregistre les marees via l'api dans la bdd"""
    for maree in marees :
        try:
            #Ajout du port_id
            maree['id_port']=port['id_port']
            print(maree)

            # Appel API Maree, méthode GET pour obtenir les ports
            post = BASE_URL_API_MAREE+"maree"
            reponse = requests.post(post,json=maree)
            print("Statut Code : "+reponse.status_code) 

        except Exception as exception:
             envoie_sms("[Python][Scrapping][main.py], Une exception a été levée lors d'un enregistrement de maree, port : "+port['nom'] )

if __name__ == "__main__":

    try:

        print("Récuperation des ports ...")
        liste_port = recup_liste_port()
       
    except Exception as exception:
        envoie_sms("[Python][Scrapping][main.py], Une exception a été levée lors de la récupération des ports")
        exit()

    # Boucle sur chaque port 
    for port in liste_port:

        print("Port:" + port["nom"])

        # Mise en cache de la page web
        print("Début scrapping...")
        scrap_by_url(port)
        print("Scrapping ok")

        # Traitement du cache
        print("Début scrapping analyse...")
        marees = analyse(port['nom'])
        print("Scrapping analyse ok")

        # Enregistrement 
        print("Enregistremen via API Maree...")
        enregistrement_maree(marees, port)
        print("Fin enregistrement")
        
        
