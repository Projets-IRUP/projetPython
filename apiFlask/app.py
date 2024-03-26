#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
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
app.run(debug=True)