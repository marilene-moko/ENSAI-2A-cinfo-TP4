from dao.historique_dao import HistoriqueDAO

class Historique :
    def __init__(
        self,
        id_historique,
        historique_rechercher
    ):

        self.id_historique = id_historique
        self.historique_rechercher = historique_rechercher

    def afficher_historique_utilisateur(email):
        """ 
        Méthode qui permet à l'utilisateur d'afficher son historique

        retourne : l'historique
        """" 
        return HistoriqueDAO.afficher_historique_utilisateur(email)

    def importer_historique(email):
        """ 
        Méthode qui permet à l'utilisateur d'importer son historique
        """
        return HistoriqueDAO.importer_historique(email)

    def exporter_historique(email):
        """ 
        Méthode qui permet à l'utilisater d'exporter son historique
        """ 
        return HistoriqueDAO.exporter_historique(email)

    def supprimer_historique(email):

        return HistoriqueDAO.supprimer_historique_utilisateur(email)

    def ajouter_historique(email, URL_page):

        return HistoriqueDAO.ajouter_historique(email, URL_page)
    
    