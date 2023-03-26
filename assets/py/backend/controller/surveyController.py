from flask import Flask, render_template
from flask_cors import CORS

from assets.py.backend.service.surveyService import *

app = Flask(__name__)
CORS(app)


@app.route("/aliment_types_repartition")
def getResults1():
    return aliment_types_repartition()


@app.route("/most_ate_aliment")
def getResults2():
    return most_ate_aliment()


@app.route("/mean_age_by_aliment_types")
def getResults3():
    return mean_age_by_aliment_types()


@app.route("/mean_kcal")
def getResults4():
    return mean_kcal()
