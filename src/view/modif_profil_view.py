from InquirerPy import prompt

from view.abstract_view import AbstractView

from client.utilisateur_client import UtilisateurClient
from view.session import Session
from view.fct_statut import Statut


class ModifProfilView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "confirm",
                "message": "Voulez-vous changer votre nom? ",
                "default": False,
            },
            {
                "type": "confirm",
                "message": "Voulez-vous changer votre prénom? ",
                "default": False,
            },
            {
                "type": "confirm",
                "message": "Voulez-vous changer votre mot de passe? Y/N ",
                "default": False,
            },
        ]

    def display_info(self):
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        email = Session().email
        if answers[0] is True:
            modif_nom = input("Choisissez un nouveau nom")
            if UtilisateurClient.modifier_nom(email, modif_nom) is True:
                Session().nom = modif_nom
                Session().pseudo = Session().nom + " " + Session().prenom
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        elif answers[0] is False:
            Session().nom = Session().nom
        else:
            print("Vous devez répondre par Y ou N")

        if answers[1] is True:
            modif_prenom = input("Choisissez un nouveau prénom")
            if UtilisateurClient.modifier_prenom(email, modif_prenom) is True:
                Session().prenom = modif_prenom
                Session().pseudo = Session().nom + " " + Session().prenom
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        elif answers[1] is False:
            Session().prenom = Session().prenom
        else:
            print("Vous devez répondre par Y ou N")

        if answers[2] is True:
            modif_mdp = input("Choisissez un nouveau mot de passe")
            if UtilisateurClient.modifier_mdp(email, modif_mdp) is True:
                Session().mot_de_passe = modif_mdp
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        elif answers[2] is False:
            Session().mot_de_passe = Session().mot_de_passe
        else:
            print("Vous devez répondre par Y ou N")

        Statut.def_statut(self, Session().statut)
