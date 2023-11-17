from view.ap_connexion_view_admin import ApConnexionViewAdmin
from view.ap_connexion_view_prof import ApConnexionViewProf
from view.ap_sans_authentification_view import ApSansAuthentificationView
from view.ap_connexion_view_eleve import ApConnexionViewEleve


class Statut:
    def __init__(self):
        pass

    @staticmethod
    def def_statut(statut: str):
        print("Statut: " + statut)
        if statut == "eleve":
            print("Eleve detected")

            return ApConnexionViewEleve()
        elif statut == "professeur":
            print("Prof detected")

            return ApConnexionViewProf()
        elif statut == "administrateur":
            print("Admin detected")

            return ApConnexionViewAdmin()
        else:
            print("Visiteur detected")

            return ApSansAuthentificationView()
