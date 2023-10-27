from dao.listeenvie_dao import ListeEnvieDAO


class ListeEnvieService:
    def afficher_listeEnvie_utilisateur(self, adresse_mail):
        """
        Call the DAO function to retrieve and return the user's wishlist.
        """
        dao = ListeEnvieDAO()
        return dao.afficher_listeEnvie_utilisateur(self, adresse_mail)

    def supprimer_listeEnvie_utilisateur(self, adresse_mail, identifiant_voeu):
        """
        Call the DAO function to remove a wish from the user's wishlist.
        """
        dao = ListeEnvieDAO()
        return dao.supprimer_listeEnvie_utilisateur(
            self, adresse_mail, identifiant_voeu
        )

    def ajouter_stage_listeEnvie_utilisateur(self, adresse_mail, identifiant_stage):
        """
        Call the DAO function to add a stage to the user's wishlist.
        """
        dao = ListeEnvieDAO()
        return dao.ajouter_stage_listeEnvie_utilisateur(
            self, adresse_mail, identifiant_stage
        )

    def importer_voeux(self, adresse_mail):
        """
        Call the DAO function to import wishlist data.
        """
        dao = ListeEnvieDAO()
        return dao.importer_voeux(self, adresse_mail)

    def exporter_voeux(self, adresse_mail):
        """
        Call the DAO function to export wishlist data.
        """
        dao = ListeEnvieDAO()
        return dao.exporter_voeux(self, adresse_mail)
