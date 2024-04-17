import requests
from bs4 import BeautifulSoup
from datetime import datetime

'''
url ="https://marine.meteoconsult.fr/meteo-marine/horaires-des-marees/port-maria-999/avril-24"
try:
    
    reponse = requests.get(url)
    reponse.encoding ="utf-8"
except:
    requests.post("https://smsapi.free-mobile.fr/sendmsg?user=49185763&pass=3y7dWE7iULpE0Z&msg=Erreur%20API")

if reponse.status_code ==200:
    html=reponse.text
    print(html)
    f=open("copy.html","w",encoding='utf-8')
    f.write(html)
    f.close()
html = ""
# Ouvrir un fichier en mode lecture
with open("copy.html", "r") as fichier:
    # Lire le contenu du fichier
    html = fichier.read()
'''

# Créer un objet BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Trouver toutes les balises <div> avec la classe "grid col-16 tide"
ListeDivGlobal = soup.find_all('div', class_='grid col-16 tide')


# Afficher le contenu de chaque balise trouvée
for div in ListeDivGlobal:
    print(div)
    print('************************************')

    # Trouver la balise <div> avec la classe "tide-date week"
    date_div = soup.find('div', class_='tide-date week')

    # Récupérer le contenu du span
    date_str = date_div.span.text.strip()

    # Convertir la date en une date valide avec le mois en cours
    # Obtenez le mois actuel
    current_month = datetime.now().strftime("%B").lower()

    # Remplacer le nom du mois dans la chaîne de date par le mois actuel
    date_str = date_str.replace("vendredi", "Friday").replace("samedi", "Saturday").replace("dimanche", "Sunday").replace("lundi", "Monday").replace("mardi", "Tuesday").replace("mercredi", "Wednesday").replace("jeudi", "Thursday").replace("janvier", current_month).replace("février", current_month).replace("mars", current_month)

    # Convertir la chaîne de date en objet datetime
    date = datetime.strptime(date_str, "%A %d %B")

    # Afficher la date
    print(date)



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