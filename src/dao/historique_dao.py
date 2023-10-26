from typing import List, Optional
from utils.singleton import Singleton
from dao.db_connection import DBConnection


class HistoriqueDAO(metaclass=Singleton):
    def afficher_historique_utilisateur(self, utilisateur):
        identifiant_personne = utilisateur.identifiant_personne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Select *             "
                    'FROM "Projet_Info".page_visitee'
                    "WHERE identifiant_personne = %(identifiant_personne)s;",
                    {"identifiant_personne": identifiant_personne},
                )
                res = cursor.fetchall()
            return res

    def importer_historique(self, utilisateur):
        with open("data/importerHistorique.txt", "r") as f:
            next(f)  # Ignorer la première ligne si elle contient les en-têtes
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    for line in f:
                        data = line.strip().split(
                            ","
                        )  # Supposer que le CSV est délimité par des virgules
                        # Assurez-vous que l'identifiant de l'utilisateur est utilisé pour l'insertion
                        sql = """INSERT INTO "Projet_Info".page_visitee (date_visite, URL_page, identifiant_personne)
                                VALUES (%s, %s, %s);"""
                        cursor.execute(
                            sql, (data[0], data[1], utilisateur.identifiant_personne)
                        )

    def exporter_historique(self, utilisateur):
        identifiant_personne = utilisateur.identifiant_personne
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT *
                    FROM "Projet_Info".page_visitee
                    WHERE identifiant_personne = %(identifiant_personne)s""",
                    {"identifiant_personne": identifiant_personne},
                )
                res = cursor.fetchall()
                with open("data/exporterHistorique.txt", "w", newline="") as f:
                    if f.tell() == 0:
                        # Écrire le header seulement si le fichier est vide
                        header = [
                            "Identifiant_page",
                            "date_visite",
                            "URL_page",
                            "identifiant_personne",
                        ]
                        f.write(",".join(header) + "\n")
                    # Écrire les données
                    for row in res:
                        # Extraire les données de chaque ligne sous forme de dictionnaire
                        row_data = [
                            str(row["identifiant_page"]),
                            str(row["date_visite"]),
                            row["url_page"],
                            str(row["identifiant_personne"]),
                        ]
                        f.write(",".join(row_data) + "\n")


########### il manque la fonction supprimer historique ###########
