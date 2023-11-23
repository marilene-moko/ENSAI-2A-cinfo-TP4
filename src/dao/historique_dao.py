from utils.singleton import Singleton
from dao.db_connection import DBConnection
import datetime


class HistoriqueDAO(metaclass=Singleton):
    @staticmethod
    def afficher_historique_utilisateur(adresse_mail):
        """
        Affiche l'historique d'un utilisateur

        Paramètre:
            adresse_mail : str : l'adresse mail de l'utilisateur

        Retour :
            l'historique
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT * FROM "Projet_Info".page_visitee '
                    "WHERE adresse_mail = %(adresse_mail)s;",
                    {"adresse_mail": adresse_mail},
                )
                res = cursor.fetchall()
            return res

    @staticmethod
    def importer_historique(adresse_mail):
        """
        Importe un historique aux entêtes date_visite,URL_page,adresse_mail

        L'importation se fait nécessairement d'un fichier nommé "importHistorique" situé
        dans le dossier data.
        L'utilisateur qui importe ne peut importer des lignes d'historiques que pour son id

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'import

        Retour :
            un booléen qui indique si la tâche a bien été effectuée
        """
        try:
            with open("data/importerHistorique.txt", "r") as f:
                next(f)  # Ignorer la première ligne si elle contient les en-têtes
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        for line in f:
                            data = line.strip().split(
                                ","
                            )  # Supposer que le CSV est délimité par des virgules
                            # Assurez-vous que l'identifiant de l'utilisateur est utilisé pour l'insertion
                            sql = """INSERT INTO "Projet_Info".page_visitee (date_visite, URL_page, titre, adresse_mail)
                                    VALUES (%s, %s, %s, %s);"""
                            cursor.execute(
                                sql, (data[0], data[1], data[2], adresse_mail)
                            )
            return True  # L'importation a réussi
        except Exception as e:
            return False  # L'importation a échoué

    def importer_historique_modified(self, adresse_mail, stage):
        """
        On conserve les liens, des stages qui ont parcourus par les utilisateurs ainsi que les dates auxquelles ils ont été consultés.
        """
        try:
            now = datetime.datetime.now()
            date_f = now.strftime("%Y-%m-%d %H:%M:%S")

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Assurez-vous que l'identifiant de l'utilisateur est utilisé pour l'insertion
                    sql = """INSERT INTO "Projet_Info".page_visitee (date_visite, URL_page, titre , adresse_mail)
                            VALUES (%s, %s, %s,  %s);"""
                    cursor.execute(
                        sql, date_f, stage.URL_stage, stage.titre, adresse_mail
                    )
            return True  # L'importation a réussi
        except Exception:
            return False  # L'importation a échoué

    @staticmethod
    def exporter_historique(adresse_mail):
        """
        Exporter un historique

        L'exportation se fait en envoyés dans un fichier "exporterHistorique"
        L'utilisateur qui exporte ne peut exporter que SON historique

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'import

        Retour :
            un booléen qui indique si la tâche a bien été effectuée
        """
        try:
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
                                "titre",
                                "adresse_mail",
                            ]
                            f.write(",".join(header) + "\n")
                        # Écrire les données
                        for row in res:
                            row_data = [
                                str(row["identifiant_page"]),
                                str(row["date_visite"]),
                                str(row["titre"]),
                                row["url_page"],
                                str(row["adresse_mail"]),
                            ]
                            f.write(",".join(row_data) + "\n")
            return True  # L'exportation a réussi
        except Exception as e:
            return False  # L'exportation a échoué

    @staticmethod
    def supprimer_historique_utilisateur(adresse_mail):
        """
        Supprime l'historique d'un utilisateur

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'import

        Retour :
            un booléen qui indique si la tâche a bien été effectuée
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'DELETE FROM "Projet_Info".page_visitee '
                        "WHERE adresse_mail = %(adresse_mail)s;",
                        {"adresse_mail": adresse_mail},
                    )
                    return True  # La suppression de l'historique a réussi
        except Exception as e:
            print(f"Erreur lors de la suppression de l'historique : {str(e)}")
            return False  # La suppression de l'historique a échoué

    @staticmethod
    def ajouter_historique(adresse_mail, URL_page, titre):
        """
        Ajoute les informations de la recherche dans la table page_visitee avec l'adresse_mail de la personne ayant fait la recherche

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'ajout
            URL_page : str : l'URL de la page du stage que l'utilisateur souhaite ajouter

        Retour :
            un booléen qui indique si la tâche a bien été effectuée
        """
        try:
            current_date = datetime.date.today()
            date_visite = current_date.strftime("%Y/%m/%d")

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO "Projet_Info".page_visitee (date_visite, URL_page, adresse_mail, titre) '
                        "VALUES (%(date_visite)s, %(URL_page)s, %(adresse_mail)s, %(titre)s);",
                        {
                            "date_visite": date_visite,
                            "URL_page": URL_page,
                            "adresse_mail": adresse_mail,
                            "titre": titre,
                        },
                    )
                    connection.commit()  # N'oubliez pas de commettre la transaction
            return True  # L'ajout d'historique a réussi
        except Exception as e:
            print(f"Erreur lors de l'ajout d'historique : {str(e)}")
            return False  # L'ajout d'historique a échoué
