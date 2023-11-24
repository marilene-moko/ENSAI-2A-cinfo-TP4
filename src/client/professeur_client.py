from client.utilisateur_client import UtilisateurClient
from dao.professeur_dao import ProfesseurDao
import datetime as dt


class ProfesseurClient(UtilisateurClient):
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
    def ajouterStage(adresse_mail, titre, URL, categorie, ville, poste):
        """
        Méthode qui permet à un professeur d'ajouter un stage

        Paramètres :
            adresse_mail : str : adresse mail du professeur
            titre : str : titre/intitulé du stage à ajouter
            URL : str : URL du stage à ajouter
            categorie : str : catégorie du stage à ajouter
            ville : str : ville du stage à ajouter
            poste : str : type de poste du stage à ajouter

        Retour :
            un str qui indique si la tâche a été effectuée
        """
        return ProfesseurDao.ajouterStage(
            adresse_mail, titre, URL, categorie, ville, poste
        )

    @staticmethod
    def retirerStage(adresse_mail, stage_id):
        """
        Méthode qui permet à un professeur d'ajouter un stage

        Paramètres :
            adresse_mail : str : adresse mail du professeur
            URL : str : URL du stage à retirer

        Retour :
            un str qui indique si la tâche a été effectuée
        """
        return ProfesseurDao.retirerStage(adresse_mail, URL)
