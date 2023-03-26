from flask import Blueprint

from backend.service.surveyService import mean_age_by_aliment_types, mean_kcal

mean_blueprint = Blueprint('mean', __name__)


@mean_blueprint.get("/")
def repartition_home():
    return {
        "info": {
            "Description": "Information sur la moyenne",
            "Groupe": "/mean"
        },
    }


@mean_blueprint.get("/age")
def get_mean_age_by_aliment_type():
    return mean_age_by_aliment_types()


@mean_blueprint.get("/kcal")
def get_mean_kcal():
    return mean_kcal()
