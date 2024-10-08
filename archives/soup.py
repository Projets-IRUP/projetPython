
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

def traitement_donnees_maree(filename:str) -> None:
    """
    Méthode permetant de récupérer de le html, les informations des marées pour un port sur un mois

    Arguments:
    filename  – first name, must be string
    
    Return:
    Tableau contenant la liste des marées pour chaque jour d'un port 

    """
    # Ouvrir un fichier en mode lecture
    with open(filename+".html", "r") as fichier:
        # Lire le contenu du fichier
        html = fichier.read()

    # Créer un objet BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Trouver toutes les balises <div> avec la classe "grid col-16 tide"
    # Contient la liste des div contenant l'ensemble des information d'une marée ( 1 élément = 1 marée) 
    ListeDivGlobale = soup.find_all('div', class_='grid col-16 tide')

    # Obtenez le mois actuel et l'année
    mois_en_cours = datetime.now().strftime("%m")
    annee_en_cours = datetime.now().strftime("%Y")


    # Contenu de l'ensemble des marées d'un port sur un mois, 1 élément = marées d'une journée 
    tableau = []

    # Afficher le contenu de chaque balise trouvée
    for div in ListeDivGlobale:
        date_div = div.find('div', class_='tide-date')

        if date_div is not None:
            date_str = date_div.span.text.strip()
            jour = date_str.split(' ')[1]

            if len(jour) == 1:
                jour = '0' + jour

            complete_date_str = f"{jour}/{mois_en_cours}/{annee_en_cours}"
            date = datetime.strptime(complete_date_str, "%d/%m/%Y")

            # Trouver la balise <div> avec la classe "tide-container" à l'intérieur de chaque div
            maree_div = div.find('div', class_='tide-container')

            # Vérifier si tides_div est None
            if maree_div is not None:
                # Trouver toutes les balises <span> avec la classe "hour" à l'intérieur de tides_div
                hour_spans = maree_div.find_all('span', class_='hour')
            
                # Trouver toutes les balises <span> avec la classe "label" à l'intérieur de tides_div
                label_spans = maree_div.find_all('span', class_='label')

                # Trouver toutes les balises <span> avec la classe "height" à l'intérieur de tides_div
                height_spans = maree_div.find_all('span', class_='height')

                # Trouver toutes les balises <span> à l'intérieur des balises <div> avec les classes
                coef_spans = maree_div.find_all("div", {"class": re.compile("^tide-coef-level-")})

                
            # Liste pour stocker les valeurs extraites des balises <span>
                coefficients = []

                # Afficher le contenu des balises <span> et ajouter les valeurs à la liste
                for coef_tag in coef_spans:
                    coef_value = int(coef_tag.text.strip())
                    coefficients.append(coef_value)
                    
                print("********************************************")
                
                
            # Créer une liste vide pour stocker les informations sur les marées
                maree_info = []
            # Déterminer le nombre minimum d'éléments entre hour_spans et coefficients
            num_elements = min(len(hour_spans), len(coefficients))
            
            # Imprimer la date et l'heure pour chaque balise hour_span trouvée
            for i in range(len(hour_spans)):
                # Ajouter l'heure à la date
                complete_date_str = f"{jour}/{mois_en_cours}/{annee_en_cours} {hour_spans[i].text}"
                    
                # Convertir la date et l'heure en un objet datetime
                date = datetime.strptime(complete_date_str, "%d/%m/%Y %Hh%M")
                    
                # Convertir le type de marée en binaire
                type_maree = 0 if label_spans[i].text.split(' ')[1] == 'basse' else 1
                    
                # Convertir la hauteur en mètres
                hauteur = float(height_spans[i].text.replace('m', ''))
                    
                # Créer un dictionnaire pour stocker les informations sur une marée
                maree_dict = {
                        "date_heure": date,
                        "type_maree": type_maree,
                        "hauteur": hauteur
                }
                
                 
                    
                # Ajouter le coefficient de marée si le type de marée est égal à 1
                if type_maree == 1:
                    if( i < 2):
                        coef = coefficients[0]  # Récupérer le coefficient de marée
                        maree_dict["coef"] = coef
                    else:
                        maree_dict["coef"] = coefficients[1]
                else:
                                maree_dict["coef"] = None  # Coefficient vide pour les marées 

                # Ajouter le dictionnaire à la liste des marées
                maree_info.append(maree_dict)
                
            # Ajouter les informations sur les marées à la liste principale
            tableau.extend(maree_info)

            # Imprimer les informations sur les marées
            for info in maree_info:
                print(info)
        # Afficher le tableau complet des coefficients
        print(coefficients)
