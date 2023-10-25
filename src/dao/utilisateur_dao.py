from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.type_attack_dao import TypeAttackDAO

from business_object.attack.abstract_attack import AbstractAttack
from business_object.attack.attack_factory import AttackFactory
from client.utilisateur import Utilisateur


class UtilisateurDao(metaclass=Singleton):
    def utilisateur_exists(self, email: str, mdp: str) -> Optional[AbstractAttack]:
        """
        Regarder si l'utilisateur existe bien
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                       "
                    "  FROM Personne                                "
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

    def update_utilisateur(self, utilisateur) -> bool:
        updated = False

        # Get the email
        email = #TypeAttackDAO().find_email_by_label(attack.type)
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
                        "nom": nom,
                        "prenom": prenom,
                        "mdp": mdp,
                        "statut": statut #=eleve par defaut 
                    },
                )
                if cursor.rowcount:
                    updated = True
        return updated




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
