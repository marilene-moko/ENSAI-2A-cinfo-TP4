from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from view.fct_statut import Statut
from client.utilisateur_client import UtilisateurClient


class ProfilView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Afficher son profil",
                    "Modifier son profil",
                    "Supprimer son profil",
                    "Revenir à la page précédente",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Afficher son profil":
            print("Nom :")
            print(Session().nom)
            print("\n")
            print("Prénom : ")
            print(Session().prenom)
            print("\n")
            print("Email :  ")
            print(Session().email)
            print("\n")
            print("Pseudo :  ")
            print(Session().pseudo)
            print("\n")
            print("\n")
            print("Statut :")
            print(Session().statut)
            print("\n")
            return Statut().def_statut(Session().statut)

        elif reponse["choix"] == "Modifier son profil":
            from view.modif_profil_view import ModifProfilView

            return ModifProfilView()

        elif reponse["choix"] == "Supprimer son profil":
            if (
                UtilisateurClient(
                    identifiant_personne=0,
                    nom=Session().nom,
                    prenom=Session().prenom,
                    adresse_mail=Session().email,
                    mot_de_passe=Session().mot_de_passe,
                ).supprimer_profil(Session().email)
                is True
            ):
                print("Votre compte a bien été supprimé")
                from view.start_view_sans_logo import StartViewSimple

                return StartViewSimple()
            else:
                print("Une erreur est survenue. Veuillez essayer ultérieurement.")
                return Statut.def_statut(Session().statut)

        elif reponse["choix"] == "Revenir à la page précédente":
            return Statut.def_statut(Session().statut)
