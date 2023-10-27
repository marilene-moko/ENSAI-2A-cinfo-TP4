from client.visiteur_client import VisiteurClient
import datetime as dt
from dao.utilisateur_dao import UtilisateurDao


class UtilisateurClient(VisiteurClient):
    def __init__(
        self,
        identifiant_personne,
        nom,
        prenom,
        adresse_mail,
        mot_de_passe,
        dateDerniereConnection=0,
    ):
        super().__init__()
        self.identifiant_personne = identifiant_personne
        self.nom = nom
        self.prenom = prenom
        self.adresse_mail = adresse_mail
        self.mot_de_passe = mot_de_passe
        self.dateDerniereConnection = dt.date.today()

    @staticmethod
    def utilisateur_exists(adresse_mail, mot_de_passe):
        """
        Méthode qui permet de vérifier l'existence d'un utilisateur.

        Paramètres :
            adresse_mail : str : l'adresse mail de l'utilisateur
            mot_de_passe : str : le mot de passe de l'utilisateur

        Retour :
            None si l'utilisateur n'existe pas et les caractéristiques de l'utilisateur s'il existe
        """
        return UtilisateurDao.utilisateur_exists(adresse_mail, mot_de_passe)

    @staticmethod
    def afficher_profil(adresse_mail, pseudo, nom, prenom, mot_de_passe):
        """
        Méthode qui permet d'afficher les caractéristiques d'un profil utilisateur.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur
            pseudo : str : pseudo de l'utilisateur
            nom : str : nom de l'utilisateur
            prenom : str : prénom de l'utilisateur
            mot_de_passe : str : mot de passe de l'utilisateur

        Retour :
            un str qui indique les caractéristiques du profil utilisateur
        """
        return UtilisateurDao.afficher_profil(
            adresse_mail, pseudo, nom, prenom, mot_de_passe
        )

    @staticmethod
    def modifier_nom(adresse_mail, modification):
        """
        Méthode qui permet à un utilisateur de changer son nom sur son profil.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur
            modification : str : le nouveau nom

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_nom(adresse_mail, modification)

    @staticmethod
    def modifier_prenom(adresse_mail, modification):
        """
        Méthode qui permet à un utilisateur de changer son prénom sur son profil.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur
            modification : str : le nouveau prénom

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_prenom(adresse_mail, modification)

    @staticmethod
    def modifier_mdp(adresse_mail, modification):
        """
        Méthode qui permet à un utilisateur de changer son mot de passe.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur
            modification : str : le nouveau mot de passe

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_mdp(adresse_mail, modification)

    @staticmethod
    def supprimer_profil(adresse_mail):
        """
        Méthode qui permet à un utilisateur de supprimer son historique.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.supprimer_profil(adresse_mail)
