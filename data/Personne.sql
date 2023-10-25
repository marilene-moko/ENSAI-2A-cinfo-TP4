import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    email="email",
    nom="nom",
    prenom="prenom",
    mdp="mdp"
    profil="profil"
)

cursor = connection.cursor()

insert_query = "INSERT INTO Utilisateurs (nom, prenom, email, mot_de_passe, profil) VALUES (%s, %s, %s, %s, %s)"
user_data = ("John", "Doe", "johndoe@example.com", "mot_de_passe_hache", "eleve")

cursor.execute(insert_query, user_data)

connection.commit()

cursor.close()
connection.close()
