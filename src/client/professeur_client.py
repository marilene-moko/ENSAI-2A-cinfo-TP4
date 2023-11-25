from client.utilisateur_client import UtilisateurClient
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
