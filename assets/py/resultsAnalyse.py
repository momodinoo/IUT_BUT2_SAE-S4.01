pip install mysql-connector-python

import mysql.connector
import matplotlib.pyplot as plt

config = {
    'host' : 'sql.freedb.tech',
    'database' : 'freedb_momododo',
    'user' : 'freedb_momododo',
    'password' : 'unfw7W@2%K%thrT',
    'port' : '3306',
    'raise_on_warnings' : True
}

try:
    connect = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    exit()
curseur = connect.cursor()

req = ("SELECT * FROM sondage")
curseur.execute(req)
result = curseur.fetchall()

for l in result:
    print(l)


config = {
    'user' : 'freedb_momododo',
    'password' : 'unfw7W@2%K%thrT',
    'host' : 'sql.freedb.tech',
    'database' : 'freedb_momododo',
    'port' : '3306',
    'raise_on_warnings' : True
}

try:
    connect = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    exit()
curseur = connect.cursor()

req = ("SELECT type_aliment, COUNT(*) FROM sondage GROUP BY type_aliment")
curseur.execute(req)
result = curseur.fetchall()

data = {}
for l in result:
    data[l[0]] = l[1]

fig, ax = plt.subplots()
ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
ax.set_title("Répartition des types d'aliments dans le sondage")

plt.show()











config = {
    'user' : 'freedb_momododo',
    'password' : 'unfw7W@2%K%thrT',
    'host' : 'sql.freedb.tech',
    'database' : 'freedb_momododo',
    'port' : '3306',
    'raise_on_warnings' : True
}

try:
    connect = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    exit()
curseur = connect.cursor()

req = ("SELECT type_aliment, age, COUNT(*) FROM sondage GROUP BY type_aliment, age ORDER BY age ASC")
curseur.execute(req)
result = curseur.fetchall()

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









config = {
    'user' : 'freedb_momododo',
    'password' : 'unfw7W@2%K%thrT',
    'host' : 'sql.freedb.tech',
    'database' : 'freedb_momododo',
    'port' : '3306',
    'raise_on_warnings' : True
}

try:
    connect = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    exit()
curseur = connect.cursor()

req = ("SELECT type_aliment, niveau_enseignement, COUNT(*) FROM sondage GROUP BY type_aliment, niveau_enseignement ORDER BY niveau_enseignement ASC")
curseur.execute(req)
result = curseur.fetchall()

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












config = {
    'user' : 'freedb_momododo',
    'password' : 'unfw7W@2%K%thrT',
    'host' : 'sql.freedb.tech',
    'database' : 'freedb_momododo',
    'port' : '3306',
    'raise_on_warnings' : True
}

try:
    connect = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    exit()
curseur = connect.cursor()

req = ("SELECT type_aliment, moment_journee, COUNT(*) FROM sondage GROUP BY type_aliment, moment_journee ORDER BY moment_journee ASC")
curseur.execute(req)
result = curseur.fetchall()

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















config = {
    'user' : 'freedb_momododo',
    'password' : 'unfw7W@2%K%thrT',
    'host' : 'sql.freedb.tech',
    'database' : 'freedb_momododo',
    'port' : '3306',
    'raise_on_warnings' : True
}

try:
    connect = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    print(err)
    exit()
curseur = connect.cursor()

req = ("SELECT type_aliment, moment_journee, niveau_enseignement, COUNT(*) FROM sondage GROUP BY type_aliment, moment_journee, niveau_enseignement ORDER BY moment_journee, niveau_enseignement ASC")
curseur.execute(req)
result = curseur.fetchall()

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
        ax.pie(data[moment_journee][niveau_enseignement].values(), labels=data[moment_journee][niveau_enseignement].keys(), autopct='%1.1f%%')
        ax.set_title(f"Répartition des types d'aliments dans le sondage (moment de la journée: {moment_journee}, niveau d'enseignement: {niveau_enseignement})")
