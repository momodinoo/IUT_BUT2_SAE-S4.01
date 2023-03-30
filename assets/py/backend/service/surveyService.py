from statistics import mean

from model.database import Database

db = Database()


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

    cursor = db.query(req)
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

    def get_age_index_array(array: list, age: int):
        for i in range(len(array)):
            element = array[i]
            if element["age"] == age:
                return i
        return -1

    def get_age(element):
        return element["age"]

    req = f"""
        SELECT type_aliment, age, COUNT(*) 
        FROM sondage
        GROUP BY type_aliment, age
    """

    cursor = db.query(req)
    result = cursor.fetchall()
    result = list(map(generate_dict, result))
    to_return = []
    for e in result:
        index = get_age_index_array(to_return, e["age"])
        data_to_add = {
            "type_aliment": e["type_aliment"],
            "count": e["count"]
        }
        if index == -1:
            to_return.append({
                "age": e["age"],
                "data": [data_to_add]
            })
        else:
            to_return[index]["data"].append(data_to_add)

    to_return.sort(key=get_age)

    return to_return


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

    cursor = db.query(req)
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

    cursor = db.query(req)
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

    cursor = db.query(req)
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

    cursor = db.query(req)
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

    cursor = db.query(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def aliment_types_repartition_with_school_level_and_moment():
    def generate_dict(list):
        [type_aliment, school_level, moment, count] = list
        return {
            "type_aliment": type_aliment,
            "niveau_enseignement": school_level,
            "moment": moment,
            "count": count
        }

    req = f"""
        SELECT type_aliment, niveau_enseignement, moment_journee, COUNT(*)
        FROM sondage
        GROUP BY type_aliment, niveau_enseignement, moment_journee
    """

    cursor = db.query(req)
    result = cursor.fetchall()
    result = list(map(generate_dict, result))

    to_return = [
        {
            "school_level": "Lycée",
            "morning": [],
            "evening": [],
        },
        {
            "school_level": "Collège",
            "morning": [],
            "evening": [],
        }
    ]

    for e in result:
        data_to_add = {
            "type_aliment": e["type_aliment"],
            "count": e["count"]
        }

        to_append = to_return[0]

        if e["niveau_enseignement"] == "Collège":
            to_append = to_return[1]

        if e["moment"] == "Matin":
            to_append["morning"].append(data_to_add)
        else:
            to_append["evening"].append(data_to_add)

    return to_return


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

    cursor = db.query(req)
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

    cursor = db.query(req)
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

    cursor = db.query(req)
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

    cursor = db.query(req)
    result = cursor.fetchall()
    return list(map(generate_dict, result))


def mean_kcal():
    kcal_table_name = "Energie, Règlement UE N° 1169/2011 (kcal/100 g)"

    def get_kcal_value(element):
        return element[0]

    def remove_empty_value(element):
        return element != '-' and element != ''

    def replace_comma(element):
        return element.replace(',', '.')

    def set_values_to_float(element):
        return float(element)

    req = f"""
        SELECT `{kcal_table_name}`
        FROM sondage 
            INNER JOIN aliments ON aliments.alim_nom_fr = sondage.aliment 
    """

    cursor = db.query(req)
    result = cursor.fetchall()
    raw_values = list(map(get_kcal_value, result))
    values = filter(remove_empty_value, raw_values)
    cleaned_values = list(map(replace_comma, values))
    int_values = list(map(set_values_to_float, cleaned_values))


    return {
        "mean": round(mean(int_values), 2)
    }
