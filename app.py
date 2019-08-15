######################################################################
# IMPORT FLASK AND OTHER DEFECIENCIS
######################################################################
from flask import Flask, render_template, request
# , redirect, jsonify
from data import data_table, perperson_table
from health import problem_dd

######################################################################
# create app passing the __name__
######################################################################
app = Flask(__name__)

######################################################################
# HOME PAGE
######################################################################
@app.route("/")
def index():
    return render_template('indexB.html')

######################################################################
# DATA TABLE AND TABLEAU 
######################################################################
@app.route("/data")
def data():
    
    return render_template("data.html", data_index=data_table(), person_index=perperson_table())
  
######################################################################
# EAT YOUR WAY TO HEALTH - FOOD API
######################################################################

@app.route("/health")
def health():
        
        return render_template('health.html', problem_html=problem_dd())


if __name__=='__main__':
    app.run(debug=True)
