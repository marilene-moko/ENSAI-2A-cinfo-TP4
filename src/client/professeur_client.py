from client.utilisateur_client import UtilisateurClient
from dao.professeur_dao import ProfesseurDao

class ProfesseurClient(Utilisateur):
    def __init__(self):
        super().__init__()

    @staticmethod
    def ajouterStage(adresse_mail, titre, URL, categorie, ville, poste):
        """ 
        Méthode qui permet à un professeur d'ajouter un stage

        paramètres :
        email : str : adresse mail du professeur
        titre : str : titre/intitulé du stage à ajouter
        URL : str : URL du stage à ajouter
        categorie : str : catégorie du stage à ajouter
        ville : str : ville du stage à ajouter
        poste : str : type de poste du stage à ajouter
        
        retourne : un str qui indique si la tâche a été effectuée
        """ 
        return ProfesseurDao.ajouterStage(adresse_mail, titre, URL, categorie, ville, poste)

    @staticmethod
    def retirerStage(self, stage_id):
        """ 
        Méthode qui permet à un professeur d'ajouter un stage

        paramètres :
        email : str : adresse mail du professeur
        URL : str : URL du stage à retirer
        
        retourne : un str qui indique si la tâche a été effectuée
        """ 
        return ProfesseurDao.retirerStage(adresse_mail, URL)
        
 """    ################ à faire  ##############################     
        def notify_user(self, user, stage_id):
            if self.authenticated:
                # Notification l'utilisateur sur le stage
                # ...

 """