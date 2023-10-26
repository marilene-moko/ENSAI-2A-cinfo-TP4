from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.historique_dao import HistoriqueDAO


import hashlib


class VisiteurDao(metaclass=Singleton):
    def hash_mdp(self, mdp):
        # Créez un objet de hachage SHA-256
        hasher = hashlib.sha256()

        # Mettez le mot de passe dans l'objet de hachage
        hasher.update(mdp.encode("utf-8"))

        # Récupérez la valeur de hachage (représentation hexadécimale)
        hashed_mdp = hasher.hexdigest()

        return hashed_mdp

    def inscription(
        self, adresse_mail, nom, prenom, mot_de_passe, statut="eleve"
    ) -> bool:
        """
        Add an utilisateur to the database
        """
        created = False

        # hacher le mot de passe
        mdp_hache = self.hash_mdp(mot_de_passe)

        # Get the id type
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                         "
                    'FROM "Projet_Info".Personne                      '
                    "WHERE adresse_mail = %(adresse_mail)s;                  ",
                    {"adresse_mail": adresse_mail},
                )
                res = cursor.fetchone()
        if res:
            return created
        else:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO "Projet_Info".Personne (adresse_mail, nom, prenom, mot_de_passe, statut)'
                        "VALUES                                                                      "
                        "(%(adresse_mail)s, %(nom)s, %(prenom)s, %(mdp_hache)s, %(statut)s);                  ",
                        {
                            "adresse_mail": adresse_mail,
                            "nom": nom,
                            "prenom": prenom,
                            "mdp_hache": mot_de_passe,
                            "statut": statut,
                        },
                    )
                    res = cursor.rowcount()
            if res:
                created = True

            return created

    def voir_historique(self):
        return HistoriqueDAO().voir_historique()

    def exporter_historique(self):
        return HistoriqueDao().exporter_historique()


""" 
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

    mon_utilisateur.mdp = UtilisateurDao().hash_password(mon_utilisateur.mdp)
    succes = UtilisateurDao().add_utilisateur(mon_utilisateur)
    print("Utilisateur created in database : " + str(succes))
 """
