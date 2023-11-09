from InquirerPy import prompt

from view.abstract_view import AbstractView

from client.utilisateur_client import UtilisateurClient
from view.session import Session


class ConnectionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {"type": "input", "message": "Email:"},
            {"type": "password", "message": "Mot de passe: "},
        ]
        self.__revenir_menu = [
            {
                "type": "confirm",
                "message": "Voulez-vous réessayer de vous connecter:",
                "default": True,
            }
        ]

    def display_info(self):
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        mdp = UtilisateurClient.hash_mdp(answers[1])
        utilisateur = UtilisateurClient.utilisateur_exists(
            adresse_mail=answers[0], mot_de_passe=mdp
        )
        if utilisateur is not None:
            if utilisateur.statut == "eleve":
                Session().nom = utilisateur.nom
                Session().prenom = utilisateur.prenom
                Session().pseudo = Session().nom + " " + Session().prenom
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "eleve"

                from view.ap_connexion_view_eleve import ApConnexionViewEleve

                return ApConnexionViewEleve()

            elif utilisateur.statut == "professeur":
                Session().nom = utilisateur.nom
                Session().prenom = utilisateur.prenom
                Session().pseudo = Session().nom + " " + Session().prenom
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "professeur"

                from view.ap_connexion_view_prof import ApConnexionViewProf

                return ApConnexionViewProf()

            elif utilisateur.statut == "administrateur":
                Session().nom = utilisateur.nom
                Session().prenom = utilisateur.prenom
                Session().pseudo = Session().nom + " " + Session().prenom
                Session().email = answers[0]
                Session().mot_de_passe = answers[1]
                Session().statut = "administrateur"

                from view.ap_connexion_view_admin import ApConnexionViewAdmin

                return ApConnexionViewAdmin()
        else:
            print("L'email et/ou le mot de passe est incorrect")
            quest = prompt(self.__revenir_menu)
            if quest is True:
                from star_view import StartView

                return StartView()
            else:
                return ConnectionView()
