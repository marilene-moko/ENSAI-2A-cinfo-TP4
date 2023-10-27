from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from view.fct_statut import Statut


class PublicationView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Afficher ses publications",
                    "Publier des offres",
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

        elif reponse["choix"] == "Afficher ses publications":
            Statut.def_statut(self, Session().statut)

        elif reponse["choix"] == "Publier des offres":
            Statut.def_statut(self, Session().statut)
