from typing import List, Optional
from utils.singleton import Singleton
from dao.db_connection import DBConnection


class ListeEnvieDAO(metaclass=Singleton):
    # def afficher_listeEnvie(self):
    # with DBConnection().connection as connection:
    # with connection.cursor() as cursor:
    # cursor.execute("Select *           " 'FROM "Projet_Info".voeu;')
    # res = cursor.fetcall()
    # return res

    def afficher_listeEnvie_utilisateur(self, utilisateur):
        identifiant_personne = utilisateur.identifiant_personne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Select *             "
                    'FROM "Projet_Info".voeu'
                    "WHERE identifiant_personne = %(identifiant_personne)s;",
                    {"identifiant_personne": identifiant_personne},
                )
                res = cursor.fetchall()
            return res

    def supprimer_listeEnvie_utilisateur(self, utilisateur, identifiant_voeu):
        identifiant_personne = utilisateur.identifiant_personne
        # Vérifier si le voeu appartient à l'utilisateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT identifiant_personne FROM "Projet_Info".voeu WHERE identifiant_voeu = %(identifiant_voeu)s;',
                    {"identifiant_voeu": identifiant_voeu},
                )
                row = cursor.fetchone()

        if row is None:
            # Le voeu n'existe pas
            return "Le voeu spécifié n'existe pas."

        identifiant_personne_voeu = row["identifiant_personne"]

        if identifiant_personne_voeu != utilisateur.identifiant_personne:
            # Le voeu n'appartient pas à l'utilisateur
            return "Ce voeu ne fait pas partie de la liste de l'utilisateur."

        # Supprimer le voeu de la table "voeu"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'DELETE FROM "Projet_Info".voeu WHERE identifiant_voeu = %(identifiant_voeu)s;',
                    {"identifiant_voeu": identifiant_voeu},
                )

        return "Le voeu a été supprimé avec succès."

    def ajouter_stage_listeEnvie_utilisateur(self, utilisateur, identifiant_stage):
        identifiant_personne = utilisateur.identifiant_personne
        # Vérifier si le stage existe et n'est pas déjà dans la liste d'envies de l'utilisateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Vérifier si le stage existe
                cursor.execute(
                    'SELECT * FROM "Projet_Info".stage WHERE identifiant_stage = %(identifiant_stage)s;',
                    {"identifiant_stage": identifiant_stage},
                )
                stage = cursor.fetchone()

                if stage is None:
                    return "Le stage spécifié n'existe pas."

                # Vérifier si le stage est déjà dans la liste d'envies de l'utilisateur
                cursor.execute(
                    'SELECT * FROM "Projet_Info".voeu WHERE identifiant_personne = %(identifiant_personne)s AND identifiant_stage = %(identifiant_stage)s;',
                    {
                        "identifiant_personne": utilisateur.identifiant_personne,
                        "identifiant_stage": identifiant_stage,
                    },
                )
                existing_entry = cursor.fetchone()

                if existing_entry:
                    return "Le stage est déjà dans la liste d'envies de l'utilisateur."

                # Ajouter le stage à la liste d'envies de l'utilisateur
                cursor.execute(
                    'INSERT INTO "Projet_Info".voeu (identifiant_personne, identifiant_stage)'
                    "VALUES (%(identifiant_personne)s, %(identifiant_stage)s);",
                    {
                        "identifiant_personne": utilisateur.identifiant_personne,
                        "identifiant_stage": identifiant_stage,
                    },
                )

        return "Le stage a été ajouté à la liste d'envies de l'utilisateur."

    def importer_voeux(self, utilisateur):
        with open("data/importerVoeux.txt", "r") as f:
            next(f)  # Ignorer la première ligne si elle contient les en-têtes
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    for line in f:
                        data = line.strip().split(
                            ","
                        )  # Supposer que le CSV est délimité par des virgules
                        # Assurez-vous que l'identifiant de l'utilisateur est utilisé pour l'insertion
                        sql = """INSERT INTO "Projet_Info".voeu (URL_voeu, Categorie, Intitule, Ville, Poste, Entreprise, identifiant_personne)
                                VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                        cursor.execute(
                            sql,
                            (
                                data[0],
                                data[1],
                                data[2],
                                data[3],
                                data[4],
                                data[5],
                                utilisateur.identifiant_personne,
                            ),
                        )

    def exporter_voeux(self, utilisateur):
        identifiant_personne = utilisateur.identifiant_personne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT *
                    FROM "Projet_Info".voeu
                    WHERE identifiant_personne = %(identifiant_personne)s""",
                    {"identifiant_personne": identifiant_personne},
                )
                res = cursor.fetchall()
                with open("data/exporterVoeux.csv", "w", newline="") as f:
                    if f.tell() == 0:
                        # Écrire le header seulement si le fichier est vide
                        header = [
                            "identifiant_voeu",
                            "URL_voeu",
                            "Categorie",
                            "Intitule",
                            "Ville",
                            "Poste",
                            "Entreprise",
                            "identifiant_personne",
                        ]
                        f.write(",".join(header) + "\n")
                    # Écrire les données
                    for row in res:
                        row_data = [
                            str(row["identifiant_voeu"]),
                            row["URL_voeu"],
                            row["Categorie"],
                            row["Intitule"],
                            row["Ville"],
                            row["Poste"],
                            row["Entreprise"],
                            str(row["identifiant_personne"]),
                        ]
                        f.write(",".join(row_data) + "\n")
