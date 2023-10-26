from typing import List, Optional
from utils.singleton import Singleton
from dao.db_connection import DBConnection


class ListeEnvieDAO(metaclass=Singleton):
    def afficher_liseEnvie(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("Select *           " 'FROM "Projet_Info".voeu;')
                res = cursor.fetcall()
            return res

    def afficher_liseEnvie_utilisateur(self, utilisateur):
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
