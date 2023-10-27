from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class ListeEnvieView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Afficher sa liste d'envie",
                    "Sauvegarder une offre dans sa liste",
                    "Modifier sa liste d'envie",
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

        elif reponse["choix"] == "Afficher sa liste d'envie":
            

        elif reponse["choix"] == "Sauvegarder une offre dans sa liste":
            

        elif reponse["choix"] == "Modifier sa liste d'envie":
            
