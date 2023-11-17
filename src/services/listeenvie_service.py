from dao.listeenvie_dao import ListeEnvieDAO


class ListeEnvieService:
    @staticmethod
    def afficher_listeEnvie_utilisateur(adresse_mail):
        """
        Call the DAO function to retrieve and return the user's wishlist.
        """
        dao = ListeEnvieDAO()
        return dao.afficher_listeEnvie_utilisateur(adresse_mail)

    @staticmethod
    def supprimer_listeEnvie_utilisateur(adresse_mail, identifiant_voeu):
        """
        Call the DAO function to remove a wish from the user's wishlist.
        """
        dao = ListeEnvieDAO()
        return dao.supprimer_listeEnvie_utilisateur(adresse_mail, identifiant_voeu)

    @staticmethod
    def ajouter_stage_listeEnvie_utilisateur(
        adresse_mail, identifiant_stage, specialite, titre, localisation, employeur
    ):
        """
        Call the DAO function to add a stage to the user's wishlist.
        """
        dao = ListeEnvieDAO()
        return dao.ajouter_stage_listeEnvie_utilisateur(
            adresse_mail, identifiant_stage, specialite, titre, localisation, employeur
        )

    @staticmethod
    def importer_voeux(adresse_mail):
        """
        Call the DAO function to import wishlist data.
        """
        dao = ListeEnvieDAO()
        return dao.importer_voeux(adresse_mail)

    @staticmethod
    def exporter_voeux(adresse_mail):
        """
        Call the DAO function to export wishlist data.
        """
        dao = ListeEnvieDAO()
        return dao.exporter_voeux(adresse_mail)
