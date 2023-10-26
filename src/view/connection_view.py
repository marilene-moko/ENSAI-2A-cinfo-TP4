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
        utilisateur = UtilisateurDao.utilisateur_exists(
            self=self, email=answers[0], mdp=answers[1]
        )
        if utilisateur is not None:
            if utilisateur.statut == "eleve":
                Session().nom = utilisateur["nom"]
                Session().prenom = utilisateur["prenom"]
                Session().pseudo = Session().nom + " " + Session().prenom
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "eleve"

                from view.ap_connexion_view_eleve import ApConnexionViewEleve

                return ApConnexionViewEleve()

            elif utilisateur.statut == "professeur":
                Session().nom = utilisateur["nom"]
                Session().prenom = utilisateur["prenom"]
                Session().pseudo = Session().nom + " " + Session().prenom
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "professeur"

                from view.ap_connexion_view_prof import ApConnexionViewProf

                return ApConnexionViewProf()

            elif utilisateur.statut == "administrateur":
                Session().nom = utilisateur["nom"]
                Session().prenom = utilisateur["prenom"]
                Session().pseudo = Session().nom + " " + Session().prenom
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "administrateur"

                from view.ap_connexion_view_admin import ApConnexionViewAdmin

                return ApConnexionViewAdmin()
        else:
            print("L'email et/ou le mot de passe est incorrect")
            from view.start_view import StartView

            return StartView()
