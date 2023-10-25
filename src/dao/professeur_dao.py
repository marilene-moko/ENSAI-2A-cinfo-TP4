from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.utilisateur_dao import UtilisateurDao


class ProfesseurDao(UtilisateurDao):
    def ajouterStage(
        self,
        utilisateur,
        titre_stage,
        URL_stage,
        categorie_stage,
        ville_stage,
        poste_stage,
    ):
        email = utilisateur["email"]


        #if => vérifier si le stage n'est pas déjà dans la BDD
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO "Projet_Info".stage(URL_stage, Categorie, Intitule, Ville, Poste, identifiant_personne_ajout) VALUE '
                        "(URL_stage, categorie_stage, titre_stage, ville_stage, poste_stage, email);                                     "
                    )
                    
                    if cursor.rowcount > 0:
                        return "Le stage a été ajouté avec succès !"
                    else:
                        return "Un problème est survenu et le stage n'a pas pu être ajouté"
