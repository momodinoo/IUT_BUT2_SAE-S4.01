from backend.model.database import Database

db = Database()
cursor = db.get_cursor()


def aliment_types_repartition():
    def generate_dict(list):
        [type_aliment, count] = list
        return {
            "type_aliment": type_aliment,
            "count": count
        }

    req = """
        SELECT type_aliment, COUNT(*) 
        FROM sondage 
        GROUP BY type_aliment
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_with_all_ages():
    def generate_dict(list):
        [type_aliment, age, count] = list
        return {
            "type_aliment": type_aliment,
            "age": age,
            "count": count
        }

    req = f"""
        SELECT type_aliment, age, COUNT(*) 
        FROM sondage
        GROUP BY type_aliment, age
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_by_age(chosen_age: int):
    def generate_dict(list):
        [type_aliment, count] = list
        return {
            "type_aliment": type_aliment,
            "count": count
        }

    req = f"""
        SELECT type_aliment, COUNT(*) 
        FROM sondage 
        WHERE age={chosen_age} 
        GROUP BY type_aliment
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_with_all_school_level():
    def generate_dict(list):
        [type_aliment, school_level, count] = list
        return {
            "type_aliment": type_aliment,
            "niveau_enseignement": school_level,
            "count": count
        }

    req = f"""
        SELECT type_aliment, niveau_enseignement, COUNT(*) 
        FROM sondage
        GROUP BY type_aliment, niveau_enseignement
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_by_school_level(school_level: str):
    """
    :param school_level: Must be **Collège** or **Lycée**
    """

    def generate_dict(list):
        [type_aliment, count] = list
        return {
            "type_aliment": type_aliment,
            "count": count
        }

    req = f"""
        SELECT type_aliment, COUNT(*) 
        FROM sondage 
        WHERE niveau_enseignement = {school_level}
        GROUP BY type_aliment
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_by_moment(chosen_moment: str):
    """
    :param chosen_moment: Must be **Matin** or **Soir**
    """

    def generate_dict(list):
        [type_aliment, count] = list
        return {
            "type_aliment": type_aliment,
            "count": count
        }

    req = f"""
        SELECT type_aliment, COUNT(*)
        FROM sondage
        WHERE moment_journee = {chosen_moment}
        GROUP BY type_aliment
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_by_school_level_and_moment(school_level: str, chosen_moment: str):
    """
    :param school_level: Must be **Collège** or **Lycée**
    :param chosen_moment: Must be **Matin** or **Soir**
    """

    def generate_dict(list):
        [type_aliment, count] = list
        return {
            "type_aliment": type_aliment,
            "count": count
        }

    req = f"""
        SELECT type_aliment, COUNT(*)
        FROM sondage 
        WHERE (niveau_enseignement = {school_level} AND moment_journee = {chosen_moment})
        GROUP BY type_aliment
    """

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

    req = """
        SELECT aliment, COUNT(*) AS nombre
        FROM sondage 
        GROUP BY aliment 
        ORDER BY nombre 
        DESC LIMIT 1
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))[0]


def most_age_participated():
    def generate_dict(list):
        [age, count] = list
        return {
            "age": age,
            "count": count
        }

    req = """
        SELECT age, COUNT(*) AS nombre
        FROM sondage 
        GROUP BY age 
        ORDER BY nombre 
        DESC LIMIT 1
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))[0]


def most_school_level_participated():
    def generate_dict(list):
        [school_level, count] = list
        return {
            "niveau_enseignement": school_level,
            "count": count
        }

    req = """
        SELECT niveau_enseignement, COUNT(*) AS nombre
        FROM sondage 
        GROUP BY niveau_enseignement 
        ORDER BY nombre 
        DESC LIMIT 1
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))[0]


def mean_age_by_aliment_types():
    def generate_dict(list):
        [type_aliment, mean] = list
        return {
            "type_aliment": type_aliment,
            "mean": mean
        }

    req = """
        SELECT type_aliment, AVG(age)
        FROM sondage 
        GROUP BY type_aliment
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def mean_kcal():
    kcal_table_name = "Energie, Règlement UE N° 1169/2011 (kcal/100 g)"

    req = f"""
        SELECT AVG(`{kcal_table_name}`) 
        FROM sondage 
            INNER JOIN aliments ON aliments.alim_nom_fr = sondage.aliment 
        WHERE `{kcal_table_name}` <> '-'
    """

    cursor.execute(req)
    result = cursor.fetchall()
    return {
        "mean": result[0][0]
    }
