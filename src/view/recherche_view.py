from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from dao.visiteur_dao import VisiteurDao
from src.client.utilisateur.visiteur.stage_client_visiteur import Stageclientvisiteur


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
            liste_stage = Stageclientvisiteur().get_stage(specialite, localisation)
            affichage = Stageclientvisiteur().afficher_stage(liste_stage)
        elif (answers[0] == "Y") | (answers[1] == "Y"):
            localisation = input("Localisation: ")
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage(specialite, localisation)
            affichage = Stageclientvisiteur().afficher_stage(liste_stage)
        elif (answers[0] == "N") | (answers[1] == "N"):
            localisation = input("Localisation: ")
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage(specialite, localisation)
            affichage = Stageclientvisiteur().afficher_stage(liste_stage)

        if Session().statut == "eleve":
            from view.ap_connexion_view_eleve import ApConnexionViewEleve

            return ApConnexionViewEleve()
        elif Session().statut == "prof":
            from view.ap_connexion_view_prof import ApConnexionViewProf

            return ApConnexionViewProf()
        else:
            from view.ap_connexion_view_admin import ApConnexionViewAdmin

            return ApConnexionViewAdmin()
