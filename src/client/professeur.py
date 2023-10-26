from utilisateur import Utilisateur
from dao.professeur_dao import *

class Professeur(Utilisateur):
    def __init__(self):
        super().__init__()

    def add_stage(self, stage_data):
        """ 
        Méthode qui permet à un(e) professeur(e) d'ajouter un stage
        
        retourne : un str qui indique si la tâche a été effectuée
        """ 
        return 

    def remove_stage(self, stage_id):
        if self.authenticated:
            # Suppression de stage
            # ...

    def notify_user(self, user, stage_id):
        if self.authenticated:
            # Notification l'utilisateur sur le stage
            # ...

    # Autres méthodes de la classe Professeur
