from dao.listeenvie_dao import ListeEnvieDAO


class ListeEnvie:
    def __init__(self, id_list, envies):
        self.id_list = id_list
        self.envies = envies  # liste des id de stages

    def afficher_listeEnvie_utilisateur(adresse_mail):
        """
        Méthode qui permet à un utilisateur d'afficher sa liste d'envie.

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui veut afficher sa liste d'envie

        Retour :
            la liste d'envie de l'utilisateur
        """

        return ListeEnvieDAO.afficher_listeEnvie_utilisateur(adresse_mail)

    def supprimer_listeEnvie_utilisateur(adresse_mail, id_stage):
        """
        Méthode qui permet à un utilisateur de retirer un stage à sa liste d'envie.

        Paramètres :
            adresse_mail : str : l'adresse mail de l'utiliseur qui veut retirer un stage de sa liste d'envie
            id_stage : l'identifiant du stage à retirer de la liste d'envie

        Retour :
            un booléen qui indique si la tâche a été affectuée
        """
        return ListeEnvieDAO.supprimer_listeEnvie_utilisateur(adresse_mail, id_stage)

    def ajouter_stage_listeEnvie_utilisateur(adresse_mail, id_stage):
        """
        Méthode qui permet à un utilisateur d'ajouter un stage à sa liste d'envie.

        Paramètres :
            adresse_mail : str : l'adresse mail de l'utiliseur qui veut ajouter un stage de sa liste d'envie
            id_stage : l'identifiant du stage à ajouter dans la liste d'envie


        Retour :
            un booléen qui indique si la tâche a été affectuée
        """
        return ListeEnvieDAO.ajouter_stage_listeEnvie_utilisateur(
            adresse_mail, id_stage
        )

    def importer_voeux(adresse_mail):
        """
        Méthode qui permet à un utilisateur d'importer des voeux dans sa liste d'envie.

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'import

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """

        return ListeEnvieDAO.importer_voeux(adresse_mail)

    def exporter_voeux(adresse_mail):
        """
        Méthode qui permet à un utilisateur d'exporter sa liste d'envie.
        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'export

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return ListeEnvie.exporter_voeux(adresse_mail)
