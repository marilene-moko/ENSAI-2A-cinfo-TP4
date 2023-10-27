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

    def utilisateur_exists(self, email, mdp):
        """
        Méthode qui permet de vérifier l'existence d'un utilisateur.

        Paramètres :
            email : str : l'adresse mail de l'utilisateur
            mdp : str : le mot de passe de l'utilisateur

        Retour :
            None si l'utilisateur n'existe pas et les caractéristiques de l'utilisateur s'il existe
        """
        return UtilisateurDao.utilisateur_exists(self, email, mdp)

    def afficher_profil(self, email, pseudo, nom, prenom, mdp):
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
        return UtilisateurDao.afficher_profil(self, email, pseudo, nom, prenom, mdp)

    def modifier_nom(self, email, modification):
        """
        Méthode qui permet à un utilisateur de changer son nom sur son profil.

        Paramètres :
            email : str : adresse mail de l'utilisateur
            modification : str : le nouveau nom

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_nom(self, email, modification)

    def modifier_prenom(self, email, modification):
        """
        Méthode qui permet à un utilisateur de changer son prénom sur son profil.

        Paramètres :
            email : str : adresse mail de l'utilisateur
            modification : str : le nouveau prénom

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_prenom(self, email, modification)

    def modifier_mdp(self, email, modification):
        """
        Méthode qui permet à un utilisateur de changer son mot de passe.

        Paramètres :
            email : str : adresse mail de l'utilisateur
            modification : str : le nouveau mot de passe

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """
        return UtilisateurDao.modifier_mdp(self, email, modification)

    def modifhisto(self):
        """
                Méthode qui permet à un utilisateur de modifier son historique.

                Retour :
        ###########pas fini###################"
        """
