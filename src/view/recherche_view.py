from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from view.fct_statut import Statut

from dao.visiteur_dao import VisiteurDao
from client.utilisateur.visiteur.stage_client_visiteur import Stageclientvisiteur


class RechercheView(AbstractView):
    def __init__(self):
        self.__questions = [
            {"type": "input", "message": "Voulez-vous choisir votre spécialité? Y/N"},
            {"type": "input", "message": "Voulez-vous choisir votre localisation? Y/N"},
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
            affichage = Stageclientvisiteur().afficher_stage(liste_stage)
        elif (answers[0] == "Y") | (answers[1] == "Y"):
            localisation = input("Localisation: ")
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            affichage = Stageclientvisiteur().afficher_stage(liste_stage)
        elif (answers[0] == "N") | (answers[1] == "N"):
            localisation = input("Localisation: ")
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            affichage = Stageclientvisiteur().afficher_stage(liste_stage)

        Statut.def_statut(Session().email)
