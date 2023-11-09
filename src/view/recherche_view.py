from InquirerPy import prompt
from tabulate import tabulate

from view.abstract_view import AbstractView
from view.session import Session
from view.fct_statut import Statut

from client.utilisateur.visiteur.stage_client_visiteur import Stageclientvisiteur


class RechercheView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "confirm",
                "message": "Voulez-vous choisir votre spécialité? Y/N",
                "default": False,
            },
            {
                "type": "confirm",
                "message": "Voulez-vous choisir votre localisation? Y/N",
                "default": False,
            },
        ]
        self.__parcourir_question = [
            {
                "type": "confirm",
                "message": "Souhaitez-vous parcourir votre recherche ?",
                "default": True,
            }
        ]
        self.__revenir_menu = [
            {
                "type": "confirm",
                "message": "Saisissez 'y' ou 'n' pour revenir au menu principal:",
                "default": True,
            }
        ]

    def display_info(self):
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        if (answers[0] == "Y") & (answers[1] == "Y"):
            localisation = input("Localisation: ")
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            print(dir(liste_stage[0]))
            # affichage = Stageclientvisiteur().afficher_stage(liste_stage)
            if liste_stage is not None:
                table = tabulate(
                    liste_stage,
                    headers=[
                        "titre",
                        "description",
                        "specialite",
                        "localisation",
                        "siteSource",
                        "URL_stage",
                        "employeur",
                        "date_publication",
                    ],
                    tablefmt="pretty",
                    disable_numparse=True,
                    colalign=["left", "center", "center", "center", "center"],
                )
                print(table)
                # Proposer à l'utilisateur de parcourir la liste des voeux
                parcours = prompt(self.__parcourir_question)
                if parcours[0]:
                    choix_recherche = [
                        {
                            "name": f"Titre: {recherche[0]}, Specialite: {recherche[2]}, Localisation: {recherche[3]}",
                            "value": recherche,
                        }
                        for recherche in liste_stage
                    ]
                    questions = [
                        {
                            "type": "list",
                            "message": "Sélectionnez la recherche que vous voulez approfondir :",
                            "name": "recherche_selectionnee",
                            "choices": choix_recherche,
                        }
                    ]
                    prompt(questions).get("recherche_selectionnee")
                    prompt(self.__revenir_menu)
                    return ConnectedStartView()

        elif (answers[0] == "Y") & (answers[1] == "N"):
            localisation = "0"
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            affichage = Stageclientvisiteur().afficher_stage(
                liste_stage, Session().email
            )
        elif (answers[0] == "N") & (answers[1] == "Y"):
            localisation = input("Localisation: ")
            specialite = "0"
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            affichage = Stageclientvisiteur().afficher_stage(
                liste_stage, Session().email
            )
        else:
            localisation = "0"
            specialite = "0"
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            affichage = Stageclientvisiteur().afficher_stage(
                liste_stage, Session().email
            )

        Statut.def_statut(Session().statut)
