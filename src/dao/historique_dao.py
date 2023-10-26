from typing import List, Optional
from utils.singleton import Singleton
from dao.db_connection import DBConnection
import pandas as pd
from sqlalchemy import create_engine


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

    def importer_historique(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO "Projet_Info".page_visitee 
                    Select * FROM
                    '\\filer-eleves2id2241\\Cours2A\\UE3_Complements_informatique\\TP\\TP4\\depot_commun\\ENSAI-2A-cinfo-TP4\\data\\import.csv'
                    DELIMITER ',' CSV HEADER """
                )

    def exporter_historique(self):
        db_url = "postgresql://id2241:id2241@sgbd-eleves.domensai.ecole:5432/id2241"
        engine = create_engine(db_url)
