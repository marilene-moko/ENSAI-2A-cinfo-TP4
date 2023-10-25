from typing import List, Optional
from utils.singleton import Singleton
from client.utilisateur import Utilisateur
from dao.db_connection import DBConnection


class HistoriqueDAO(metaclass=Singleton):
    def afficher_historique(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("Select *           " 'FROM "Projet_Info".personne;')
                res = cursor.fetcall()
            return res

    def afficher_historique_utilisateur(self, utilisateur):
        identifiant_personne = utilisateur["identifiant_personne"]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Select *             "
                    'FROM "Projet_Info".page_visitee'
                    "WHERE identifiant_personne = %(identifiant_personne)s;",
                    {
                        "identifiant_personne": identifiant_personne,
                    },
                )
                res = cursor.fetchall()
            return res
