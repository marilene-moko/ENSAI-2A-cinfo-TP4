<<<<<<< HEAD
import mysql.connector
import bcrypt


# Hacher le mdp

mot_de_passe_hache = bcrypt.hashpw(mot_de_passe.encode('utf-8'), bcrypt.gensalt())

connection = mysql.connector.connect(
    host="localhost",
    email="email",
    nom="nom",
    prenom="prenom",
    mdp="mdp"
    profil="profil"
)

cursor = connection.cursor()

insert_query = "INSERT INTO Utilisateurs (email, nom, prenom, mdp, profil) VALUES (%s, %s, %s, %s, %s)"
user_data = ("John", "Doe", "johndoe@example.com", "mot_de_passe_hache", "eleve")

cursor.execute(insert_query, user_data)

connection.commit()

cursor.close()
connection.close()
=======
INSERT INTO "Projet_Info".personne(nom, prenom, adresse_mail, mot_de_passe, statut) VALUES
('Mathieu','Maude','maude.mathieu@gmail.com','MaUdE123456','administrateur'),
('Mounier','Clément','clement.mounier@gmail.com','ClEmEnT987654321','administrateur'),
('Heidsieck', 'Suzanne','suzanne.heidsieck@gmail.com','Susudu35','administrateur'),
('Kougoum Moko Mani','Marilene','marilene.kougoum-moko-mani@gmail.com','RiRidu35000','administrateur'),
('Boubet','Sophie','sophie.boubet@gmail.com','SoPhIe35','administrateur'),
('Bouzeria','Abdel','abdel.bouzeria@gmail.com','Abdel98765432100','professeur'),
('Riviere','Leana','leana.riviere@gmail.com','JadoreLH2O','professeur'),
('Zitoun','Sarah','sarah.zitoun@gmail.com','SAsaSAsa94','professeur'),
('Defour','Vincent','vincent.defour@gmail.com','CupCake35','professeur'),
('Funaer','Catherine','catherine.funaer@gmail.com','CHaCHabada93','professeur'),
('Dupont','Kevin','kevin.dupont@gmail.com','Kev35','utilisateur'),
('Dupont', 'Nathalie', 'nathalie.dupont@gmail.com','Jdetestelamusique35','utilisateur'),
('Zaza','Jacob','jacob.zaza@gmail.com','1235Jac','utilisateur'),
('Elkarif','Abdelraouf','abdelraouf.elkarif@gmail.com','Karirif35','utilisateur'),
('Carofil','Mathieu','mathieu.carofil@gmail.com','JusteDance75','utilisateur'),
('Gewoncik','Zuzana','zuzana.gewoncik@gmail.com','Gege75','utilisateur');
>>>>>>> 34e21df1d7b1631123fd8ecfb4b696613df3ca1f
