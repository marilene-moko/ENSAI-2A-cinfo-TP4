from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.historique_dao import HistoriqueDAO


import hashlib


class VisiteurDao(metaclass=Singleton):
    @staticmethod
    def hash_mdp(mdp):
        """
        Méthode qui permet de hasher un mot de passe.

        Paramètres :
            mdp : str : mot de passe à hasher

        Retour :
            str : le mot de passe hasher
        """

        # Créez un objet de hachage SHA-256
        hasher = hashlib.sha256()

        # Mettez le mot de passe dans l'objet de hachage
        hasher.update(mdp.encode("utf-8"))

        # Récupérez la valeur de hachage (représentation hexadécimale)
        hashed_mdp = hasher.hexdigest()

        return hashed_mdp

    @staticmethod
    def inscription(adresse_mail, nom, prenom, mot_de_passe, statut="eleve") -> bool:
        """
        Méthode qui permet de hasher un mot de passe.

        Paramètres :
            adresse_mail : str : adresse mail du visiteur
            nom : str : nom du visiteur
            prenom : str : prénom du visiteur
            mot_de_passe : str : mot de passe que le visiteur souhaite
            statut : str : statut du visiteur (automatiquement "eleve")

        Retour :
            un booléen qui indique si l'inscription a bien été faite
        """
        created = False

        # Get the id type
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                         "
                    'FROM "Projet_Info".Personne                      '
                    "WHERE adresse_mail = %(adresse_mail)s;           ",
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
                        "VALUES                                                                              "
                        "(%(adresse_mail)s, %(nom)s, %(prenom)s, %(mot_de_passe)s, %(statut)s);                 ",
                        {
                            "adresse_mail": adresse_mail,
                            "nom": nom,
                            "prenom": prenom,
                            "mot_de_passe": mot_de_passe,
                            "statut": statut,
                        },
                    )
                    res = cursor.rowcount
            if res:
                created = True

            return created


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
