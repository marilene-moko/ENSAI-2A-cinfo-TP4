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

        try:
            # Get the id type
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                                         "
                        'FROM "Projet_Info".Personne                      '
                        "WHERE adresse_mail = %(adresse_mail)s;           ",
                        {"adresse_mail": adresse_mail},
                    )
                    utilisateur_existe = cursor.fetchone()
            if utilisateur_existe:
                return created

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
                    lignes_modif = cursor.rowcount

            if lignes_modif:
                created = True

        except Exception as e:
            # Gérer les exceptions (par exemple, les erreurs de base de données)
            print(f"Erreur lors de l'inscription de l'utilisateur : {e}")

        return created
