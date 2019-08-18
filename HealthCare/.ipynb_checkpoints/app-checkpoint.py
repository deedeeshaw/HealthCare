######################################################################
# IMPORT FLASK
######################################################################
from flask import Flask, render_template, request, redirect, jsonify
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
    health = pd.read_csv("static/data/Big_Cities_Health_Data_Inventory.csv")
    health_html = health.head(100).to_html().replace('\n', '')
    return render_template("index.html", health_index=health_html)



if __name__=='__main__':
    app.run(debug=True)
