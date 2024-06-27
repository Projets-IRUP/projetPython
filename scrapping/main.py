import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
from scrap import *
from urllib.parse import quote
from soup3 import *

# Base de l'url 
base_url_scrap ="https://marine.meteoconsult.fr/meteo-marine/horaires-des-marees/"
base_url_api_maree="http://127.0.0.1:5000/" 

# Liste des des mois en français
list_mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin","juillet", "aout", "septembre", "octobre", "novembre", "decembre"]

# Obtenir la date actuelle
date_actuelle = datetime.today()
mois_en_cours  = list_mois[date_actuelle.month-1]
annee_en_cours = str(date_actuelle.year)

#Récupération de la liste des ports 
try:
    # Appel API Maree, méthode GET pour obtenir les ports
    response = requests.get(base_url_api_maree+"port")
    if response.status_code == 200:
        list_port = json.loads(response.text)
    else:
        raise Exception("Statut code api différent de 200")
except Exception as ex:
    erreur = quote("[Scrapping][Main] Une erreur s'est produite à la récupération des ports, " + ex.args[0]+" Arrêt du programme")
    requests.post("https://smsapi.free-mobile.fr/sendmsg?user=49185763&pass=3y7dWE7iULpE0Z&msg="+erreur)
    exit()

# Boucle sur chaque port pour enregistrement
for port in list_port:

    # Construction de l'url
    # Exemple "https://marine.meteoconsult.fr/meteo-marine/horaires-des-marees/port-maria-999/avril-2024"
    url = base_url_scrap + port['url'] + "/"+mois_en_cours+"-"+annee_en_cours

    # Scrapping, 
    try:
        print(port)
        scrap_by_url(url,port['nom'])
        marees = main(port['nom'])
        for maree in marees :
            maree['id_port']=port['id_port']
            print(maree)
            # Appel API Maree, méthode GET pour obtenir les ports
            post = base_url_api_maree+"maree"
           
            reponse = requests.post(post,json=maree)
            print(reponse)

    except Exception as ex:
        erreur = quote("[Scrapping][Main] Une erreur s'est produite au scrapping du port "+port['nom']+", " 
        + ex.args[0]
        +" Arrêt du programme")
        requests.post("https://smsapi.free-mobile.fr/sendmsg?user=49185763&pass=3y7dWE7iULpE0Z&msg="+erreur)
        continue
