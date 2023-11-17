from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from services.listeenvie_service import ListeEnvieService
from view.fct_statut import Statut


class ListeEnvieView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Afficher sa liste d'envie",
                    "Modifier sa liste d'envie",
                    "Importer sa liste d'envie",
                    "Exporter sa liste d'envie",
                    "Quitter",
                ],
            }
        ]
        self.__choix = [
            {
                "type": "confirm",
                "message": "Souhaitez-vous ajouter un voeux grâce à son identifiant ?",
                "default": False,
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Afficher sa liste d'envie":
            liste_envie = ListeEnvieService.afficher_listeEnvie_utilisateur(
                adresse_mail=Session().email
            )
            print(liste_envie)
            return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Modifier sa liste d'envie":
            choix = input(
                "Choississez l'identifiant du voeux que vous voulez supprimer: "
            )
            modif = ListeEnvieService.supprimer_listeEnvie_utilisateur(
                adresse_mail=Session().email, identifiant_voeu=choix
            )
            if modif is True:
                print("Votre voeux a bien été supprimé")
            else:
                print(modif)
            return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Importer sa liste d'envie":
            importer = ListeEnvieService.importer_voeux(adresse_mail=Session().email)
            if importer is True:
                print("Votre liste a bien été importée")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")
            return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Exporter sa liste d'envie":
            exporter = ListeEnvieService.exporter_voeux(adresse_mail=Session().email)
            if exporter is True:
                print("Votre liste a bien été exportée")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")
            return Statut.def_statut(Session().statut)
