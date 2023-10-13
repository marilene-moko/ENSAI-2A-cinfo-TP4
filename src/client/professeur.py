from utilisateur import Utilisateur

class Professeur(Utilisateur):
    def __init__(self):
        super().__init__()
        self.specialties = []

    def add_stage(self, stage_data):
        if self.authenticated:
            # Ajout de stage sécurisé ici
            # ...

    def remove_stage(self, stage_id):
        if self.authenticated:
            # Suppression de stage sécurisée ici
            # ...

    def notify_user(self, user, stage_id):
        if self.authenticated:
            # Notification sécurisée de l'utilisateur sur le stage
            # ...

    # Autres méthodes de la classe Professeur
