from visiteur import Visiteur

class Utilisateur(Visiteur):
    def __init__(self):
        super().__init__()
        self.profile = {}
        self.alerts = []
        self.wishlist = []
        self.session_history = []

    def edit_profile(self, data):
        if self.authenticated:
            # Modification du profil sécurisée ici
            # ...

    def create_alert(self, criteria):
        if self.authenticated:
            # Création d'alerte sécurisée ici
            # ...

    def edit_wishlist(self, stage_id, data):
        if self.authenticated:
            # Modification de la liste de souhaits sécurisée ici
            # ...

    # Autres méthodes de la classe Utilisateur
