# TODO create methods to manage result data (in Database)
from assets.py.backend.model.database import Database

db = Database()
cursor = db.get_cursor()


def req1():
    def generate_dict(list):
        [id, age, level, time, category, aliment] = list
        return {
            "id": id,
            "age": age,
            "level": level,
            "time": time,
            "category": category,
            "aliment": aliment
        }

    req = "SELECT * FROM sondage"
    cursor.execute(req)
    result = cursor.fetchall()

    return list(map(generate_dict, result))
