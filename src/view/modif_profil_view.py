from InquirerPy import prompt

from view.abstract_view import AbstractView

from dao.utilisateur_dao import UtilisateurDao
from view.session import Session


class ModifProfilView(AbstractView):
    def __init__(self):
        self.__questions = [
            {"type": "input", "message": "Voulez-vous changer votre nom? Y/N "},
            {"type": "input", "message": "Voulez-vous changer votre prénom? Y/N "},
            {
                "type": "input",
                "message": "Voulez-vous changer votre mot de passe? Y/N ",
            },
        ]

    def display_info(self):
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        email = Session().email
        if answers[0] == "Y":
            modif_nom = input("Choisissez un nouveau nom")
            if UtilisateurDao.modifier_nom(email, modif_nom) is True:
                Session().nom = modif_nom
                Session().pseudo = Session().nom + " " + Session().prenom
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        elif answers[0] == "N":
            Session().nom = Session().nom
        else:
            raise ValueError("Vous devez répondre par Y ou N")

        if answers[1] == "Y":
            modif_prenom = input("Choisissez un nouveau prénom")
            if UtilisateurDao.modifier_prenom(email, modif_prenom) is True:
                Session().prenom = modif_prenom
                Session().pseudo = Session().nom + " " + Session().prenom
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        elif answers[1] == "N":
            Session().prenom = Session().prenom
        else:
            raise ValueError("Vous devez répondre par Y ou N")

        if answers[2] == "Y":
            modif_mdp = input("Choisissez un nouveau mot de passe")
            if UtilisateurDao.modifier_mdp(email, modif_mdp) is True:
                Session().mot_de_passe = modif_mdp
            else:
                print(
                    "Votre modification n'a pas pu être enregistrée. Veuillez réessayer s'il-vous-plaît."
                )
        elif answers[2] == "N":
            Session().mot_de_passe = Session().mot_de_passe
        else:
            raise ValueError("Vous devez répondre par Y ou N")

        if Session().statut == "eleve":
            from view.ap_connexion_view_eleve import ApConnexionViewEleve

            return ApConnexionViewEleve()
        elif Session().statut == "prof":
            from view.ap_connexion_view_prof import ApConnexionViewProf

            return ApConnexionViewProf()
        else:
            from view.ap_connexion_view_admin import ApConnexionViewAdmin

            return ApConnexionViewAdmin()
