from dao.historique_dao import HistoriqueDAO


class HistoriqueService:
    def afficher_historique_utilisateur(self, adresse_mail):
        """
        Call the DAO function to retrieve and return the user's history.
        """
        dao = HistoriqueDAO()
        return dao.afficher_historique_utilisateur(self, adresse_mail)

    def importer_historique(self, adresse_mail):
        """
        Call the DAO function to import history data.
        """
        dao = HistoriqueDAO()
        return dao.importer_historique(self, adresse_mail)

    def exporter_historique(self, adresse_mail):
        """
        Call the DAO function to export history data.
        """
        dao = HistoriqueDAO()
        return dao.exporter_historique(self, adresse_mail)

    def supprimer_historique_utilisateur(self, adresse_mail):
        """
        Call the DAO function to delete user's history.
        """
        dao = HistoriqueDAO()
        return dao.supprimer_historique_utilisateur(self, adresse_mail)

    def ajouter_historique(self, adresse_mail, URL_page):
        """
        Call the DAO function to add history data.
        """
        dao = HistoriqueDAO()
        return dao.ajouter_historique(self, adresse_mail, URL_page)
