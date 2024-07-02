
### Projet IRUP, 2024 
### Contacts
Anthony Barriol,  
Mathis Vercelloni

# Projet API Marrée 


## Description
Ce projet vise à développer une API RESTful distribuant les horaires des marées et des ports.
L’objectif est de fournir une API gratuite consommable et facile d’accès par différentes plateformes 
tel que l’application Android (projet Kotlin).

## Fonctionnalités
* Gestion des ports : Création et suppression et consultation des ports. 
* Gestion des marées : Création et consultation des horaires des marées par filtrage.  
* Ajout possible de toutes autres fonctionnalités utiles.
## Technologies Utilisées
- Python
- Flask
- BeautifulSoup4 (pour le web scraping)
- Requests (pour effectuer des requêtes HTTP)
- Base de donnée MySQL

## Prérequis
- Python 3

## Installation

1. **Cloner le dépôt:**
    ```bash
    git clone https://github.com/Projets-IRUP/projetPython.git
    ```


3. **Installer les dépendances:**
    ```bash
   pip install flask requests beautifulsoup4

    ```

## Configuration
Mettre à jour le fichier `db.py` avec les configurations nécessaires, comme les URLs pour le web scraping et les clés API si nécessaire.

## Utilisation

1. **Lancer l'API :**
    ```bash
    python3 app.py
    ```

1. **Lancer le scrapping :**
    ```bash
    python3 main.py
    ```
2. **Accéder à l'API:**
    L'API sera accessible à `http://127.0.0.1:5000`.


## Structure
```
apiMaree/
├── classes/
│ ├── pycache/
│ ├── db.py
│ ├── maree.py
│ ├── mareeController.py
│ ├── mareeModel.py
│ ├── port.py
│ ├── portController.py
│ ├── portModel.py
│ ├── testMaree.py
├── app.py
├── archives/
│ ├── c_port.py
│ ├── m_port.py
│ ├── model.py
│ ├── soup.py
├── bddMaree/
├── scrapping/
│ ├── pycache/
│ ├── main.py
│ ├── scrap.py
│ ├── soup3.py
├── port-maria.html
└── README.md
```