from InquirerPy import prompt
from tabulate import tabulate

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
            pass

        elif reponse["choix"] == "Afficher l'historique":
            liste = HistoriqueService.afficher_historique_utilisateur(
                adresse_mail=Session().email
            )
            if len(liste) > 0:
                liste_modif = {
                    "titre": [liste[stage]["titre"] for stage in range(0, len(liste))],
                    "url_page": [
                        liste[stage]["url_page"] for stage in range(0, len(liste))
                    ],
                    "date_visite": [
                        liste[stage]["date_visite"].strftime("%Y/%m/%d")
                        for stage in range(0, len(liste))
                    ],
                }
                historique = tabulate(
                    liste_modif,
                    headers=[
                        "titre",
                        "url_page",
                        "date_visite",
                    ],
                    tablefmt="fancy_grid",
                    disable_numparse=True,
                    colalign=["center", "center", "center"],
                )
                print(historique)
            else:
                print("Votre historique est vide")
            return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Supprimer l'historique":
            if Session().email == "adresse_mail_visiteur":
                print("Veuillez-vous connecter pour accéder à cette fonctionnalité")
            else:
                supp = HistoriqueService.supprimer_historique_utilisateur(
                    adresse_mail=Session().email
                )
                if supp is True:
                    print("La suppression de votre historique a bien eu lieu")
                else:
                    print(supp)
            return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Exporter l'historique":
            if Session().email == "adresse_mail_visiteur":
                print("Veuillez-vous connecter pour accéder à cette fonctionnalité")
            else:
                exporter = HistoriqueService.exporter_historique(
                    adresse_mail=Session().email
                )
                if exporter is True:
                    print("Votre historique a bien été exporté")
                else:
                    print("Une erreur s'est produite. Veuillez essayer ultérieurement.")
            return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Importer l'historique":
            if Session().email == "adresse_mail_visiteur":
                print("Veuillez-vous connecter pour accéder à cette fonctionnalité")
            else:
                importer = HistoriqueService.importer_historique(
                    adresse_mail=Session().email
                )
                if importer is True:
                    print("Votre historique a bien été exporté")
                else:
                    print("Une erreur s'est produite. Veuillez essayer ultérieurement.")
            return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Revenir à la page précédente":
            return Statut.def_statut(Session().statut)
