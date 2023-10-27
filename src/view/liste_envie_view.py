from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from dao.listeenvie_dao import ListeEnvieDAO
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
                    "Sauvegarder une offre dans sa liste",
                    "Modifier sa liste d'envie",
                    "Importer sa liste d'envie",
                    "Exporter sa liste d'envie",
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

        elif reponse["choix"] == "Afficher sa liste d'envie":
            liste_envie = ListeEnvieDAO.afficher_listeEnvie_utilisateur(
                self, adresse_mail=Session().email
            )
            Statut.def_statut(Session().email)
            print(liste_envie)

        elif reponse["choix"] == "Sauvegarder une offre dans sa liste":
            choix = input(
                "Choississez l'identifiant du voeux que vous voulez sauvegarder: "
            )
            sauvegarder = ListeEnvieDAO.ajouter_stage_listeEnvie_utilisateur(
                self, adresse_mail=Session().email, identifiant_stage=choix
            )
            Statut.def_statut(Session().email)
            if sauvegarder is True:
                print("Votre voeux a bien été sauvegardé")
            else:
                print(sauvegarder)

        elif reponse["choix"] == "Modifier sa liste d'envie":
            choix = input(
                "Choississez l'identifiant du voeux que vous voulez supprimer: "
            )
            modif = ListeEnvieDAO.supprimer_listeEnvie_utilisateur(
                self, adresse_mail=Session().email, identifiant_voeu=choix
            )
            Statut.def_statut(Session().email)
            if modif is True:
                print("Votre voeux a bien été supprimé")
            else:
                print(modif)

        elif reponse["choix"] == "Importer sa liste d'envie":
            importer = ListeEnvieDAO.importer_voeux(self, adresse_mail=Session().email)
            Statut.def_statut(Session().email)
            if importer is True:
                print("Votre liste a bien été importée")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")

        elif reponse["choix"] == "Exporter sa liste d'envie":
            exporter = ListeEnvieDAO.exporter_voeux(self, adresse_mail=Session().email)
            Statut.def_statut(Session().email)
            if exporter is True:
                print("Votre liste a bien été exportée")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")
