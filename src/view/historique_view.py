from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class HistoriqueView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().user_name}",
                "choices": [
                    "Afficher l'historique",
                    "Modifier l'historique",
                    "Exporter l'historique",
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

        elif reponse["choix"] == "Afficher l'historique":
            

        elif reponse["choix"] == "Modifier l'historique":
            

        elif reponse["choix"] == "Exporter l'historique":
            
