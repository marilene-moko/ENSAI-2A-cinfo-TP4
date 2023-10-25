from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from dao.utilisateur_dao import UtilisateurDao


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
        utilisateur = UtilisateurDao().get_utilisateur_by_email(self.email)

        if utilisateur["statut"] == "eleve":
            from view.ap_connexion_view_eleve import ApConnexionViewEleve

            return ApConnexionViewEleve()
        elif utilisateur["statut"] == "professeur":
            from view.ap_connexion_view_prof import ApConnexionViewProf

            return ApConnexionViewProf()
        elif utilisateur["statut"] == "administrateur":
            from view.ap_connexion_view_admin import ApConnexionViewAdmin

            return ApConnexionViewAdmin()

    if UtilisateurDao.utilisateur_exists(answers[0], answers[1]):
        raise ValueError("Email ou mot de passe incorrect")
