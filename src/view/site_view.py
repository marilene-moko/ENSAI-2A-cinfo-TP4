from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from dao.utilisateur_dao import UtilisateurDao
from dao.stage_dao import StageDao


class SiteView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().user_name}",
                "choices": [
                    "Modifier des offres",
                    "Modifier des profils",
                    "Supprimer des offres",
                    "Supprimer des profils",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Modifier des offres":
            

        elif reponse["choix"] == "Modifier des profils":
            

        elif reponse["choix"] == "Supprimer des offres":
            supp_offre = input("Veuillez entrer l'identifiant de l'offre que vous voulez supprimer: ")
            if StageDao().supprimer_stage(supp_profil) is True:
                print("Le compte a bien été supprimé")
                from view.ap_connexion_view_admin import ApConnexionViewAdmin
                return ApConnexionViewAdmin()
            else:
                print("Une erreur est survenue. Veuillez essayer ultérieurement.")
                    from view.ap_connexion_view_admin import ApConnexionViewAdmin
                    return ApConnexionViewAdmin()

        elif reponse["choix"] == "Supprimer des profils":
            supp_profil = input("Veuillez entrer l'email que vous voulez supprimer: ")
            if UtilisateurDao().supprimer_profil(supp_profil) is True:
                print("Le compte a bien été supprimé")
                from view.ap_connexion_view_admin import ApConnexionViewAdmin
                return ApConnexionViewAdmin()
            else:
                print("Une erreur est survenue. Veuillez essayer ultérieurement.")
                    from view.ap_connexion_view_admin import ApConnexionViewAdmin
                    return ApConnexionViewAdmin()
            
