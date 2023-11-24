from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from client.utilisateur_client import UtilisateurClient
from client.utilisateur.visiteur.stage_client_visiteur import Stageclientvisiteur
from client.administrateur_client import AdministrateurClient
from view.fct_statut import Statut


class SiteView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Modifier des profils",
                    "Supprimer des profils",
                    "Revenir à la page précédente",
                    "Quitter",
                ],
            }
        ]
        self.__mail = [
            {
                "type": "input",
                "message": "Renseigner l'adresse-mail de l'utilisateur: ",
            }
        ]
        self.__modif_profil = [
            {
                "type": "confirm",
                "message": "Voulez-vous changer le statut de l'utilisateur? ",
                "default": False,
            },
        ]
        self.__nature_profil = [
            {
                "type": "list",
                "message": "Quel est le nouveau statut de l'utilisateur:",
                "choices": ["eleve", "professeur", "administrateur"],
            },
        ]

    def display_info(self):
        with open("src/graphical_assets/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Modifier des profils":
            reponse = prompt(self.__modif_profil)
            if reponse[0] is True:
                modif_statut = prompt(self.__nature_profil)[0]
                adresse_mail = prompt(self.__mail)[0]
                AdministrateurClient(
                    identifiant_personne=Session().email,
                    nom=Session(),
                    prenom=Session().prenom,
                    adresse_mail=Session().email,
                    mot_de_passe=Session().mot_de_passe,
                ).modifierDroitsUtilisateur(adresse_mail, modif_statut)
            else:
                print(
                    "Vous ne pouvez pas effectuer d'autres modifications que le changement de profil"
                )
            from view.ap_connexion_view_admin import ApConnexionViewAdmin

            return ApConnexionViewAdmin()

        elif reponse["choix"] == "Supprimer des profils":
            adresse_mail = prompt(self.__mail)[0]
            UtilisateurClient.supprimer_profil(adresse_mail)
            if UtilisateurClient.supprimer_profil(adresse_mail) is True:
                print("Le compte a bien été supprimé")
            else:
                print("Une erreur est survenue. Veuillez essayer ultérieurement.")
            from view.ap_connexion_view_admin import ApConnexionViewAdmin

            return ApConnexionViewAdmin()

        elif reponse["choix"] == "Revenir à la page précédente":
            return Statut.def_statut(Session().statut)
