import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

# Ouvrir un fichier en mode lecture
with open("copy.html", "r") as fichier:
    # Lire le contenu du fichier
    html = fichier.read()

# Créer un objet BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Trouver toutes les balises <div> avec la classe "grid col-16 tide"
ListeDivGlobal = soup.find_all('div', class_='grid col-16 tide')

# Obtenez le mois actuel et l'année
current_month = datetime.now().strftime("%m")
current_year = datetime.now().strftime("%Y")

tableau = []

# Afficher le contenu de chaque balise trouvée
for div in ListeDivGlobal:
    date_div = div.find('div', class_='tide-date')

    if date_div is not None:
        date_str = date_div.span.text.strip()
        day = date_str.split(' ')[1]

        if len(day) == 1:
            day = '0' + day

        complete_date_str = f"{day}/{current_month}/{current_year}"
        date = datetime.strptime(complete_date_str, "%d/%m/%Y")

        # Trouver la balise <div> avec la classe "tide-container" à l'intérieur de chaque div
        tides_div = div.find('div', class_='tide-container')

        # Vérifier si tides_div est None
        if tides_div is not None:
            # Trouver toutes les balises <span> avec la classe "hour" à l'intérieur de tides_div
            hour_spans = tides_div.find_all('span', class_='hour')
        
            # Trouver toutes les balises <span> avec la classe "label" à l'intérieur de tides_div
            label_spans = tides_div.find_all('span', class_='label')

            # Trouver toutes les balises <span> avec la classe "height" à l'intérieur de tides_div
            height_spans = tides_div.find_all('span', class_='height')


            # 
            # Trouver toutes les balises <span> à l'intérieur des balises <div> avec les classes
            span_tags = tides_div.find_all("div", {"class": re.compile("^tide-coef-level-")})

            '''
            # Imprimer la date et l'heure pour chaque balise hour_span trouvée
            for i in range(len(hour_spans)):
                print(f"{date}, {hour_spans[i].text}, {label_spans[i].text.split(' ')[1]}, {height_spans[i].text}")
            '''
            # Afficher le contenu des balises <span>
            for span_tag in span_tags:
                print(span_tag.text)
            
            print("********************************************")

            
        # Créer une liste vide pour stocker les informations sur les marées
            tide_info = []

            # Imprimer la date et l'heure pour chaque balise hour_span trouvée
            for i in range(len(hour_spans)):
                # Ajouter l'heure à la date
                complete_date_str = f"{day}/{current_month}/{current_year} {hour_spans[i].text}"
                
                # Convertir la date et l'heure en un objet datetime
                date = datetime.strptime(complete_date_str, "%d/%m/%Y %Hh%M")
                
                # Convertir le type de marée en binaire
                tide_type = 0 if label_spans[i].text.split(' ')[1] == 'basse' else 1
                
                # Convertir la hauteur en mètres
                height = float(height_spans[i].text.replace('m', ''))
                
                # Créer un dictionnaire pour stocker les informations sur une marée
                tide_dict = {
                    "datetime": date,
                    "tide_type": tide_type,
                    "height": height
                }
                
                # Ajouter le dictionnaire à la liste
                tide_info.append(tide_dict)

            # Imprimer les informations sur les marées
            for info in tide_info:
                print(info)