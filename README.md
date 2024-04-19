# Projet Python

## Site à Scrap : 
- https://marine.meteoconsult.fr/meteo-marine/horaires-des-marees/biarritz-1085/mars-2024


# Ce qu'il faut récupérer : 
- un port
- Jour de la semaine
- Heure Marée basse et haute
- Coefficient de marée 

partir de grid col-16 tide
ligne 1827

Convertir les textes en jours de la semaine.
Convertir les textes en heures de marées
Convertir les textes en coefficient de marées

boucle sur les ports et une fois sur les mois en cours


# Old :

'''
# maree = soup.find_all("vendredi 22")
# for child in maree[0].children:
#     print(child)
# print(maree.contents[0])

        # Trouver le tableau contenant les données des marées (exemple)
tableau_marees = soup.find("table", class_="marees-table")

# Récupérer la date du premier jour du mois
premier_jour_du_mois = datetime.now().replace(day=1).strftime("%Y-%m-%d")

# Trouver les lignes du tableau correspondant au premier jour du mois (exemple)
premier_jour_rows = tableau_marees.find_all("tr", {"data-date": premier_jour_du_mois})

# Afficher les horaires des marées pour le premier jour du mois
for row in premier_jour_rows:
    heures = row.find_all("td")[0].text
    hauteurs = row.find_all("td")[1].text
    print("Heures:", heures)
    print("Hauteurs:", hauteurs)

# else :
requests.post("https://smsapi.free-mobile.fr/sendmsg?user=49185763&pass=3y7dWE7iULpE0Z&msg=Erreur%20API")
'''