import unittest

from client.utilisateur.utilisateur.utilisateur_factory import UtilisateurFactory
from dao.administrateur_dao import AdministrateurDao
from dao.db_connection import DBConnection


class TestAdministrateurDao(unittest.TestCase):
    def test_modifierDroitsUtilisateur(self):
        sansmail = AdministrateurDao.modifierDroitsUtilisateur(None, "eleve")
        test_vrai = AdministrateurDao.modifierDroitsUtilisateur("t", "eleve")

        # on regarde s'il est bien impossible de modifier sans mail de l'utilisateur
        self.assertFalse(sansmail)

        # on regarde si la modification a bien été faite
        self.assertTrue(test_vrai)


if __name__ == "__main__":
    unittest.main()
