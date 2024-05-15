import requests

def scrap_by_url(url:str,filename:str):
    """
    Méthode récuperant l'intégralité d'une page web (url) et l'enregistre sous son nom(filename)
    """
    # Envoie de la requête GET
    response = requests.get(url)
    reponse = requests.get(url)
    reponse.encoding ="utf-8"
    if reponse.status_code ==200:
        html=reponse.text
        print(html)
        f=open(filename +".html","w",encoding='utf-8')
        f.write(html)
        f.close()
    else:
        raise ValueError("Réponse du GET différent de 200")



    
   