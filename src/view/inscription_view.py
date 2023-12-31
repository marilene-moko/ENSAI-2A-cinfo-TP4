from InquirerPy import prompt
from InquirerPy.validator import PasswordValidator

from view.abstract_view import AbstractView

from client.visiteur_client import VisiteurClient


class InscriptionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {"type": "input", "message": "Email:"},
            {"type": "input", "message": "Nom: "},
            {"type": "input", "message": "Prénom: "},
            {
                "type": "password",
                "message": "Mot de passe (au moins 8 caractères dont un spécial, une majuscule et un chiffre): ",
                "validate": PasswordValidator(
                    length=8,
                    cap=True,
                    special=True,
                    number=True,
                    message="Le mot de passe fournit ne satisfait pas aux conditions demandées",
                ),
            },
        ]

    def display_info(self):
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        mot_de_passe = VisiteurClient.hash_mdp(answers[3])
        if (
            VisiteurClient.inscription(
                adresse_mail=answers[0],
                nom=answers[1],
                prenom=answers[2],
                mot_de_passe=mot_de_passe,
            )
            is True
        ):
            print("Votre compte a bien été créé")
            from view.start_view_sans_logo import StartViewSimple

            return StartViewSimple()

        else:
            print(
                "L'email choisi existe déjà. Veuillez en choisir un autre s'il-vous-plaît."
            )
            from view.start_view_sans_logo import StartViewSimple

            return StartViewSimple()
