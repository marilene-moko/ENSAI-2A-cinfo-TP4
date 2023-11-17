from view.ap_connexion_view_admin import ApConnexionViewAdmin
from view.ap_connexion_view_prof import ApConnexionViewProf
from view.ap_sans_authentification_view import ApSansAuthentificationView
from view.ap_connexion_view_eleve import ApConnexionViewEleve


class Statut:
    def __init__(self):
        pass

    @staticmethod
    def def_statut(statut: str):
        if statut == "eleve":
            return ApConnexionViewEleve()
        elif statut == "professeur":
            return ApConnexionViewProf()
        elif statut == "administrateur":
            return ApConnexionViewAdmin()
        else:
            return ApSansAuthentificationView()
