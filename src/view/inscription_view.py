from InquirerPy import prompt

from view.abstract_view import AbstractView

from  dao.utilisateur_dao import UtilisateurDao

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
        self.nom = answers[1]
        self.prenom = answers[2]
        self.email = answers[0]
        self.mot_de_passe = answers[3]
        # if email in utilisateur:
        #    raiseValueError()

        from view.start_view import StartView

        return StartView()


if UtilisateurDao.email_exists(email):
    raise ValueError("Cet email existe déjà")
