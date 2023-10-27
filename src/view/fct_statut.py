class Statut:
    def __init__(self):
        pass

    @staticmethod
    def def_statut(statut):
        if statut == "eleve":
            from view.ap_connexion_view_eleve import ApConnexionViewEleve

            return ApConnexionViewEleve()
        elif statut == "professeur":
            from view.ap_connexion_view_prof import ApConnexionViewProf

            return ApConnexionViewProf()
        else:
            from view.ap_connexion_view_admin import ApConnexionViewAdmin

            return ApConnexionViewAdmin()
