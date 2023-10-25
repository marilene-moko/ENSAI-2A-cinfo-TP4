from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.historique_dao import HistoriqueDao

class VisiteurDao(metaclass=Singleton):
    def inscription(self, utilisateur) -> bool:
        """
        Add an utilisateur to the database
        """
        created = False

        # Get the id type
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT *                                         '
                    'FROM "Projet_Info".Personne                      '
                    'WHERE adresse_mail = %(email)s;                  ',
                    {
                        "adresse_mail": email
                    },
                )
                res = cursor.fetchone()
        if not res:
            raise ValueError(
                "L'email choisi existe déjà. Veuillez en choisir un autre s'il-vous-plaît."
            )
        else:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO "Projet_Info".Personne (email, nom, prenom, mdp)             '
                        'VALUES                                                                   '
                        '(%(email)s, %(nom)s, %(prenom)s, %(mdp)s);                               ',
                        {
                            "email": email,
                            "nom": nom,
                            "prenom": prenom,
                            "mdp": mdp,
                            "statut": statut
                        },
                    )
                    res = cursor.fetchone()
            if res:
                created = True

            return created

    def voir_historique(self):
        return HistoriqueDao().voir_historique()

    def exporter_historique(self):
        return HistoriqueDao().exporter_historique()




if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv
    from business_object.attack.physical_attack import PhysicalFormulaAttack

    dotenv.load_dotenv(override=True)

    # Création d'un utilisateur et ajout en BDD
    mon_utilisateur = PhysicalFormulaAttack(
        nom=Toto,
        prenom=,
        email=,
        mdp=
    )

    succes = UtilisateurDao().add_utilisateur(mon_utilisateur)
    print("Utilisateur created in database : " + str(succes))

