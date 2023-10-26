from utilisateur import Utilisateur

class Professeur(Utilisateur):
    def __init__(self):
        super().__init__()

    def add_stage(self, stage_data):
        if self.authenticated:
            # Ajout de stage
            # ...

    def remove_stage(self, stage_id):
        if self.authenticated:
            # Suppression de stage
            # ...

    def notify_user(self, user, stage_id):
        if self.authenticated:
            # Notification l'utilisateur sur le stage
            # ...

    # Autres méthodes de la classe Professeur
