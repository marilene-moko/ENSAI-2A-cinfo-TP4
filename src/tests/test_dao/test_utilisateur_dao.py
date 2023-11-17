import unittest

from client.utilisateur.utilisateur.utilisateur_factory import UtilisateurFactory
from dao.utilisateur_dao import UtilisateurDao


class TestUtilisateurDao(unittest.TestCase):
    def test_utilisateur_exists(self):
        utilisateur_not_exists = UtilisateurDao.utilisateur_exists(
            "test@example.com", "password"
        )

        utilisateur_exists = UtilisateurDao.utilisateur_exists(
            "zuzana.gewoncik@gmail.com", "Gege75"
        )

        self.assertIsNone(utilisateur_not_exists)
        self.assertIsNotNone(utilisateur_exists)

    ####A faire quand la fonction sera finie###
    """
    def test_afficher_profil(self):
        resultat_attendu = "Voici les informations de votre profil : '"
    """

    def test_modifier_nom(self):
        resultat_vrai = UtilisateurDao.modifier_nom("sophie.boubet@gmail.com", "Bou")
        resultat_attendu_vrai = True
        resultat_faux = UtilisateurDao.modifier_nom(None, "blabla")

        self.assertEqual(resultat_vrai, resultat_attendu_vrai)
        self.assertFalse(resultat_faux)

    def test_modifier_prenom(self):
        resultat_vrai = UtilisateurDao.modifier_prenom("sophie.boubet@gmail.com", "Bou")
        resultat_attendu_vrai = True
        resultat_faux = UtilisateurDao.modifier_prenom(None, "blabla")

        self.assertEqual(resultat_vrai, resultat_attendu_vrai)
        self.assertFalse(resultat_faux)

    def test_modifier_mdp(self):
        resultat_vrai = UtilisateurDao.modifier_mdp("sophie.boubet@gmail.com", "Bou")
        resultat_attendu_vrai = True
        resultat_faux = UtilisateurDao.modifier_mdp(None, "blabla")

        self.assertEqual(resultat_vrai, resultat_attendu_vrai)
        self.assertFalse(resultat_faux)

    def test_supprimer_profil(self):
        resultat_vrai = UtilisateurDao.supprimer_profil("sophie.boubet@gmail.com")
        resultat_attendu_vrai = True
        resultat_faux = UtilisateurDao.supprimer_profil(None)

        self.assertEqual(resultat_vrai, resultat_attendu_vrai)
        self.assertFalse(resultat_faux)


if __name__ == "__main__":
    unittest.main()
