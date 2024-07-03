import requests
from datetime import datetime

# Bases des url
BASE_URL_SCRAP ="https://marine.meteoconsult.fr/meteo-marine/horaires-des-marees/"

# Liste des des mois en français
LISTE_MOIS = ["janvier", "fevrier", "mars", "avril", "mai", "juin","juillet", "aout", "septembre", "octobre", "novembre", "decembre"]

def scrap_by_url(port):
    """
    Méthode récuperant l'intégralité de la page web des marées du mois en cours et du port fournit en paramètre et l'enregistre sous le nom du port
    """

    # Obtenir la date actuelle
    date_actuelle = datetime.today()
    mois_en_cours  = LISTE_MOIS[date_actuelle.month-1]
    annee_en_cours = str(date_actuelle.year)

    # Composition de l'url à scrapper
    url = BASE_URL_SCRAP + port['url'] + "/" + mois_en_cours + "-" + annee_en_cours

    # Envoie de la requête GET
    reponse = requests.get(url)
    reponse.encoding ="utf-8"
    if reponse.status_code ==200:
        html=reponse.text
        #print(html)
        f=open(port['nom'] +".html","w",encoding='utf-8')
        f.write(html)
        f.close()
    else:
        raise ValueError("Réponse du GET différent de 200")



    
   