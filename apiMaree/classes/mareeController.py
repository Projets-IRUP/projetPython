from classes.mareeModel import *
from classes.maree import Maree



def add_maree(data):
    
    maree = Maree( None, data['datetime'], data['hauteur'], data['coefficient'], data['type'], data['id_port'])
    reponse_id = insert(maree)
    return reponse_id

def get_marees_by_port_1_j(data):
    reponse = select_maree_by_port_1_j(data['id_port'])
    return [Maree(x[0], x[1], x[2], x[3], x[4], x[5]) for x in reponse]

def get_marees_by_port_3_j(data):
    reponse = select_maree_by_port_3_j(data['id_port'])
    return [Maree(x[0], x[1], x[2], x[3], x[4], x[5]) for x in reponse]

def get_marees_by_port_30_j(data):
    reponse = select_maree_by_port_30_j(data['id_port'])
    return [Maree(x[0], x[1], x[2], x[3], x[4], x[5]) for x in reponse]