from client.professeur_client import ProfesseurClient
from dao.administrateur_dao import AdministrateurDao
import datetime as dt


class AdministrateurClient(ProfesseurClient):
    def __init__(
        self,
        identifiant_personne,
        nom,
        prenom,
        adresse_mail,
        mot_de_passe,
        dateDerniereConnection=0,
    ):
        super().__init__(identifiant_personne, nom, prenom, adresse_mail, mot_de_passe)
        self.dateDerniereConnection = dt.date.today()

    @staticmethod
    def modifierDroitsUtilisateur(adresse_mail, nv_statut):
        """
        Méthode qui permet à un administrateur de modifier le statut d'un utilisateur (utilisateur, professeur, administrateur).

        Paramètres :
            adresse_mail : str : l'adresse mail de l'utilisateur dont l'administrateur veut changer le statut
            nv_statut : str : le statut que l'administrateur veut attribuer à l'utilisateur
                            ce statut ne peut qu'être : 'utilisateur', 'professeur', 'administrateur'
        Retour :
            un str qui indique si la modification des droits a bien été faite
        """
        return AdministrateurDao.modifierDroitsUtilisateur(adresse_mail, nv_statut)
