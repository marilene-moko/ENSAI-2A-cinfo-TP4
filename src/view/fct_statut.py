class Statut:
    def __init__(self, statut):
        self.statut = statut

    def def_statut(self, statut):
        if statut == "eleve":
            from view.ap_connexion_view_eleve import ApConnexionViewEleve

            return ApConnexionViewEleve()
        elif statut == "professeur":
            from view.ap_connexion_view_prof import ApConnexionViewProf

            return ApConnexionViewProf()
        else:
            from view.ap_connexion_view_admin import ApConnexionViewAdmin

            return ApConnexionViewAdmin()
