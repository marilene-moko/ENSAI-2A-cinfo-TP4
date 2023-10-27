from dao.listeenvie_dao import ListeEnvieDAO


class ListeEnvie:
    def __init__(self, id_list, envies):
        self.id_list = id_list
        self.envies = envies  # liste des id de stages

    def afficher_listeEnvie_utilisateur(email):
        """
        Méthode qui permet d'afficher la liste d'envie

        retourne : la liste d'envie de l'utilisateur
        """

        return ListeEnvieDAO.afficher_listeEnvie_utilisateur(email)

    def supprimer_listeEnvie_utilisateur(email, id_stage):
        """
        Méthode qui permet de retirer un stage à la liste envies

        prend en paramètre : stage_id : l'id du stage à retirer de la liste d'envie

        retourne : retourne un str qui indique si la tâche a été affectuée
        """
        return ListeEnvieDAO.supprimer_listeEnvie_utilisateur(email, id_stage)

    def ajouter_stage_listeEnvie_utilisateur(email, id_stage):
        """
        Méthode qui permet d'ajouter un stage à la liste envies

        prend en paramètre : stage_id : l'id du stage à rajouter dans la liste d'envie

        retourne : retourne rien met à mis à jour la liste envies
        """
        return ListeEnvieDAO.ajouter_stage_listeEnvie_utilisateur(email, id_stage)

    def importer_voeux(email):
        """
        Méthode qui permet d'importer des voeux à la liste d'envie

        """

        return ListeEnvieDAO.importer_voeux(email)

    def exporter_voeux(email):
        """
        Méthode qui permet d'exporter des voeux à la liste d'envie

        """

        return ListeEnvie.exporter_voeux(email)
