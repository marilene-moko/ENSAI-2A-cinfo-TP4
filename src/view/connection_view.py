from InquirerPy import prompt

from view.abstract_view import AbstractView
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
        # if email in utilisateur:
        #    raiseValueError()
        Session().user_name = answers[1] + " " + answers[2]

        #if utilisateur = eleve:
            from view.ap_connexion_view_eleve import ApConnexionViewEleve
            return ApConnexionViewEleve()
        #elif utilisateur = prof:
            #from view.ap_connexion_view_prof import ApConnexionViewProf
            #return ApConnexionViewProf()
        #elif utilisateur = admin:
            #from view.ap_connexion_view_admin import ApConnexionViewAdmin
            #return ApConnexionViewAdmin()
