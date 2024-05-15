#!/usr/bin/env python
# encoding: utf-8
from controller import c_port
import json
from flask import Flask
from flask import jsonify
app = Flask(__name__)

marees_quiberon = [
    {"heure": "05:30", "hauteur": 3.2},
    {"heure": "11:42", "hauteur": 0.8},
    {"heure": "17:59", "hauteur": 3.5},
    {"heure": "23:59", "hauteur": 0.6}
]
@app.route('/maree')
def index():
    return json.dumps(marees_quiberon)

@app.route('/GetPorts',methods=['GET'])
def get_ports():
    ports = c_port.get_portss()  # Récupérer la liste d'objets Port

    # Définir une fonction pour sérialiser les objets Port en JSON
    def port_to_json(port):
        return {'id_port': port.id_port, 'nom': port.nom, 'url': port.url}

    # Utiliser la fonction 'port_to_json' pour sérialiser chaque objet Port
    ports_json = json.dumps(ports, default=port_to_json)

    return ports_json, 200, {'Content-Type': 'application/json'}

# auto reload de l'API

app.run(debug=True)