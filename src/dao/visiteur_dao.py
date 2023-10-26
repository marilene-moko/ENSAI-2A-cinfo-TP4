from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.historique_dao import HistoriqueDao

import hashlib

class VisiteurDao(metaclass=Singleton):
    def inscription(self, utilisateur) -> bool:
        """
        Add an utilisateur to the database
        """
        created = False

        #hacher le mot de passe 
        mdp_hache = self.hash_password(utilisateur.mdp)

        # Get the id type
        email = TypeAttackDAO().find_id_by_label(attack.type)
        if email in #email dans Personne:
            raise ValueError(
                "L'email choisi existe déjà. Veuillez en choisir un autre s'il-vous-plaît."
            )

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Personne (email, nom, prenom, mdp)             "
                    "VALUES                                                     "
                    "(%(email)s, %(nom)s, %(prenom)s, %(mdp)s)                  "
                    "RETURNING email;",
                    {
                        "email": email,
                        "nom": nom,
                        "prenom": prenom,
                        "mdp": mdp,
                        "statut": statut #=eleve par defaut 
                    },
                )
                res = cursor.fetchone()
        if res:
            email = res["email"]
            created = True

        return created

    def voir_historique(self):
        return HistoriqueDao().voir_historique()

    def exporter_historique(self):
        return HistoriqueDao().exporter_historique()

    def hash_password(self, password):
        # Créez un objet de hachage SHA-256
        hasher = hashlib.sha256()
        
        # Mettez le mot de passe dans l'objet de hachage
        hasher.update(password.encode('utf-8'))
        
        # Récupérez la valeur de hachage (représentation hexadécimale)
        hashed_password = hasher.hexdigest()
        
        return hashed_password


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

