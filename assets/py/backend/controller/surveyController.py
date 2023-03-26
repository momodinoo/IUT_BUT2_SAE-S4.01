from flask import Blueprint
from backend.controller.blueprints.repartitionController import repartition_blueprint
from backend.controller.blueprints.meanController import mean_blueprint
from backend.controller.blueprints.mostController import most_blueprint

main_blueprint = Blueprint('main', __name__)
main_blueprint.register_blueprint(repartition_blueprint, url_prefix='/repartition')
main_blueprint.register_blueprint(mean_blueprint, url_prefix='/mean')
main_blueprint.register_blueprint(most_blueprint, url_prefix='/most')


@main_blueprint.get("/")
def welcome():
    # return render_template('welcome.html') //TODO welcome page ? (Extra-feature)
    return {
        "message": "Welcome ! API Works"
    }
