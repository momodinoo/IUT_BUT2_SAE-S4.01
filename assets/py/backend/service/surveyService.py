from assets.py.backend.model.database import Database

db = Database()
cursor = db.get_cursor()


def aliment_types_repartition():
    def generate_dict(list):
        [type_aliment, count] = list
        return {
            "type_aliment": type_aliment,
            "count": count
        }

    req = "SELECT type_aliment, COUNT(*) FROM sondage GROUP BY type_aliment"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


# TODO filter pour chaque age ou quoi la team

def aliment_types_repartition_17():
    def generate_dict(list):
        [type_aliment, age, count] = list
        return {
            "type_aliment": type_aliment,
            "age": age,
            "count": count
        }

    req = "SELECT type_aliment, age, COUNT(*) FROM sondage WHERE age=17 GROUP BY type_aliment, age"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_12():
    def generate_dict(list):
        [type_aliment, age, count] = list
        return {
            "type_aliment": type_aliment,
            "age": age,
            "count": count
        }

    req = "SELECT type_aliment, age, COUNT(*) FROM sondage WHERE age=12 GROUP BY type_aliment, age"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


# TODO faire une méthode + générale


def aliment_types_repartition_by_school_level_college():
    def generate_dict(list):
        [type_aliment, school_level, count] = list
        return {
            "type_aliment": type_aliment,
            "school_level": school_level,
            "count": count
        }

    req = "SELECT type_aliment, niveau_enseignement, COUNT(*) FROM sondage WHERE niveau_enseignement = 'Collège' " \
          "GROUP BY type_aliment, niveau_enseignement "
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_by_school_level_lycee():
    def generate_dict(list):
        [type_aliment, school_level, count] = list
        return {
            "type_aliment": type_aliment,
            "school_level": school_level,
            "count": count
        }

    req = "SELECT type_aliment, niveau_enseignement, COUNT(*) FROM sondage WHERE niveau_enseignement = 'Lycée' " \
          "GROUP BY type_aliment, niveau_enseignement "
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_by_moment_morning():
    def generate_dict(list):
        [type_aliment, moment, count] = list
        return {
            "type_aliment": type_aliment,
            "moment": moment,
            "count": count
        }

    req = "SELECT type_aliment, moment_journee, COUNT(*) FROM sondage WHERE moment_journee = 'Matin' " \
          "GROUP BY type_aliment, moment_journee"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_by_moment_evening():
    def generate_dict(list):
        [type_aliment, moment, count] = list
        return {
            "type_aliment": type_aliment,
            "moment": moment,
            "count": count
        }

    req = "SELECT type_aliment, moment_journee, COUNT(*) FROM sondage WHERE moment_journee = 'Soir' " \
          "GROUP BY type_aliment, moment_journee"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_in_college_evening():
    def generate_dict(list):
        [type_aliment, moment, niveau_enseignement, count] = list
        return {
            "type_aliment": type_aliment,
            "moment": moment,
            "niveau_enseignement": niveau_enseignement,
            "count": count
        }

    req = "SELECT type_aliment, moment_journee, niveau_enseignement, COUNT(*)" \
          "FROM sondage WHERE (niveau_enseignement = 'Collège' AND moment_journee = 'Soir') " \
          "GROUP BY type_aliment, moment_journee, niveau_enseignement"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_in_lycee_morning():
    def generate_dict(list):
        [type_aliment, moment, niveau_enseignement, count] = list
        return {
            "type_aliment": type_aliment,
            "moment": moment,
            "niveau_enseignement": niveau_enseignement,
            "count": count
        }

    req = "SELECT type_aliment, moment_journee, niveau_enseignement, COUNT(*)" \
          "FROM sondage WHERE (niveau_enseignement = 'Lycée' AND moment_journee = 'Matin') " \
          "GROUP BY type_aliment, moment_journee, niveau_enseignement"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def most_ate_aliment():
    def generate_dict(list):
        [type_aliment, count] = list
        return {
            "type_aliment": type_aliment,
            "count": count
        }

    req = "SELECT aliment, COUNT(*) AS nombre FROM sondage GROUP BY aliment ORDER BY nombre DESC LIMIT 1"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def mean_age_by_aliment_types():
    def generate_dict(list):
        [type_aliment, mean] = list
        return {
            "type_aliment": type_aliment,
            "mean": mean
        }

    req = "SELECT type_aliment, AVG(age) FROM sondage GROUP BY type_aliment"
    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def mean_kcal():
    req = "SELECT AVG(`Energie, Règlement UE N° 1169/2011 (kcal/100 g)`) FROM sondage INNER JOIN aliments ON " \
          "aliments.alim_nom_fr = sondage.aliment WHERE `Energie, Règlement UE N° 1169/2011 (kcal/100 g)` <> '-'"
    cursor.execute(req)
    result = cursor.fetchall()
    return result
