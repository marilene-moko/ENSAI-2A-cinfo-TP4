from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.utilisateur_dao import UtilisateurDao


class ProfesseurDao(UtilisateurDao):
    @staticmethod
    def ajouterStage(
        email, titre_stage, URL, categorie_stage, ville_stage, poste_stage
    ):
        """
        Méthode qui permet à un professeur d'ajouter un stage

        Paramètres :
            adresse_mail : str : adresse mail du professeur
            titre_stage : str : titre/intitulé du stage à ajouter
            URL : str : URL du stage à ajouter
            categorie_stage : str : catégorie du stage à ajouter
            ville_stage : str : ville du stage à ajouter
            poste_stage : str : type de poste du stage à ajouter

        Retour :
            un str qui indique si la tâche a été effectuée
        """

        # Vérifier que le stage n'existe pas
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * " 'FROM "Projet_Info".Stage ' "WHERE URL_stage = %s;",
                    (URL,),
                )
                res = cursor.fetchone()

        # Si le stage est bien inexistant on l'ajoute à la BDD
        if not res:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO "Projet_Info".Stage (URL_stage, Categorie, Intitule, Ville, Poste, identifiant_personne_ajout) '
                        "VALUES (%s, %s, %s, %s, %s, %s);",
                        (
                            URL,
                            categorie_stage,
                            titre_stage,
                            ville_stage,
                            poste_stage,
                            email,
                        ),
                    )

                    if cursor.rowcount > 0:
                        return "Le stage a été ajouté avec succès !"
                    else:
                        return "Un problème est survenu et le stage n'a pas pu être ajouté."
        return "Le stage existe déjà."

    @staticmethod
    def retirerStage(email, URL):
        """
        Méthode qui permet à un professeur d'ajouter un stage

        Paramètres :
            adresse_mail : str : adresse mail du professeur
            URL : str : URL du stage à retirer

        Retour :
            un str qui indique si la tâche a été effectuée
        """

        # Vérifier que le stage existe
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * " 'FROM "Projet_Info".Stage ' "WHERE URL_stage = %s;",
                    (URL,),
                )
                res = cursor.fetchone()

        # Si le stage existe bien on le retire de la BDD
        if res:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'DELETE FROM "Projet_Info".stage ' "WHERE URL_stage = %s;",
                        (URL,),
                    )

                    if cursor.rowcount > 0:
                        return "Le stage a été retiré avec succès !"
                    else:
                        return "Un problème est survenu et le stage n'a pas pu être retiré."
        return "Ce stage n'existe pas."


"""
 ################ à faire  ##############################     
    def conseillerStageAEleve(self,):
"""
