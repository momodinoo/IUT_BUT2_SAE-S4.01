from flask import Flask, render_template
from flask_cors import CORS

from assets.py.backend.service.surveyService import *

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world2():
    return mean_age_by_aliment_types()
