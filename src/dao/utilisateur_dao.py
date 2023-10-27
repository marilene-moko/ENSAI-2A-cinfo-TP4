from typing import List, Optional

from client.utilisateur.utilisateur.utilisateur_factory import UtilisateurFactory
from dao.db_connection import DBConnection
from dao.visiteur_dao import VisiteurDao
from dao.historique_dao import HistoriqueDAO


class UtilisateurDao(VisiteurDao):
    @staticmethod
    def utilisateur_exists(adresse_mail: str, mot_de_passe: str):
        """
        Regarder si l'utilisateur existe bien
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                       "
                    'FROM "Projet_Info".Personne                    '
                    " WHERE adresse_mail=%(adresse_mail)s   AND mot_de_passe=%(mot_de_passe)s",
                    {"adresse_mail": adresse_mail, "mot_de_passe": mot_de_passe},
                )
                res = cursor.fetchone()

        utilisateur = None

        if res:
            utilisateur = UtilisateurFactory.instantiate_utilisateur(
                email=res["adresse_mail"],
                nom=res["nom"],
                prenom=res["prenom"],
                mdp=res["mot_de_passe"],
            )

        return utilisateur

    @staticmethod
    def afficher_profil(adresse_mail, pseudo, nom, prenom, mot_de_passe):
        print(f"Voici les informations de votre profil: {adresse_mail}")

    @staticmethod
    def modifier_nom(adresse_mail, modification) -> bool:
        updated = False

        # Get the email
        if adresse_mail is None:
            return updated

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    nom = %(modification)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": adresse_mail, "nom": modification},
                )
                if cursor.rowcount:
                    updated = True
        return updated

    @staticmethod
    def modifier_prenom(adresse_mail, modification) -> bool:
        updated = False

        # Get the email
        if adresse_mail is None:
            return updated

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    prenom = %(modification)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": adresse_mail, "prenom": modification},
                )
                if cursor.rowcount:
                    updated = True
        return updated

    @staticmethod
    def modifier_mdp(adresse_mail, modification) -> bool:
        updated = False

        # Get the email
        if adresse_mail is None:
            return updated

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    mot_de_passe = %(modification)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": adresse_mail, "mot_de_passe": modification},
                )
                if cursor.rowcount:
                    updated = True
        return updated

<<<<<<< HEAD
    @staticmethod
    def supprimer_profil(adresse_mail):
=======
    def supprimer_profil(self, adresse_mail):
>>>>>>> c33b9ac583e681acb5890c728bd54a6a3e2532bb
        supp = False

        if adresse_mail is None:
            return supp

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'DELETE FROM "Projet_Info".Personne                  '
                    "WHERE adresse_mail = %(adresse_mail)s;                            ",
                )
                if cursor.rowcount:
                    supp = True
        return supp


""" 
if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv
    from business_object.attack.physical_attack import PhysicalFormulaAttack

    dotenv.load_dotenv(override=True)

    # Création d'une attaque et ajout en BDD
    mon_utilisateur = PhysicalFormulaAttack(
        nom=,
        prenom=,
        email=,
        mdp=
    )

    succes = UtilisateurDao().add_utilisateur(mon_utilisateur)
    print("Utilisateur created in database : " + str(succes))
 """
