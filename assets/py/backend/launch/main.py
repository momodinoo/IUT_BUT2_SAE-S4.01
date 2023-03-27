from flask import Flask
from flask_cors import CORS
from controller.surveyController import main_blueprint

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5000

app = Flask(__name__, template_folder="templates")
app.register_blueprint(main_blueprint)
CORS(app)

if __name__ == "__main__":
    app.run(SERVER_IP, SERVER_PORT)

