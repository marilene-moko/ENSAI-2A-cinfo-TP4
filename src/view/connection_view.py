from InquirerPy import prompt

from view.abstract_view import AbstractView

from dao.utilisateur_dao import UtilisateurDao
from view.session import Session


class ConnectionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {"type": "input", "message": "Email:"},
            {"type": "input", "message": "Mot de passe: "},
        ]

    def display_info(self):
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        self.email = answers[0]
        self.mot_de_passe = answers[1]
        return self.email

    def authentification_reussie(self):
        answers = prompt(self.__questions)
        utilisateur = UtilisateurDao.utilisateur_exists(answers[0], answers[1])
        if utilisateur is not None:
            if utilisateur["statut"] == "eleve":
                Session().user_name = utilisateur["nom"] + " " + utilisateur["prenom"]
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "eleve"

                from view.ap_connexion_view_eleve import ApConnexionViewEleve

                return ApConnexionViewEleve()

            elif utilisateur["statut"] == "professeur":
                Session().user_name = utilisateur["nom"] + " " + utilisateur["prenom"]
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "professeur"

                from view.ap_connexion_view_prof import ApConnexionViewProf

                return ApConnexionViewProf()

            elif utilisateur["statut"] == "administrateur":
                Session().user_name = utilisateur["nom"] + " " + utilisateur["prenom"]
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "administrateur"

                from view.ap_connexion_view_admin import ApConnexionViewAdmin

                return ApConnexionViewAdmin()
        else:
            raise ValueError("L'email et/ou le mot de passe est incorrect")
