# import necessary libraries
import os
import pandas as pd
import numpy as np 

from flask_cors import CORS
from flask import Flask, jsonify, render_template, request
import pickle
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

data = pd.read_csv("cleanedData.csv") 


# Create a route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html")

# create the route for the page runs vs wins                 
@app.route("/runs", methods=['GET', 'POST'])
def runs():
 
    if request.method == 'POST':
        runsInput = request.form['runs']
        intRuns = int(runsInput)
        with open('runs_model_pickle', 'rb') as f:
            runModel = pickle.load(f)
        runPrediction = runModel.predict(intRuns)
        runsInt = int(runPrediction)
        return render_template('runs.html', input = runsInput, wins = runsInt)
    else:
        return render_template('runs.html')

@app.route("/runsScatterData")        
def runsPlotly():
    df = pd.read_csv('runsPlotData.csv')
    runsData = df.loc[:, ["R", "W", "yearID", "franchID"]]
    # Format the data to send as json

    runsData["yearTeam"] = runsData.franchID + " " + runsData.yearID.map(str)
    
    # for rows in runsData:
    data = {
    "Runs": runsData.R.values.tolist(),
    "Wins": runsData.W.values.tolist(),
    "Layout": runsData.yearTeam.values.tolist()
    }
    return jsonify(data)
    
@app.route("/homeruns", methods=['GET', 'POST'])
def homeruns():
 
    if request.method == 'POST':
        homerunsInput = request.form['homeruns']
        intRuns = int(homerunsInput)
        with open('home_runs_model_pickle', 'rb') as f:
            homerunModel = pickle.load(f)
        homerunPrediction = homerunModel.predict(intRuns)
        homerunsInt = int(homerunPrediction)
        return render_template('homeruns.html', input = homerunsInput, wins = homerunsInt)
    else:
        return render_template('homeruns.html')

@app.route("/homerunsScatterData")        
def homerunsPlotly():
    df = pd.read_csv('runsPlotData.csv')
    homerunsData = df.loc[:, ["HR", "W", "yearID", "franchID"]]
    # Format the data to send as json
    homerunsData["yearTeam"] = homerunsData.franchID + " " + homerunsData.yearID.map(str)

    # for rows in runsData:
    data = {
    "Homeruns": homerunsData.HR.values.tolist(),
    "Wins": homerunsData.W.values.tolist(),
    "Layout": homerunsData.yearTeam.values.tolist()
    }
    return jsonify(data)

@app.route("/ERA", methods=['GET', 'POST'])
def ERA():
 
    if request.method == 'POST':
        ERAInput = request.form['ERA']
        floatERA = float(ERAInput)
        with open('era_model_pickle', 'rb') as f:
            ERAModel = pickle.load(f)
        ERAPrediction = ERAModel.predict(floatERA)
        ERAInt = int(ERAPrediction)
        return render_template('ERA.html', input = ERAInput, wins = ERAInt)
    else:
        return render_template('ERA.html')

@app.route("/ERAScatterData")        
def ERAPlotly():
    df = pd.read_csv('runsPlotData.csv')
    ERAData = df.loc[:, ["ERA", "W", "yearID", "franchID"]]
    # Format the data to send as json
    ERAData["yearTeam"] = ERAData.franchID + " " + ERAData.yearID.map(str)

    # for rows in runsData:
    data = {
    "ERA": ERAData.ERA.values.tolist(),
    "Wins": ERAData.W.values.tolist(),
    "Layout": ERAData.yearTeam.values.tolist()
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5009)

  #  labelDict = {"Runs": runsData.R.values.tolist(), "Wins": runsData.W.values.tolist(), "Year": runsData.yearID.values.tolist(), "Franchise": runsData.franchID.values.tolist()} 
  #  labelDF = pd.DataFrame(labelDict)
  #  Label = labelDF.from_dict(labelDict)
    # "Label": runsData.values.tolist()