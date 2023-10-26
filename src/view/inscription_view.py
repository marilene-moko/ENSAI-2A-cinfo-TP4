from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from dao.visiteur_dao import VisiteurDao


class InscriptionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {"type": "input", "message": "Email:"},
            {"type": "input", "message": "Nom: "},
            {"type": "input", "message": "Prénom: "},
            {"type": "input", "message": "Mot de passe: "},
        ]

    def display_info(self):
        print("Veuillez renseigner les champs suivants:")

    def make_choice(self):
        answers = prompt(self.__questions)
        mot_de_passe = VisiteurDao().hash_mdp(answers[3])
        if (
            VisiteurDao().inscription(
                adresse_mail=answers[0],
                nom=answers[1],
                prenom=answers[2],
                mot_de_passe=mot_de_passe,
            )
            is True
        ):
            print("Votre compte a bien été créé")
            Session().nom = answers[1]
            Session().prenom = answers[2]
            Session().email = answers[0]
            Session().pseudo = Session().nom + " " + Session().prenom
            Session().mot_de_passe = answers[3]
        else:
            print("Une erreur est survenue. Veuillez réessayer ultérieurement.")
        from view.start_view import StartView

        return StartView()
