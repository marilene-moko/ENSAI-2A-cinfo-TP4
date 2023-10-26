from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.historique_dao import HistoriqueDAO


import hashlib

class VisiteurDao(metaclass=Singleton):
    def inscription(
        self, adresse_mail, nom, prenom, mot_de_passe, statut="eleve"
    ) -> bool:
        """
        Add an utilisateur to the database
        """
        created = False

<<<<<<< HEAD
<<<<<<< HEAD
        #hacher le mot de passe 
        mdp_hache = self.hash_password(utilisateur.mdp)

        # Get the id type
        email = TypeAttackDAO().find_id_by_label(attack.type)
        if email in #email dans Personne:
            raise ValueError(
                "L'email choisi existe déjà. Veuillez en choisir un autre s'il-vous-plaît."
            )
=======
        email = utilisateur["email"]
>>>>>>> 34618408bd36e7d4560867c3665f1a93f4e0b4b8

=======
>>>>>>> a1c815b9f8b60b127daa41cf333ad325744efca0
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
            raise ValueError(
                "L'email choisi existe déjà. Veuillez en choisir un autre s'il-vous-plaît."
            )
        else:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'INSERT INTO "Projet_Info".Personne (adresse_mail, nom, prenom, mot_de_passe)'
                        "VALUES                                                                      "
                        "(%(adresse_mail)s, %(nom)s, %(prenom)s, %(mot_de_passe)s);                  ",
                        {
                            "adresse_mail": adresse_mail,
                            "nom": nom,
                            "prenom": prenom,
                            "mot_de_passe": mot_de_passe,
                            "statut": statut,
                        },
                    )
                    res = cursor.fetchone()
            if res:
                created = True

            return created

    def voir_historique(self):
        return HistoriqueDAO().voir_historique()

    def exporter_historique(self):
<<<<<<< HEAD
        return HistoriqueDao().exporter_historique()

    def hash_password(self, password):
        # Créez un objet de hachage SHA-256
        hasher = hashlib.sha256()
        
        # Mettez le mot de passe dans l'objet de hachage
        hasher.update(password.encode('utf-8'))
        
        # Récupérez la valeur de hachage (représentation hexadécimale)
        hashed_password = hasher.hexdigest()
        
        return hashed_password
=======
        return HistoriqueDAO().exporter_historique()
>>>>>>> a1c815b9f8b60b127daa41cf333ad325744efca0


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
