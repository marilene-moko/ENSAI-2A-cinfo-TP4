from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from services.historique_service import HistoriqueService


class StartView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Connection",
                    "Inscription",
                    "Utiliser sans s'authentifier",
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
            if Session().statut == "visiteur":
                HistoriqueService.supprimer_historique_utilisateur(
                    adresse_mail=Session().email
                )
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
