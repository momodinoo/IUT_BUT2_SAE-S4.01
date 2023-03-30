from flask import Blueprint

from service.surveyService import most_ate_aliment, most_age_participated, most_school_level_participated, most_count_participated

most_blueprint = Blueprint('most', __name__)


@most_blueprint.get("/")
def repartition_home():
    return {
        "info": {
            "Description": "Information sur les maximums (le plus)",
            "Groupe": "/most"
        },
    }


@most_blueprint.get("/aliment")
def get_most_ate_aliment():
    return most_ate_aliment()


@most_blueprint.get("/age")
def get_most_age_participated():
    return most_age_participated()


@most_blueprint.get("/school")
def get_most_school_level_participated():
    return most_school_level_participated()

@most_blueprint.get("/count")
def get_mort_count_participated():
    return most_count_participated();