from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class InscriptionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "email": "email",
                "message": "What's your pseudo",
                "nom": "nom",
                "prénom": "prénom",
                "mot de passe": "mot de passe",
                "choices": "liste_réponse",
            }
        ]

    def display_info(self):
        print(f"Veuillez renseigner les champs suivants dans l'ordre:
        \n Nom
        \n Prénom
        \n email
        \n mot de passe")

    def make_choice(self):
        answers = prompt(self.__questions)
        self.nom = answers[3]
        self.prenom = answer[4]
        self.email = answer[5]
        self.mdp = answers[6]
        if email in utilisateur:
            raiseValueError()
        Session().user_name = answers["nom" + " " + "prénom"]

        from view.start_view import StartView

        return StartView()
