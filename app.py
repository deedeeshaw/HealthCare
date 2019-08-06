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
    data_df = pd.read_csv("static/data/health.csv")
    data = data_df.rename(columns={'All_persons': 'Total', 
        'Less_than_high_school': '< High School', 'High_school': "High Schhol",
        'Some_college': 'Some College', "Less_than_18": "Still in School",
        "Excellent_health": "Excellent Health",
        "VG_health": "Very Good Health", "Good_health": "Good Health",
         "Fair_health": "Fair Health", "Poor_health": "Poor Health"})
    data.set_index("Year", inplace=True)
    data = data.applymap('{:,}'.format)
    data_html = data.to_html().replace('\n', '')
  
    per_person_df = pd.read_csv("static/data/per_person.csv")
    per_person = per_person_df.rename(columns={'Per_person': 'Total per Person', 'per_Male': "Male", 'per_Female': "Female",
                    'per_Less_than_high_school': '< High School', 'per_High_school': "High Schhol",
                      'per_Some_college': 'Some College', "per_Less_than_18": "Still in School",
                        "per_Excellent_health": "Excellent Health",
                      "per_VG_health": "Very Good Health", "per_Good_health": "Good Health", "per_Fair_health": "Fair Health",
                      "per_Poor_health": "Poor Health"})
    per_person.set_index("Year", inplace=True)
    person_html = per_person.to_html().replace('\n', '')
   
    return render_template("data.html", data_index=data_html, person_index=person_html)

######################################################################
# EAT YOUR WAY TO HEALTH - FOOD API
######################################################################

from config import api

base_url="https://nutridigm-api-dev.azurewebsites.net"
consume_url="/api/v1/nutridigm/topitemstoconsume?"
avoid_url="/api/v1/nutridigm/topitemstoavoid?"

problemId = 3

query_consume=base_url + consume_url + f'subscriptionId={api}&problemId={problemId}&api_key={api}'

query_avoid=base_url + avoid_url + f'subscriptionId={api}&problemId={problemId}&api_key={api}'

@app.route("/health")
def food():
    consume_food = requests.get(query_consume).json()
    for c in consume_food:
        consume =c.split('; ')
    
    avoid_food= requests.get(query_avoid).json()
    for a in avoid_food:
        avoid=a.split('; ')
        # print(consume)
        # print(avoid)
        return render_template('health.html', consume_html=consume, avoid_html=avoid)


if __name__=='__main__':
    app.run(debug=True)
