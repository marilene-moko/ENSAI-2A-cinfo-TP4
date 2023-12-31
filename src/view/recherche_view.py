from InquirerPy import prompt
from tabulate import tabulate
import textwrap

from view.abstract_view import AbstractView
from view.session import Session
from view.fct_statut import Statut

from client.utilisateur.visiteur.stage_client_visiteur import Stageclientvisiteur
from services.historique_service import HistoriqueService
from services.listeenvie_service import ListeEnvieService


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
            {
                "type": "confirm",
                "message": "Voulez-vous choisir la date de publication de l'offre?",
                "default": False,
            },
        ]
        self.__parcourir_question = [
            {
                "type": "confirm",
                "message": "Souhaitez-vous parcourir votre recherche ?",
                "default": False,
            }
        ]
        self.__revenir_menu = [
            {
                "type": "confirm",
                "message": "Souhaitez-vous continuer votre parcourt de recherche ?",
                "default": False,
            }
        ]
        self.__continuer = [
            {
                "type": "confirm",
                "message": "Voulez-vous continuer de rechercher ?",
                "default": False,
            }
        ]
        self.__fav = [
            {
                "type": "confirm",
                "message": "Voulez-vous enregister ce stage dans vos favoris ?",
                "default": False,
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        if (answers[0] is True) & (answers[1] is True) & (answers[2] is True):
            specialite = input("Spécialité: ")
            localisation = input("Localisation: ")
            plage_pub = input(
                "Date de publication (sous la forme jour trois premières lettres du mois., année): "
            )
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite=specialite, localisation=localisation, plage_pub=plage_pub
            )
            if len(liste_stage) > 0:
                liste_stage_modif = {
                    "titre": [
                        textwrap.fill(liste_stage[stage][1], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "description": [
                        textwrap.fill(liste_stage[stage][2][0:300], 50)
                        for stage in range(0, len(liste_stage))
                    ],
                    "specialite": [
                        liste_stage[stage][3] for stage in range(0, len(liste_stage))
                    ],
                    "localisation": [
                        textwrap.fill(liste_stage[stage][4], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "date_publication": [
                        liste_stage[stage][8] for stage in range(0, len(liste_stage))
                    ],
                }
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
                    colalign=["center", "center", "center", "center", "center"],
                )
                print(table)
                # Proposer à l'utilisateur de parcourir la liste des voeux
                parcours = prompt(self.__parcourir_question)
                while parcours[0]:
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
                    HistoriqueService().ajouter_historique(
                        Session().email, recherche[6], recherche[1]
                    )
                    if Session().email != "adresse_mail_visiteur":
                        favori = prompt(self.__fav)
                        if favori[0] is True:
                            ListeEnvieService().ajouter_stage_listeEnvie_utilisateur(
                                Session().email,
                                recherche[6],
                                recherche[3],
                                recherche[1],
                                recherche[4],
                                recherche[7],
                            )
                    parcours = prompt(self.__revenir_menu)
            else:
                print("La recherche demandée n'a pas de résultats")

        elif (answers[0] is True) & (answers[1] is True) & (answers[2] is False):
            specialite = input("Spécialité: ")
            localisation = input("Localisation: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite=specialite, localisation=localisation
            )
            if len(liste_stage) > 0:
                liste_stage_modif = {
                    "titre": [
                        textwrap.fill(liste_stage[stage][1], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "description": [
                        textwrap.fill(liste_stage[stage][2][0:300], 50)
                        for stage in range(0, len(liste_stage))
                    ],
                    "specialite": [
                        liste_stage[stage][3] for stage in range(0, len(liste_stage))
                    ],
                    "localisation": [
                        textwrap.fill(liste_stage[stage][4], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "date_publication": [
                        liste_stage[stage][8] for stage in range(0, len(liste_stage))
                    ],
                }
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
                    colalign=["center", "center", "center", "center", "center"],
                )
                print(table)
                # Proposer à l'utilisateur de parcourir la liste des voeux
                parcours = prompt(self.__parcourir_question)
                while parcours[0]:
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
                    HistoriqueService().ajouter_historique(
                        Session().email, recherche[6], recherche[1]
                    )
                    if Session().email != "adresse_mail_visiteur":
                        favori = prompt(self.__fav)
                        if favori[0] is True:
                            ListeEnvieService().ajouter_stage_listeEnvie_utilisateur(
                                Session().email,
                                recherche[6],
                                recherche[3],
                                recherche[1],
                                recherche[4],
                                recherche[7],
                            )
                    parcours = prompt(self.__revenir_menu)
            else:
                print("La recherche demandée n'a pas de résultats")

        elif (answers[0] is True) & (answers[1] is False) & (answers[2] is True):
            specialite = input("Spécialité: ")
            plage_pub = input(
                "Date de publication (sous la forme jour trois premières lettres du mois., année): "
            )
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite=specialite, plage_pub=plage_pub
            )
            if len(liste_stage) > 0:
                liste_stage_modif = {
                    "titre": [
                        textwrap.fill(liste_stage[stage][1], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "description": [
                        textwrap.fill(liste_stage[stage][2][0:300], 50)
                        for stage in range(0, len(liste_stage))
                    ],
                    "specialite": [
                        liste_stage[stage][3] for stage in range(0, len(liste_stage))
                    ],
                    "localisation": [
                        textwrap.fill(liste_stage[stage][4], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "date_publication": [
                        liste_stage[stage][8] for stage in range(0, len(liste_stage))
                    ],
                }
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
                while parcours[0]:
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
                    HistoriqueService().ajouter_historique(
                        Session().email, recherche[6], recherche[1]
                    )
                    if Session().email != "adresse_mail_visiteur":
                        favori = prompt(self.__fav)
                        if favori[0] is True:
                            ListeEnvieService().ajouter_stage_listeEnvie_utilisateur(
                                Session().email,
                                recherche[6],
                                recherche[3],
                                recherche[1],
                                recherche[4],
                                recherche[7],
                            )
                    parcours = prompt(self.__revenir_menu)
            else:
                print("La recherche demandée n'a pas de résultats")

        elif (answers[0] is True) & (answers[1] is False) & (answers[2] is False):
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(specialite=specialite)
            if len(liste_stage) > 0:
                liste_stage_modif = {
                    "titre": [
                        textwrap.fill(liste_stage[stage][1], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "description": [
                        textwrap.fill(liste_stage[stage][2][0:300], 50)
                        for stage in range(0, len(liste_stage))
                    ],
                    "specialite": [
                        liste_stage[stage][3] for stage in range(0, len(liste_stage))
                    ],
                    "localisation": [
                        textwrap.fill(liste_stage[stage][4], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "date_publication": [
                        liste_stage[stage][8] for stage in range(0, len(liste_stage))
                    ],
                }
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
                while parcours[0]:
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
                    HistoriqueService().ajouter_historique(
                        Session().email, recherche[6], recherche[1]
                    )
                    if Session().email != "adresse_mail_visiteur":
                        favori = prompt(self.__fav)
                        if favori[0] is True:
                            ListeEnvieService().ajouter_stage_listeEnvie_utilisateur(
                                Session().email,
                                recherche[6],
                                recherche[3],
                                recherche[1],
                                recherche[4],
                                recherche[7],
                            )
                    parcours = prompt(self.__revenir_menu)
            else:
                print("La recherche demandée n'a pas de résultats")

        elif (answers[0] is False) & (answers[1] is True) & (answers[2] is True):
            localisation = input("Localisation: ")
            plage_pub = input(
                "Date de publication (sous la forme jour trois premières lettres du mois., année): "
            )
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                localisation=localisation, plage_pub=plage_pub
            )
            if len(liste_stage) > 0:
                liste_stage_modif = {
                    "titre": [
                        textwrap.fill(liste_stage[stage][1], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "description": [
                        textwrap.fill(liste_stage[stage][2][0:300], 50)
                        for stage in range(0, len(liste_stage))
                    ],
                    "specialite": [
                        liste_stage[stage][3] for stage in range(0, len(liste_stage))
                    ],
                    "localisation": [
                        textwrap.fill(liste_stage[stage][4], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "date_publication": [
                        liste_stage[stage][8] for stage in range(0, len(liste_stage))
                    ],
                }
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
                while parcours[0]:
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
                    HistoriqueService().ajouter_historique(
                        Session().email, recherche[6], recherche[1]
                    )
                    if Session().email != "adresse_mail_visiteur":
                        favori = prompt(self.__fav)
                        if favori[0] is True:
                            ListeEnvieService().ajouter_stage_listeEnvie_utilisateur(
                                Session().email,
                                recherche[6],
                                recherche[3],
                                recherche[1],
                                recherche[4],
                                recherche[7],
                            )
                    parcours = prompt(self.__revenir_menu)
            else:
                print("La recherche demandée n'a pas de résultats")

        elif (answers[0] is False) & (answers[1] is True) & (answers[2] is False):
            localisation = input("Localisation: ")
            specialite = "0"
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            if len(liste_stage) > 0:
                liste_stage_modif = {
                    "titre": [
                        textwrap.fill(liste_stage[stage][1], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "description": [
                        textwrap.fill(liste_stage[stage][2][0:300], 50)
                        for stage in range(0, len(liste_stage))
                    ],
                    "specialite": [
                        liste_stage[stage][3] for stage in range(0, len(liste_stage))
                    ],
                    "localisation": [
                        textwrap.fill(liste_stage[stage][4], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "date_publication": [
                        liste_stage[stage][8] for stage in range(0, len(liste_stage))
                    ],
                }
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
                while parcours[0]:
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
                    HistoriqueService().ajouter_historique(
                        Session().email, recherche[6], recherche[1]
                    )
                    if Session().email != "adresse_mail_visiteur":
                        favori = prompt(self.__fav)
                        if favori[0] is True:
                            ListeEnvieService().ajouter_stage_listeEnvie_utilisateur(
                                Session().email,
                                recherche[6],
                                recherche[3],
                                recherche[1],
                                recherche[4],
                                recherche[7],
                            )
                    parcours = prompt(self.__revenir_menu)
            else:
                print("La recherche demandée n'a pas de résultats")

        elif (answers[0] is False) & (answers[1] is False) & (answers[2] is True):
            plage_pub = input(
                "Date de publication (sous la forme jour trois premières lettres du mois., année): "
            )
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(plage_pub=plage_pub)
            if len(liste_stage) > 0:
                liste_stage_modif = {
                    "titre": [
                        textwrap.fill(liste_stage[stage][1], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "description": [
                        textwrap.fill(liste_stage[stage][2][0:300], 50)
                        for stage in range(0, len(liste_stage))
                    ],
                    "specialite": [
                        liste_stage[stage][3] for stage in range(0, len(liste_stage))
                    ],
                    "localisation": [
                        textwrap.fill(liste_stage[stage][4], 25)
                        for stage in range(0, len(liste_stage))
                    ],
                    "date_publication": [
                        liste_stage[stage][8] for stage in range(0, len(liste_stage))
                    ],
                }
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
                while parcours[0]:
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
                    HistoriqueService().ajouter_historique(
                        Session().email, recherche[6], recherche[1]
                    )
                    if Session().email != "adresse_mail_visiteur":
                        favori = prompt(self.__fav)
                        if favori[0] is True:
                            ListeEnvieService().ajouter_stage_listeEnvie_utilisateur(
                                Session().email,
                                recherche[6],
                                recherche[3],
                                recherche[1],
                                recherche[4],
                                recherche[7],
                            )
                    parcours = prompt(self.__revenir_menu)
            else:
                print("La recherche demandée n'a pas de résultats")

        else:
            print("Il est nécessaire de rentrer au moins l'un des deux")
            continu = prompt(self.__continuer)
            if continu[0] is True:
                return RechercheView()
        return Statut().def_statut(Session().statut)
