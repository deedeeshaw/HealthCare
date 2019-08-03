######################################################################
# IMPORT FLASK
######################################################################
from flask import Flask, render_template, request, redirect, jsonify
import requests
import pandas as pd

######################################################################
# create app passing the __name__
######################################################################
app = Flask(__name__)

######################################################################
# HOME PAGE
######################################################################
@app.route("/")
def index():
    return render_template('index.html')

######################################################################
# DATA TABLE AND TABLEAU 
######################################################################
@app.route("/data")
def data():
    health = pd.read_csv("static/data/health.csv")
    health_html = health.to_html().replace('\n', '')
    per_person = pd.read_csv("static/data/per_person.csv")
    person_html = per_person.to_html().replace('\n', '')
    return render_template("data.html", health_index=health_html, person_index=person_html)

######################################################################
# EAT YOUR WAY TO HEALTH - FOOD API
######################################################################

from config import api

base_url="https://nutridigm-api-dev.azurewebsites.net"
consume="/api/v1/nutridigm/topitemstoconsume?"
avoid="/api/v1/nutridigm/topitemstoavoid?"

problemId = 6

query_consume=base_url + consume + f'subscriptionId={api}&problemId={problemId}&api_key={api}'

query_avoid=base_url + avoid + f'subscriptionId={api}&problemId={problemId}&api_key={api}'

@app.route("/health")
def food():
    
    consume_food = requests.get(query_consume).json()
    avoid_food= requests.get(query_avoid).json()
    print(consume_food)
    print(avoid_food)
    return render_template('health.html', consume_html=consume_food, avoid_html=avoid_food)

# @app.route("/avoid")
# def avoid():
#     return avoid_food()

if __name__=='__main__':
    app.run(debug=True)
