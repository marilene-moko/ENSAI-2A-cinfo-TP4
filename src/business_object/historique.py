from dao.historique_dao import *

class Historique :
    def __init__(
        self,
        id_historique,
        historique_rechercher
    ):

        self.id_historique = id_historique
        self.historique_rechercher = historique_rechercher

    def afficherHistorique(self, utilisateur):
        """ 
        Méthode qui permet à l'utilisateur d'afficher son historique

        retourne : l'historique
        """" 
        return afficher_historique_utilisateur(self, utilisateur)

    def importer_historique(self, utilisateur):
        """ 
        Méthode qui permet à l'utilisateur d'importer son historique
        """
        return importer_historique(self, utilisateur)

    def exporter_historique(self, utilisateur):
        """ 
        Méthode qui permet à l'utilisater d'exporter son historique
        """ 
        return exporter_historique(self, utilisateur)

########### il manque la fonction supprimer historique ###########