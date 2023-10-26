from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from dao.utilisateur_dao import UtilisateurDao


class ProfilView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().user_name}",
                "choices": [
                    "Afficher son profil",
                    "Modifier son profil",
                    "Supprimer son profil",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Afficher son profil":
            

        elif reponse["choix"] == "Modifier son profil":
            from view.modif_profil_view import ModifProfilView

            return ModifProfilView()


        elif reponse["choix"] == "Supprimer son profil":
            if UtilisateurDao().supprimer_profil(Session().email) is True:
                print("Votre compte a bien été supprimé")
                from view.start_view import StartView
                return StartView()
            else:
                print("Une erreur est survenue. Veuillez essayer ultérieurement.")
                if Session().statut == "eleve":
                    from view.ap_connexion_view_eleve import ApConnexionViewEleve

                    return ApConnexionViewEleve()
                elif Session().statut == "prof":
                    from view.ap_connexion_view_prof import ApConnexionViewProf

                    return ApConnexionViewProf()
                else:
                    from view.ap_connexion_view_admin import ApConnexionViewAdmin

                    return ApConnexionViewAdmin()
            
