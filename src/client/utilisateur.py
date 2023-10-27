from client.visiteur import VisiteurClient
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
        self.email = adresse_mail
        self.motDePasse = mot_de_passe
        self.dateDerniereConnection = dt.date.today()

    def utilisateur_exists(email, mdp):
        """
        Méthode qui permet de vérifier l'existence d'un utilisateur.

        Paramètres :
            email : str : l'adresse mail de l'utilisateur
            mdp : str : le mot de passe de l'utilisateur

        Retour :
            None si l'utilisateur n'existe pas et les caractéristiques de l'utilisateur s'il existe
        """
        return UtilisateurDao.utilisateur_exists(email, mdp)

    def afficher_profil(email, pseudo, nom, prenom, mdp):
        """
        Méthode qui permet d'afficher les caractéristiques d'un profil utilisateur.

        Paramètres :
            email : str : adresse mail de l'utilisateur
            pseudo : str : pseudo de l'utilisateur
            nom : str : nom de l'utilisateur
            prenom : str : prénom de l'utilisateur
            mdp : str : mot de passe de l'utilisateur

        Retour :
            un str qui indique les caractéristiques du profil utilisateur
        """
        return UtilisateurDao.afficher_profil(email, pseudo, nom, prenom, mdp)

    def modifier_nom(email, modification):
        """
        Méthode qui permet à un utilisateur de changer son nom sur son profil.

        Paramètres :
            email : str : adresse mail de l'utilisateur
            modification : str : le nouveau nom

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_nom(email, modification)

    def modifier_prenom(email, modification):
        """
        Méthode qui permet à un utilisateur de changer son prénom sur son profil.

        Paramètres :
            email : str : adresse mail de l'utilisateur
            modification : str : le nouveau prénom

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_prenom(email, modification)

    def modifier_mdp(email, modification):
        """
        Méthode qui permet à un utilisateur de changer son mot de passe.

        Paramètres :
            email : str : adresse mail de l'utilisateur
            modification : str : le nouveau mot de passe

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_mdp(email, modification)

    def supprimer_profil(email):
        """
        Méthode qui permet à un utilisateur de supprimer son historique.

        Paramètres :
            email : str : adresse mail de l'utilisateur

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.supprimer_profil(email)
