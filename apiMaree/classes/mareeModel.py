from classes.db import Db
from classes.maree import Maree


 
def insert( maree:Maree):

    requete = """ INSERT INTO maree (date_heure, hauteur, maree_type, coefficient, id_port) VALUES (%s, %s, %s, %s, %s)"""  
    reponse_id = Db.query_insert(requete,(maree.date_heure, maree.hauteur, maree.maree_type, maree.coefficient, maree.id_port))
    return reponse_id

def select_maree_by_port_1_j(id_port):
        
    requete = """SELECT * FROM maree where id_port = %s and DATE(date_heure) = DATE(now());"""  
    parametre = (id_port,)
    # print(type(parametre))
    result = Db.query_all(requete,parametre)
    return result 

def select_maree_by_port_3_j(id_port):
        
    requete = """SELECT * FROM maree where id_port = %s and  DATE(date_heure) BETWEEN DATE(now()) AND DATE(DATE_ADD(now(), INTERVAL 3 DAY));"""  
    parametre = (id_port,)
    # print(type(parametre))
    result = Db.query_all(requete,parametre)
    return result 

def select_maree_by_port_30_j(id_port):
        
    requete = """SELECT * FROM maree where id_port = %s and  DATE(date_heure) BETWEEN DATE(now()) AND DATE(DATE_ADD(now(), INTERVAL 30 DAY));"""  
    parametre = (id_port,)
    # print(type(parametre))
    result = Db.query_all(requete,parametre)
    return result 
