from utilisateur import Utilisateur
from dao.professeur_dao import *

class Professeur(Utilisateur):
    def __init__(self):
        super().__init__()

    def add_stage(self, email, titre, URL, categorie, ville, poste):
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
        return ajouterStage(self, email, titre, URL, categorie, ville, poste)

    def remove_stage(self, stage_id):
        """ 
        Méthode qui permet à un professeur d'ajouter un stage

        paramètres :
        email : str : adresse mail du professeur
        URL : str : URL du stage à retirer
        
        retourne : un str qui indique si la tâche a été effectuée
        """ 
        return retirerStage(self, email, URL)
        
 ################ à faire  ##############################     
    def notify_user(self, user, stage_id):
        if self.authenticated:
            # Notification l'utilisateur sur le stage
            # ...

