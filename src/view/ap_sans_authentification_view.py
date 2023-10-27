from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class ApSansAuthentificationView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "",
                "choices": [
                    "Rechercher",
                    "Historique",
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
            from view.recherche_view import RechercheView

            return RechercheView()

        elif reponse["choix"] == "Historique":
            from view.inscription_view import InscriptionView

            return InscriptionView()
