#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request
from classes.db import Db
# Classe

# Controller
from classes.portController import get_ports
from classes.mareeController import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
 return '''<h1>API MAREE</h1>
<p>Ce site est le prototype d’une API mettant à disposition les ports et les marées.</p>'''


@app.route('/port',methods=['GET'])
def route_port_get():
    # Récupérer la liste d'objets Port
    ports = get_ports()
    return ports, 200, {'Content-Type': 'application/json'}


@app.route('/maree',methods=['POST'])
def route_maree_post():
    # Récupérer les données JSON de la requête
    data = request.get_json()
    reponse = json.dumps(add_maree(data)) 

    return reponse, 200, {'Content-Type': 'application/json'}


# En poste car biblio android ne prend pas en charge le json dans le body en GET
@app.route('/maree1j',methods=['POST'])
def route_maree_get_1_j():
    # Récupérer la liste d'objets Maree
    data = request.get_json()
    marees = get_marees_by_port_1_j(data)
    return marees, 200, {'Content-Type': 'application/json'}

@app.route('/maree3j',methods=['POST'])
def route_maree_get3j():
    # Récupérer la liste d'objets Maree
    data = request.get_json()
    marees = get_marees_by_port_3_j(data)
    return marees, 200, {'Content-Type': 'application/json'}

@app.route('/maree30j',methods=['POST'])
def route_maree_get30j():
    # Récupérer la liste d'objets Maree
    data = request.get_json()
    marees = get_marees_by_port_30_j(data)
    return marees, 200, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    # Connection bdd
    Db.open()
    # auto reload de l'API
    app.run(debug=True)