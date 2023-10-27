from typing import List, Optional
from utils.singleton import Singleton
from dao.db_connection import DBConnection


class HistoriqueDAO(metaclass=Singleton):
    def afficher_historique_utilisateur(self, adresse_mail):
        """
        Affiche l'historique d'un utilisateur
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Select *             "
                    'FROM "Projet_Info".page_visitee'
                    "WHERE adresse_mail = %(adresse_mail)s;",
                    {"adresse_mail": adresse_mail},
                )
                res = cursor.fetchall()
            return res

    def importer_historique(self, adresse_mail):
        """
        Importe un historique aux entêtes date_visite,URL_page,identifiant_personne

        L'importation se fait nécessairement d'un fichier nommé "importHistorique" situé
        dans le dosser data.
        L'utilisateur qui importe ne peut importer des lignes d'historiques que pour son id
        """

        with open("data/importerHistorique.txt", "r") as f:
            next(f)  # Ignorer la première ligne si elle contient les en-têtes
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    for line in f:
                        data = line.strip().split(
                            ","
                        )  # Supposer que le CSV est délimité par des virgules
                        # Assurez-vous que l'identifiant de l'utilisateur est utilisé pour l'insertion
                        sql = """INSERT INTO "Projet_Info".page_visitee (date_visite, URL_page, adresse_mail)
                                VALUES (%s, %s, %s);"""
                        cursor.execute(sql, (data[0], data[1], adresse_mail))

    def exporter_historique(self, adresse_mail):
        """
        Exporter un historique

        L'exportation se fait en envoyés dans un ficher "exporterHistorique"
        L'utilisateur qui exporte ne peut exporter que SON historique
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT *
                    FROM "Projet_Info".page_visitee
                    WHERE adresse_mail = %(adresse_mail)s""",
                    {"adresse_mail": adresse_mail},
                )
                res = cursor.fetchall()
                with open("data/exporterHistorique.txt", "w", newline="") as f:
                    if f.tell() == 0:
                        # Écrire le header seulement si le fichier est vide
                        header = [
                            "Identifiant_page",
                            "date_visite",
                            "URL_page",
                            "adresse_mail",
                        ]
                        f.write(",".join(header) + "\n")
                    # Écrire les données
                    for row in res:
                        # Extraire les données de chaque ligne sous forme de dictionnaire
                        row_data = [
                            str(row["identifiant_page"]),
                            str(row["date_visite"]),
                            row["url_page"],
                            str(row["adresse_mail"]),
                        ]
                        f.write(",".join(row_data) + "\n")

    def supprimer_historique_utilisateur(self, adresse_mail):
        """
        Supprime l'historique d'un utilisateur
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'DELETE FROM "Projet_Info".page_visitee '
                    "WHERE adresse_mail = %(adresse_mail)s;",
                    {"adresse_mail": adresse_mail},
                )
