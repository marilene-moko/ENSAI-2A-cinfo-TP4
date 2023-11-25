from InquirerPy import prompt
from InquirerPy.validator import PasswordValidator

from view.abstract_view import AbstractView

from client.utilisateur_client import UtilisateurClient
from view.session import Session
from view.fct_statut import Statut
from dao.visiteur_dao import VisiteurDao


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
                "message": "Voulez-vous changer votre mot de passe? ",
                "default": False,
            },
        ]
        self.__questions_modif_mdp = [
            {
                "type": "password",
                "message": "Nouveau mot de passe (au moins 8 caractères dont un spécial, une majuscule et un chiffre): ",
                "validate": PasswordValidator(
                    length=8,
                    cap=True,
                    special=True,
                    number=True,
                    message="Le mot de passe fourni ne satisfait pas aux conditions demandées",
                ),
            }
        ]

    def display_info(self):
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        email = Session().email
        if answers[0] is True:
            modif_nom = input("Choisissez un nouveau nom: ")
            if UtilisateurClient.modifier_nom(email, modif_nom) is True:
                Session().nom = modif_nom
                Session().pseudo = Session().nom + " " + Session().prenom
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        else:
            Session().nom = Session().nom

        if answers[1] is True:
            modif_prenom = input("Choisissez un nouveau prénom: ")
            if UtilisateurClient.modifier_prenom(email, modif_prenom) is True:
                Session().prenom = modif_prenom
                Session().pseudo = Session().nom + " " + Session().prenom
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        else:
            Session().prenom = Session().prenom

        if answers[2] is True:
            # Utilisation de la même validation de mot de passe lors de la modification
            modif_mdp = prompt(self.__questions_modif_mdp)
            mot_de_passe = VisiteurDao.hash_mdp(
                modif_mdp[0]
            )  # Hash du nouveau mot de passe

            if UtilisateurClient.modifier_mdp(email, mot_de_passe) is True:
                Session().mot_de_passe = modif_mdp[0]
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        else:
            Session().mot_de_passe = Session().mot_de_passe

        return Statut.def_statut(Session().statut)
