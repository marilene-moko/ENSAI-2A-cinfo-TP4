from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class NotificationsView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().user_name}",
                "choices": [
                    "Afficher ses notifications",
                    "Envoyer des notifications",
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

        elif reponse["choix"] == "Afficher ses notifications":
            

        elif reponse["choix"] == "Envoyer des notifications":
            