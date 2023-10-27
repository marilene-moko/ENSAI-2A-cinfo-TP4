from client.professeur_client import ProfesseurClient
from dao.administrateur_dao import AdministrateurDao


class AdministrateurClient(ProfesseurClient):
    def __init__(self):
        super().__init__()

    @staticmethod
    def modifierDroitsUtilisateur(adresse_mail, nv_statut):
        """
        Méthode qui permet à un administrateur de modifier le statut d'un utilisateur (utilisateur, professeur, administrateur).

        paramètres :
        adresse_mail : str : l'adresse mail de l'utilisateur dont l'administrateur veut changer le statut
        nv_statut : str : le statut que l'administrateur veut attribuer à l'utilisateur
                           ce statut ne peut qu'être : 'utilisateur', 'professeur', 'administrateur'
        """
        return AdministrateurDao.modifierDroitsUtilisateur(adresse_mail, nv_statut)
