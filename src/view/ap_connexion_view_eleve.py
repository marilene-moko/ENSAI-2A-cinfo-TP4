from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class ApConnexionViewEleve(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Rechercher",
                    "Historique",
                    "Liste d'envie",
                    "Profil",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Rechercher":
            from view.recherche_view import RechercheView

            return RechercheView()

        elif reponse["choix"] == "Historique":
            from view.historique_view import HistoriqueView

            return HistoriqueView()

        elif reponse["choix"] == "Liste d'envie":
            from view.liste_envie_view import ListeEnvieView

            return ListeEnvieView()

        elif reponse["choix"] == "Profil":
            from view.profil_view import ProfilView

            return ProfilView()
