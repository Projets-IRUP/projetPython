import mysql.connector

class Port:
    def __init__(self, id_port, nom, url):
        self.id_port = id_port
        self.nom = nom
        self.url = url

def get_portss():
    ports = []
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='bdd_maree',
                                             user='anthony',
                                             password='oketooketo')
        if connection.is_connected():
            print("Connecté à bdd")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM port")
            records = cursor.fetchall()
            for row in records:
                port = Port(row[0], row[1], row[2])
                ports.append(port)
    except mysql.connector.Error as error:
        print("Erreur lors de la connexion à MySQL :", error)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connexion MySQL fermée")
    return ports