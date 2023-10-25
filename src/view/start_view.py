from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Connection",
                    "Inscription",
                    "Utiliser sans s'authentifier",
                    "Quit",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quit":
            pass

        elif reponse["choix"] == "Connection":
            from view.connection_view import ConnectionView

            return ConnectionView()

        elif reponse["choix"] == "Inscription":
            from view.inscription_view import InscriptionView

            return InscriptionView()

        elif reponse["choix"] == "Utiliser sans s'authentifier":
            from view.ap_sans_authentification_view import ApSansAuthentificationView

            return ApSansAuthentificationView()
