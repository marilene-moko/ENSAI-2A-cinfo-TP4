from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from view.fct_statut import Statut
from dao.historique_dao import HistoriqueDAO


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
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Afficher l'historique":
            historique = HistoriqueDAO.afficher_historique_utilisateur(
                self, adresse_mail=Session().email
            )
            Statut.def_statut(self, Session().statut)
            print(historique)

        elif reponse["choix"] == "Supprimer l'historique":
            supp = HistoriqueDAO.supprimer_historique_utilisateur(
                self, adresse_mail=Session().email
            )
            Statut.def_statut(self, Session().statut)
            if supp is True:
                print("La suppression de votre historique a bien eu lieu")
            else:
                print(supp)

        elif reponse["choix"] == "Exporter l'historique":
            exporter = HistoriqueDAO.exporter_historique(
                self, adresse_mail=Session().email
            )
            Statut.def_statut(self, Session().statut)
            if exporter is True:
                print("Votre historique a bien été exporté")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")

        elif reponse["choix"] == "Importer l'historique":
            importer = HistoriqueDAO.importer_historique(
                self, adresse_mail=Session().email
            )
            Statut.def_statut(self, Session().statut)
            if importer is True:
                print("Votre historique a bien été exporté")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")
