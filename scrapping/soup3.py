import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

def recuperer_html(filename):
    """Récupère le contenu HTML du fichier."""
    with open(filename+".html", "r") as fichier:
        # Lire le contenu du fichier
        html = fichier.read()

    return BeautifulSoup(html, 'html.parser')

def extraire_date(jour):
    """Extrait la date de la structure HTML du jour."""
    date_str = jour.find('div', class_='tide-date').get_text(strip=True)
    current_year = datetime.now().year
    current_month = datetime.now().month
    day = int(date_str.split()[1])
    date_complete = datetime(current_year, current_month, day)
    return date_complete

def extraire_info_maree(maree, date, coefficient):
    """Extrait les informations sur une marée spécifique (haute ou basse)."""
    heure_str = maree.find('span', class_='hour').get_text(strip=True)
    heure = datetime.strptime(heure_str, '%Hh%M').time()
    date_time = datetime.combine(date.date(), heure)
    # Extraction et conversion du type de marée
    type_maree_str = maree.find('span', class_='label').get_text(strip=True)
    type_maree = 1 if type_maree_str.lower() == 'marée haute' else 0
    # Conversion de la hauteur en float et du coefficient en int
    hauteur_str = maree.find('span', class_='height').get_text(strip=True)
    hauteur = float(re.sub(r'[^\d.]', '', hauteur_str))  # Retirer tout sauf les chiffres et le point
    
    coefficient = int(coefficient) if coefficient else None

    return {
        'datetime': date_time.strftime('%Y-%m-%d %H:%M:%S'),
        'type':type_maree,
        'hauteur':hauteur,
        'coefficient': coefficient
    }

def extraire_donnees_maree(jour):
    """Extrait toutes les données de marée pour un jour donné."""
    date = extraire_date(jour)
    lignes_maree = jour.find_all('div', class_='tide-line')
    liste_info_maree = []

    for ligne in lignes_maree:

        marees = ligne.find_all("div", {"class": re.compile(r'.*-tide$')})
      
        coef = ligne.find('div', class_='coef')
        coefficient = coef.find('span').get_text(strip=True) if coef else None

        for maree in marees:
          
            liste_info_maree.append(extraire_info_maree(maree, date, coefficient))
     
  
    return liste_info_maree

def extraire_toutes_marees(soup):
    """Extrait les données de marée pour tous les jours."""
    jours = soup.find_all('div', class_='grid col-16 tide')
    toutes_donnees_maree = []
    
    for jour in jours:
        toutes_donnees_maree.extend(extraire_donnees_maree(jour))
    
    return toutes_donnees_maree

def main(filename):
    soup = recuperer_html(filename)
    previsions_maree = extraire_toutes_marees(soup)
    
    return previsions_maree
    for maree in previsions_maree:
        print(f"Datetime: {maree['datetime']}, Type: {maree['type']}, Hauteur: {maree['hauteur']}, Coefficient: {maree['coefficient']}")

# if __name__ == "__main__":
#     main('path_to_your_html_file')
