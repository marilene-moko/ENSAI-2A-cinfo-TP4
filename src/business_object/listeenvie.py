from dao.listeenvie_dao import *


class ListeEnvie:
    def __init__(self, id_list, envies):
        self.id_list = id_list
        self.envies = envies  # liste des id de stages

    def afficherEnvie(self, utilisateur):
        """
        Méthode qui permet d'afficher la liste d'envie

        retourne : la liste d'envie de l'utilisateur
        """

        return afficher_listeEnvie_utilisateur(self, utilisateur)

    def retirerEnvie(self, utilisateur, id_stage):
        """
        Méthode qui permet de retirer un stage à la liste envies

        prend en paramètre : stage_id : l'id du stage à retirer de la liste d'envie

        retourne : retourne un str qui indique si la tâche a été affectuée
        """
        return supprimer_listeEnvie_utilisateur(self, utilisateur, id_stage)

    def ajouterEnvie(self, utilisateur, stage_id):
        """
        Méthode qui permet d'ajouter un stage à la liste envies

        prend en paramètre : stage_id : l'id du stage à rajouter dans la liste d'envie

        retourne : retourne rien met à mis à jour la liste envies
        """
        return ajouter_stage_listeEnvie_utilisateur(self, utilisateur, id_stage)

    def importer_listeEnvie(self):
        """
        Méthode qui permet d'importer des voeux à la liste d'envie

        """

        return importer_voeux(self)

    def exporter_listeEnvie(self, utilisateur):
        """
        Méthode qui permet d'exporter des voeux à la liste d'envie

        """

        return exporter_voeux(self, utilisateur)
