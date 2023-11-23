from dao.historique_dao import HistoriqueDAO


class HistoriqueService:
    @staticmethod
    def afficher_historique_utilisateur(adresse_mail):
        """
        Call the DAO function to retrieve and return the user's history.
        """
        dao = HistoriqueDAO()
        return dao.afficher_historique_utilisateur(adresse_mail)

    @staticmethod
    def importer_historique(adresse_mail):
        """
        Call the DAO function to import history data.
        """
        dao = HistoriqueDAO()
        return dao.importer_historique(adresse_mail)

    @staticmethod
    def exporter_historique(adresse_mail):
        """
        Call the DAO function to export history data.
        """
        dao = HistoriqueDAO()
        return dao.exporter_historique(adresse_mail)

    @staticmethod
    def supprimer_historique_utilisateur(adresse_mail):
        """
        Call the DAO function to delete user's history.
        """
        dao = HistoriqueDAO()
        return dao.supprimer_historique_utilisateur(adresse_mail)

    @staticmethod
    def ajouter_historique(adresse_mail, URL_page, titre):
        """
        Call the DAO function to add history data.
        """
        dao = HistoriqueDAO()
        return dao.ajouter_historique(adresse_mail, URL_page, titre)
