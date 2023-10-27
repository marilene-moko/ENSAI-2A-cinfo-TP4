from dao.historique_dao import HistoriqueDAO

class Historique :
    def __init__(
        self,
        id_historique,
        historique_rechercher
    ):

        self.id_historique = id_historique
        self.historique_rechercher = historique_rechercher

    def afficher_historique_utilisateur(adresse_mail):
        """ 
        Méthode qui permet à l'utilisateur d'afficher son historique.

        Paramètre:
            adresse_mail : str : l'adresse mail de l'utilisateur

        Retour : 
            l'historique
        """" 
        return HistoriqueDAO.afficher_historique_utilisateur(adresse_mail)

    def importer_historique(adresse_mail):
        """ 
        Méthode qui permet à l'utilisateur d'importer un historique.

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'import

        Retour : 
            un booléen qui indique si la tâche a bien été effectuée
        """
        return HistoriqueDAO.importer_historique(adresse_mail)

    def exporter_historique(adresse_mail):
        """ 
        Méthode qui permet à l'utilisateur d'exporter son historique.

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'export

        Retour : 
            un booléen qui indique si la tâche a bien été effectuée
        """
        return HistoriqueDAO.exporter_historique(adresse_mail)

    def supprimer_historique(email):
        """ 
        Méthode qui permet à l'utilisateur de supprimer son historique.

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire la suppression

        Retour : 
            un booléen qui indique si la tâche a bien été effectuée
        """
        return HistoriqueDAO.supprimer_historique_utilisateur(email)

    def ajouter_historique(email, URL_page):
        """ 
        Méthode qui permet à l'utilisateur d'ajouter un stage à son historique.

        Paramètre :
            adresse_mail : str : l'adresse mail de l'utilisateur qui souhaite faire l'ajout
            URL_page : str : l'URL de la page du stage que l'utilisateur souhaite ajouter

        Retour : 
            un booléen qui indique si la tâche a bien été effectuée
        """
        return HistoriqueDAO.ajouter_historique(email, URL_page)
    
    