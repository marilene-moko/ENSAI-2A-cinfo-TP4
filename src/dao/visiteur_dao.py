from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection

class VisteurDao(metaclass=Singleton):
    def add_utilisateur(self, utilisateur) -> bool:
        """
        Add an utilisateur to the database
        """
        created = False

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
            attack.id = res["email"]
            created = True

        return created
