from flask import Blueprint
from backend.service.surveyService import \
    aliment_types_repartition, aliment_types_repartition_by_age, aliment_types_repartition_with_all_ages, \
    aliment_types_repartition_with_all_school_level, aliment_types_repartition_by_school_level, \
    aliment_types_repartition_by_moment, aliment_types_repartition_by_school_level_and_moment

repartition_blueprint = Blueprint('repartition', __name__)


@repartition_blueprint.get("/")
def repartition_home():
    return {
        "info": {
            "Description": "Information sur la répartition",
            "Groupe": "/repartition"
        },
    }


@repartition_blueprint.get("/all")
def get_aliment_type_repartition():
    return aliment_types_repartition()


@repartition_blueprint.get("/age/all")
def get_aliment_type_repartition_with_all_ages():
    return aliment_types_repartition_with_all_ages()


@repartition_blueprint.get("/age/<chosen_age>")
def get_aliment_type_repartition_by_age(chosen_age: int):
    return aliment_types_repartition_by_age(chosen_age)


@repartition_blueprint.get("/age/all")
def get_aliment_type_repartition_with_all_school_level():
    return aliment_types_repartition_with_all_school_level()


@repartition_blueprint.get("/school/<school_level>")
def get_aliment_type_repartition_by_school_level(school_level: str):
    return aliment_types_repartition_by_school_level(school_level)


@repartition_blueprint.get("/moment/<moment>")
def get_aliment_type_repartition_by_moment(moment: str):
    return aliment_types_repartition_by_moment(moment)


@repartition_blueprint.get("/<school_level>/<moment>")
def get_aliment_type_repartition_by_school_level_and_age(school_level: str, moment: str):
    return aliment_types_repartition_by_school_level_and_moment(school_level, moment)
