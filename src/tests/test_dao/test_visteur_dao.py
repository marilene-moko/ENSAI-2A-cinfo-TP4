import unittest

from client.utilisateur.utilisateur.utilisateur_factory import UtilisateurFactory
from dao.visiteur_dao import VisiteurDao
from dao.db_connection import DBConnection


class TestUtilisateurDao(unittest.TestCase):
    def test_hash_mdp(self):
        hashed_mdp = VisiteurDao.hash_mdp("MotdePASSE!")

        # on regarde si le hashage a été effectué
        self.assertIsNotNone(hashed_mdp)

        # on regarde si la sortie est bien un str
        self.assertIsInstance(hashed_mdp, str)

    def test_inscription(self):
        created = VisiteurDao.inscription(
            "test_inscription@email.eu", "Test", "User", "Ginette77!", "eleve"
        )
        created_false = VisiteurDao.inscription(
            "test_inscription@email.eu", "Test_false", "User_false", "False77!", "eleve"
        )

        # on regarde si l'inscription a bien été effectuée
        self.assertTrue(created)
        # on regarde si l'incription n'a pas été effectuée comme prévu
        self.assertFalse(created_false)

        # on enlève l'inscription que l'on vient d'effectuer pour pouvoir refaire le test plus tard
        supp = False
        mail = "test_inscription@email.eu"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'DELETE FROM "Projet_Info".Personne WHERE adresse_mail = %(email)s;',
                    {"email": mail},
                )
                if cursor.rowcount:
                    supp = True
        self.assertTrue(supp)


if __name__ == "__main__":
    unittest.main()
