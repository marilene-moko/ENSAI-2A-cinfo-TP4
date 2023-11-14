from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from view.fct_statut import Statut
from services.historique_service import HistoriqueService


class HistoriqueView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Afficher l'historique",
                    "Supprimer l'historique",
                    "Exporter l'historique",
                    "Importer l'historique",
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

        elif reponse["choix"] == "Afficher l'historique":
            historique = HistoriqueService.afficher_historique_utilisateur(
                adresse_mail=Session().email
            )
            print(historique)
            print(Session().statut)
            Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Supprimer l'historique":
            supp = HistoriqueService.supprimer_historique_utilisateur(
                adresse_mail=Session().email
            )
            Statut.def_statut(Session().statut)
            if supp is True:
                print("La suppression de votre historique a bien eu lieu")
            else:
                print(supp)

        elif reponse["choix"] == "Exporter l'historique":
            exporter = HistoriqueService.exporter_historique(
                adresse_mail=Session().email
            )
            Statut.def_statut(Session().statut)
            if exporter is True:
                print("Votre historique a bien été exporté")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")

        elif reponse["choix"] == "Importer l'historique":
            importer = HistoriqueService.importer_historique(
                adresse_mail=Session().email
            )
            Statut.def_statut(Session().statut)
            if importer is True:
                print("Votre historique a bien été exporté")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")
