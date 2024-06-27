from classes.db import Db


def select_all():
        
    requete = "SELECT * FROM port"  
    result = Db.query_all(requete)
    return result 

