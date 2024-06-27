from classes.portModel import *
from classes.port import Port




def get_ports():
    reponse = select_all()
    return [Port(x[0], x[1], x[2], x[3], x[4]) for x in reponse]
    
    #def get_ports():
    #    ports=[]
    #    reponse = portModel.select_all()
    #    for ligne in reponse:
    #        ports.append(Port(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4]))
    #    return ports