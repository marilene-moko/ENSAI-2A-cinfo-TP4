from visiteur import Visiteur
import datetime as dt

class Utilisateur(Visiteur):
    def __init__(self, identifiant_personne, nom, prenom, adresse_mail, mot_de_passe, dateDerniereConnection=0):
        super().__init__()
        self.identifiant_personne = identifiant_personne
        self.nom = nom
        self.prenom = prenom
        self.email = adresse_mail
        self.motDePasse = mot_de_passe
        self.dateDerniereConnection = dt.date.today()

    def edit_profile(self, data):
        if self.authenticated:
            # Modification du profil sécurisée ici
            # ...

    def create_alert(self, criteria):
        if self.authenticated:
            # Création d'alerte
            # ...

    def edit_wishlist(self, stage_id, data):
        if self.authenticated:
            # Modification de la liste de souhaits
            # ...

    # Autres méthodes de la classe Utilisateur
