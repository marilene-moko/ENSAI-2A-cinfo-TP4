from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class ApConnexionViewProf(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().user_name}",
                "choices": [
                    "Rechercher",
                    "Historique",
                    "Liste d'envie",
                    "Profil",
                    "Notifications",
                    "Publication",
                    "Site",
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

        elif reponse["choix"] == "Rechercher":
            from view.connection_view import ConnectionView

            return ConnectionView()

        elif reponse["choix"] == "Historique":
            from view.inscription_view import InscriptionView

            return InscriptionView()

        elif reponse["choix"] == "Liste d'envie":
            from view.inscription_view import InscriptionView

            return InscriptionView()

        elif reponse["choix"] == "Profil":
            from view.inscription_view import InscriptionView

            return InscriptionView()

        elif reponse["choix"] == "Notifications":
            from view.inscription_view import InscriptionView

            return InscriptionView()

        elif reponse["choix"] == "Publication":
            from view.inscription_view import InscriptionView

            return InscriptionView()

        elif reponse["choix"] == "Site":
            from view.inscription_view import InscriptionView

            return InscriptionView()
