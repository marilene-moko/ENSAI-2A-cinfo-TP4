from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from services.historique_service import HistoriqueService


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
                    "Revenir à la page précédente",
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
            if Session().statut == "visiteur":
                HistoriqueService.supprimer_historique_utilisateur(
                    adresse_mail=Session().email
                )
                pass

        elif reponse["choix"] == "Rechercher":
            from view.recherche_view import RechercheView

            return RechercheView()

        elif reponse["choix"] == "Historique":
            from view.historique_view import HistoriqueView

            return HistoriqueView()

        elif reponse["choix"] == "Revenir à la page précédente":
            from view.start_view_sans_logo import StartViewSimple

            return StartViewSimple()
