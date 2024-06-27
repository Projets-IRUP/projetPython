import mysql.connector
from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Port:
    def __init__(self, id_port, nom, url, latitude,longitude):
        self.id_port = id_port
        self.nom = nom
        self.url = url
        self.latitude = str(latitude)
        self.longitude = str(longitude)

    # def __repr__(self) -> str:
    #     return f"\{'id_port': {self.id_port}, 'nom':{self.nom} \}"


def get_portss():
    ports = []
    try:
        connection = mysql.connector.connect(host='127.0.0.1',database='bdd_maree',user='anthony',password='oketooketo')
        if connection.is_connected():
            print("Connecté à bdd")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM port")
            records = cursor.fetchall()
            for row in records:
                port = Port(row[0], row[1], row[2], row[3], row[4])
                ports.append(port)
    except mysql.connector.Error as error:
        print("Erreur lors de la connexion à MySQL :", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connexion MySQL fermée")
    return ports

def add_maree():
    ports = []
    try:
        connection = mysql.connector.connect(host='127.0.0.1',database='bdd_maree',user='anthony',password='oketooketo')
        if connection.is_connected():
            print("Connecté à bdd")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM port")
            records = cursor.fetchall()
            for row in records:
                port = Port(row[0], row[1], row[2], row[3], row[4])
                ports.append(port)
    except mysql.connector.Error as error:
        print("Erreur lors de la connexion à MySQL :", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connexion MySQL fermée")
    return ports