from InquirerPy import prompt
from tabulate import tabulate
import textwrap

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
                    "Revenir à la page précédente",
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
            if len(liste_envie) > 0:
                liste_envie_modif = {
                    "titre": [
                        textwrap.fill(liste_envie[stage]["intitule"], 25)
                        for stage in range(0, len(liste_envie))
                    ],
                    "URL du stage": [
                        textwrap.fill(liste_envie[stage]["identifiant_stage"], 25)
                        for stage in range(0, len(liste_envie))
                    ],
                    "specialite": [
                        liste_envie[stage]["categorie"]
                        for stage in range(0, len(liste_envie))
                    ],
                    "localisation": [
                        textwrap.fill(liste_envie[stage]["ville"], 15)
                        for stage in range(0, len(liste_envie))
                    ],
                    "entreprise": [
                        liste_envie[stage]["entreprise"]
                        for stage in range(0, len(liste_envie))
                    ],
                }
                table = tabulate(
                    liste_envie_modif,
                    headers=[
                        "titre",
                        "URL du stage",
                        "specialite",
                        "localisation",
                        "entreprise",
                    ],
                    tablefmt="fancy_grid",
                    disable_numparse=True,
                    colalign=["center", "center", "center", "center", "center"],
                )
                print(table)
            else:
                print("Votre liste d'envie est vide")
            return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Modifier sa liste d'envie":
            liste_envie = ListeEnvieService.afficher_listeEnvie_utilisateur(
                adresse_mail=Session().email
            )
            if liste_envie is not None:
                choix_modif = [
                    {
                        "name": f"Titre: {modif['intitule']}, Specialite: {modif['categorie']}, Localisation: {modif['ville']}",
                        "value": modif,
                    }
                    for modif in liste_envie
                ]
                questions = [
                    {
                        "type": "list",
                        "message": "Sélectionnez le stage que vous voulez supprimer :",
                        "name": "modification",
                        "choices": choix_modif,
                    }
                ]
                modif_stage = prompt(questions).get("modification")
                modif = ListeEnvieService.supprimer_listeEnvie_utilisateur(
                    adresse_mail=Session().email,
                    identifiant_stage=modif_stage["identifiant_stage"],
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

        elif reponse["choix"] == "Revenir à la page précédente":
            return Statut.def_statut(Session().statut)
