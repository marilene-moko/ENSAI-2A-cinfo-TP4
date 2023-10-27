from InquirerPy import prompt

from view.abstract_view import AbstractView

from client.visiteur_client import VisiteurClient


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
        mot_de_passe = VisiteurClient.hash_mdp(self, answers[3])
        if (
            VisiteurClient.inscription(
                self=self,
                adresse_mail=answers[0],
                nom=answers[1],
                prenom=answers[2],
                mot_de_passe=mot_de_passe,
            )
            is True
        ):
            print("Votre compte a bien été créé")

        else:
            from view.start_view import StartView

            return StartView()
            print(
                "L'email choisi existe déjà. Veuillez en choisir un autre s'il-vous-plaît."
            )
