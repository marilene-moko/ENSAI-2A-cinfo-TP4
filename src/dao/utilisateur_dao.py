from typing import List, Optional

from dao.db_connection import DBConnection
from dao.visiteur_dao import VisiteurDao
from dao.historique_dao import HistoriqueDao


class UtilisateurDao(VisiteurDao):
    def utilisateur_exists(self, email: str, mdp: str):
        """
        Regarder si l'utilisateur existe bien
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                       "
                    'FROM "Projet_Info".Personne                                '
                    " WHERE email=%(email)s   AND mdp=%(mdp)s       ",
                    {"email": email, "mdp": mdp},
                )
                res = cursor.fetchone()

        utilisateur = None

        if res:
            utilisateur = Utilisateur().instantiate_utilisateur(
                email=res["email"],
                nom=res["nom"],
                prenom=res["prenom"],
                mdp=res["mot de passe"],
            )

        return utilisateur

    def update_utilisateur(self, utilisateur) -> bool:
        updated = False

        # Get the email
        email = utilisateur["email"]
        if email is None:
            return updated

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE Personne                                      "
                    "   SET email = %(email)s,                            "
                    "       nom = %(nom)s,                                "
                    "       prenom = %(prenom)s,                          "
                    "       mdp = %(mdp)s,                                "
                    " WHERE email = %(email)s                             ",
                    {
                        "email": email,
                        "nom": utilisateur["nom"],
                        "prenom": utilisateur["prenom"],
                        "mdp": utilisateur["mdp"],
                        "statut": utilisateur["statut"],
                    },
                )
                if cursor.rowcount:
                    updated = True
        return updated

        def modifier_historique(self):
            return HistoriqueDao().modifier_historique()


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
