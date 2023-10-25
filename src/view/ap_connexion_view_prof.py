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
            

        elif reponse["choix"] == "Historique":
            from view.historique_view import HistoriqueView

            return HistoriqueView()

        elif reponse["choix"] == "Liste d'envie":
            from view.liste_envie_view import ListeEnvieView

            return ListeEnvieView()

        elif reponse["choix"] == "Profil":
            from view.profil_view import ProfilView

            return ProfilView()

        elif reponse["choix"] == "Notifications":
            from view.notifications_view import NotificationsView

            return NotificationsView()

        elif reponse["choix"] == "Publication":
            from view.publication_view import PublicationView

            return PublicationView()
