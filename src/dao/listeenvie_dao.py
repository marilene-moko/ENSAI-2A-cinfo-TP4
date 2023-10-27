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

    def afficher_listeEnvie_utilisateur(self, adresse_mail):
        """
        Affiche la liste d'envie d'une personne en fonction de so identifiant
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Select *             "
                    'FROM "Projet_Info".voeu'
                    "WHERE adresse_mail = %(adresse_mail)s;",
                    {"adresse_mail": adresse_mail},
                )
                res = cursor.fetchall()
            return res

    def supprimer_listeEnvie_utilisateur(self, adresse_mail, identifiant_voeu):
        """
        Supprime un voeu de la liste d'envie d'un utilisateur.
        Plusieurs tests pour savoir si le voeu existe et s'il appartient
        bien à l'utilisateur sont fait.
        """

        # Vérifier si le voeu appartient à l'utilisateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT adresse_mail FROM "Projet_Info".voeu WHERE identifiant_voeu = %(identifiant_voeu)s;',
                    {"identifiant_voeu": identifiant_voeu},
                )
                row = cursor.fetchone()

        if row is None:
            # Le voeu n'existe pas
            return "Le voeu spécifié n'existe pas."

        adresse_mail_voeu = row["adresse_mail"]

        if adresse_mail_voeu != adresse_mail:
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

    def ajouter_stage_listeEnvie_utilisateur(self, adresse_mail, identifiant_stage):
        """
        Permet d'ajouter un stage a la liste d'envie d'un utilisateur en utilisant son id.
        On vérifie en amont si le voeu est déjà présent ou non et si le stage existe bien
        """

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
                    'SELECT * FROM "Projet_Info".voeu WHERE adresse_mail = %(adresse_mail)s AND identifiant_stage = %(identifiant_stage)s;',
                    {
                        "adresse_mail": adresse_mail,
                        "identifiant_stage": identifiant_stage,
                    },
                )
                existing_entry = cursor.fetchone()

                if existing_entry:
                    return "Le stage est déjà dans la liste d'envies de l'utilisateur."

                # Ajouter le stage à la liste d'envies de l'utilisateur
                cursor.execute(
                    'INSERT INTO "Projet_Info".voeu (adresse_mail, identifiant_stage)'
                    "VALUES (%(adresse_mail)s, %(identifiant_stage)s);",
                    {
                        "adresse_mail": adresse_mail,
                        "identifiant_stage": identifiant_stage,
                    },
                )

        return "Le stage a été ajouté à la liste d'envies de l'utilisateur."

    def importer_voeux(self, adresse_mail):
        """
        Importe une liste d'envies aux entêtes URL_voeu,Categorie,Intitule,Ville,Poste,Entreprise,identifiant_personne

        L'importation se fait nécessairement d'un fichier nommé "importerVoeux" situé
        dans le dossier data.
        L'utilisateur qui importe ne peut importer des voeux que dans sa propre liste d'envies
        """
        try:
            with open("data/importerVoeux.txt", "r") as f:
                next(f)  # Ignorer la première ligne si elle contient les en-têtes
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        for line in f:
                            data = line.strip().split(
                                ","
                            )  # Supposer que le CSV est délimité par des virgules
                            # Assurez-vous que l'identifiant de l'utilisateur est utilisé pour l'insertion
                            sql = """INSERT INTO "Projet_Info".voeu (URL_voeu, Categorie, Intitule, Ville, Poste, Entreprise, adresse_mail)
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
                                    adresse_mail,
                                ),
                            )
            return True  # L'importation a réussi
        except Exception as e:
            print(f"Erreur lors de l'importation : {str(e)}")
            return False  # L'importation a échoué

    def exporter_voeux(self, adresse_mail):
        """
        Exporter un historique

        L'exportation se fait dans un fichier "exporterVoeux" dans le dossier data
        L'utilisateur qui exporte ne peut exporter que SON historique
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT *
                        FROM "Projet_Info".voeu
                        WHERE adresse_mail = %(adresse_mail)s""",
                        {"adresse_mail": adresse_mail},
                    )
                    res = cursor.fetchall()
                    with open("data/exporterVoeux.txt", "w", newline="") as f:
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
                                "adresse_mail",
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
                                str(row["adresse_mail"]),
                            ]
                            f.write(",".join(row_data) + "\n")
            return True  # L'exportation a réussi
        except Exception as e:
            print(f"Erreur lors de l'exportation : {str(e)}")
            return False  # L'exportation a échoué
