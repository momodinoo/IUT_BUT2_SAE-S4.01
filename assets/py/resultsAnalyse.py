import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

config = {
    'user': 'freedb_momododo',
    'password': 'unfw7W@2%K%thrT',
    'host': 'sql.freedb.tech',
    'database': 'freedb_momododo',
    'port': '3306',
    'raise_on_warnings': True
}

try:
    connect = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    exit()

cursor = connect.cursor()

"""req = ("SELECT * FROM sondage")
curseur.execute(req)
result = curseur.fetchall()

for l in result:
    print(l)

# ============== #

curseur = connect.cursor()

req = "SELECT type_aliment, COUNT(*) FROM sondage GROUP BY type_aliment"
curseur.execute(req)
result = curseur.fetchall()

data = {}
for l in result:
    data[l[0]] = l[1]

fig, ax = plt.subplots()
ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
ax.set_title("Répartition des types d'aliments dans le sondage")

plt.show()

# ============== #

cursor = connect.cursor()

req = "SELECT type_aliment, age, COUNT(*) FROM sondage GROUP BY type_aliment, age ORDER BY age DESC"
cursor.execute(req)
result = cursor.fetchall()

data = {}
for l in result:
    if l[1] not in data:
        data[l[1]] = {}
    data[l[1]][l[0]] = l[2]

for age_group in data:
    fig, ax = plt.subplots()
    ax.pie(data[age_group].values(), labels=data[age_group].keys(), autopct='%1.1f%%')
    ax.set_title(f"Répartition des types d'aliments dans le sondage (âge: {age_group})")

    plt.show()

# ============== #

cursor = connect.cursor()

req = (
    "SELECT type_aliment, niveau_enseignement, COUNT(*) FROM sondage GROUP BY type_aliment, niveau_enseignement ORDER BY niveau_enseignement ASC")
cursor.execute(req)
result = cursor.fetchall()

data = {}
for l in result:
    if l[1] not in data:
        data[l[1]] = {}
    data[l[1]][l[0]] = l[2]

for niveau_enseignement in data:
    fig, ax = plt.subplots()
    ax.pie(data[niveau_enseignement].values(), labels=data[niveau_enseignement].keys(), autopct='%1.1f%%')
    ax.set_title(f"Répartition des types d'aliments dans le sondage (niveau enseignement: {niveau_enseignement})")

    plt.show()

# ============== #

cursor = connect.cursor()

req = (
    "SELECT type_aliment, moment_journee, COUNT(*) FROM sondage GROUP BY type_aliment, moment_journee ORDER BY moment_journee ASC")
cursor.execute(req)
result = cursor.fetchall()

data = {}
for l in result:
    if l[1] not in data:
        data[l[1]] = {}
    data[l[1]][l[0]] = l[2]

for moment_journee in data:
    fig, ax = plt.subplots()
    ax.pie(data[moment_journee].values(), labels=data[moment_journee].keys(), autopct='%1.1f%%')
    ax.set_title(f"Répartition des types d'aliments dans le sondage (moment de la journee: {moment_journee})")

    plt.show()

# ============== #

cursor = connect.cursor()

req = (
    "SELECT type_aliment, moment_journee, niveau_enseignement, COUNT(*) FROM sondage GROUP BY type_aliment, moment_journee, niveau_enseignement ORDER BY moment_journee, niveau_enseignement ASC")
cursor.execute(req)
result = cursor.fetchall()

data = {}
for l in result:
    if l[1] not in data:
        data[l[1]] = {}
    if l[2] not in data[l[1]]:
        data[l[1]][l[2]] = {}
    data[l[1]][l[2]][l[0]] = l[3]

for moment_journee in data:
    for niveau_enseignement in data[moment_journee]:
        fig, ax = plt.subplots()
        ax.pie(data[moment_journee][niveau_enseignement].values(),
               labels=data[moment_journee][niveau_enseignement].keys(), autopct='%1.1f%%')
        ax.set_title(
            f"Répartition des types d'aliments dans le sondage (moment de la journée: {moment_journee}, niveau d'enseignement: {niveau_enseignement})")

# ============= #

cursor = connect.cursor()

req = ("SELECT aliment, COUNT(*) FROM sondage GROUP BY aliment")
cursor.execute(req)
result = cursor.fetchall()

data = {}
for l in result:
    data[l[0]] = l[1]

fig, ax = plt.subplots()
ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
ax.set_title("Répartition des aliments dans le sondage")

plt.show()

# ============= #

cursor = connect.cursor()

req = ("SELECT aliment, moment_journee, COUNT(*) FROM sondage GROUP BY aliment, moment_journee ORDER BY moment_journee ASC")
cursor.execute(req)
result = cursor.fetchall()

data = {}
for l in result:
    if l[1] not in data:
        data[l[1]] = {}
    data[l[1]][l[0]] = l[2]

for moment_journee in data:
    fig, ax = plt.subplots()
    ax.pie(data[moment_journee].values(), labels=data[moment_journee].keys(), autopct='%1.1f%%')
    ax.set_title(f"Répartition des aliments dans le sondage (moment de la journee: {moment_journee})")

    plt.show()

# ============ #

cursor = connect.cursor()

req = ("SELECT type_aliment, AVG(age) FROM sondage GROUP BY type_aliment")
cursor.execute(req)
result = cursor.fetchall()

type_aliments = []
moyennes_ages = []

for row in result:
    type_aliments.append(row[0])
    moyennes_ages.append(row[1])

plt.bar(type_aliments, moyennes_ages)
plt.xlabel('Type d\'aliment')
plt.ylabel('Moyenne d\'âge')
plt.title('Moyenne d\'âge par type d\'aliment dans le sondage')
plt.show()


# ============= #
"""
cursor = connect.cursor()

req = ("SELECT age, AVG(CASE WHEN type_aliment = 'viandes, œufs, poissons et assimilés' THEN 1 ELSE 0 END) AS viandesEct,"
       "AVG(CASE WHEN type_aliment = 'produits sucrés' THEN 1 ELSE 0 END) AS sucree,"
       "AVG(CASE WHEN type_aliment = 'produits laitiers et assimilés' THEN 1 ELSE 0 END) AS laitiers,"
       "AVG(CASE WHEN type_aliment = 'pâtes diverses, produits céréaliers' THEN 1 ELSE 0 END) AS cereale,"
       "AVG(CASE WHEN type_aliment = 'matières grasses' THEN 1 ELSE 0 END) AS matièresGrasses,"
       "AVG(CASE WHEN type_aliment = 'glaces et sorbets' THEN 1 ELSE 0 END) AS glacesSorbets,"
       "AVG(CASE WHEN type_aliment = 'fruits, légumes, légumineuses et oléagineux' THEN 1 ELSE 0 END) AS fruitsLégumesLégumineusesOléagineux,"
       "AVG(CASE WHEN type_aliment = 'entrées et plats composés' THEN 1 ELSE 0 END) AS entréesPlatsComposés,"
       "AVG(CASE WHEN type_aliment = 'eaux et autres boissons' THEN 1 ELSE 0 END) AS eauxAutresBoissons,"
       "AVG(CASE WHEN type_aliment = 'aliments infantiles' THEN 1 ELSE 0 END) AS alimentsInfantiles,"
       "AVG(CASE WHEN type_aliment = 'aides culinaires et ingrédients divers' THEN 1 ELSE 0 END) AS aidesCulinairesIngrédientsDivers"
       " FROM sondage GROUP BY age ORDER BY age ASC")
cursor.execute(req)
result = cursor.fetchall()
types_aliments = [description[0] for description in cursor.description if description[0] != 'age']

n_groups = len(result)
means = [row[1:] for row in result]
age_labels = [row[0] for row in result]

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.05
opacity = 0.9
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:orange', 'tab:purple', 'tab:brown']

for i, aliment in enumerate(types_aliments):
    plt.bar(index + (i * bar_width), [row[i] for row in means], bar_width, alpha=opacity, color=colors[i % len(colors)], label=aliment)

plt.xlabel('Age')
plt.ylabel('Moyenne de fréquence de consommation')
plt.xticks(index + bar_width, age_labels)
plt.legend()

plt.tight_layout()
plt.show()