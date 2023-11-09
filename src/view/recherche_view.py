from InquirerPy import prompt
from tabulate import tabulate

from view.abstract_view import AbstractView
from view.session import Session
from view.fct_statut import Statut
from view.start_view import StartView

from client.utilisateur.visiteur.stage_client_visiteur import Stageclientvisiteur


class RechercheView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "confirm",
                "message": "Voulez-vous choisir votre spécialité?",
                "default": False,
            },
            {
                "type": "confirm",
                "message": "Voulez-vous choisir votre localisation?",
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
        if (answers[0] is True) & (answers[1] is True):
            localisation = input("Localisation: ")
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            liste_stage_modif = {
                "titre": [
                    liste_stage[stage][1][0:75] for stage in range(0, len(liste_stage))
                ],
                "description": [
                    liste_stage[stage][2][0:100] for stage in range(0, len(liste_stage))
                ],
                "specialite": [
                    liste_stage[stage][3] for stage in range(0, len(liste_stage))
                ],
                "localisation": [
                    liste_stage[stage][4] for stage in range(0, len(liste_stage))
                ],
                "date_publication": [
                    liste_stage[stage][8] for stage in range(0, len(liste_stage))
                ],
            }
            if liste_stage is not None:
                table = tabulate(
                    liste_stage_modif,
                    headers=[
                        "titre",
                        "description",
                        "specialite",
                        "localisation",
                        "date_publication",
                    ],
                    tablefmt="fancy_grid",
                    disable_numparse=True,
                    colalign=["left", "center", "center", "center", "center"],
                )
                print(table)
                # Proposer à l'utilisateur de parcourir la liste des voeux
                parcours = prompt(self.__parcourir_question)
                if parcours[0]:
                    choix_recherche = [
                        {
                            "name": f"Titre: {recherche[1]}, Specialite: {recherche[3]}, Localisation: {recherche[4]}",
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
                    recherche = prompt(questions).get("recherche_selectionnee")
                    affichage = Stageclientvisiteur().afficher_stage(recherche)
                    quest = prompt(self.__revenir_menu)
                    if quest is True:
                        return StartView()
                    else:
                        pass

        elif (answers[0] is True) & (answers[1] is False):
            localisation = "0"
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            affichage = Stageclientvisiteur().afficher_stage(
                liste_stage, Session().email
            )
        elif (answers[0] is False) & (answers[1] is True):
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
