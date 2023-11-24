import unittest

from dao.listeenvie_dao import ListeEnvieDAO


class TestListeEnvieDao(unittest.TestCase):
    def test_afficher_listeEnvie_utilisateur(self):
        # on teste si la fonction marche bien même si la liste d'envie est vide
        vide = ListeEnvieDAO.afficher_listeEnvie_utilisateur("sophie.boubet@yahoo.com")
        self.assertEqual(vide, [])
        self.assertIsInstance(vide, list)


if __name__ == "__main__":
    unittest.main()
