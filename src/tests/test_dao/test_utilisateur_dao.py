import unittest

from client.utilisateur.utilisateur.utilisateur_factory import UtilisateurFactory
from dao.utilisateur_dao import UtilisateurDao
from dao.db_connection import DBConnection


class TestUtilisateurDao(unittest.TestCase):
    def test_utilisateur_exists(self):
        utilisateur_not_exists = UtilisateurDao.utilisateur_exists(
            "test@example.com", "password"
        )

        utilisateur_exists = UtilisateurDao.utilisateur_exists(
            "zuzana.gewoncik@gmail.com", "Gege75"
        )

        # on regarde si l'utilisateur n'existe pas comme prévu
        self.assertIsNone(utilisateur_not_exists)
        # on regarde si l'utilisateur existe bien
        self.assertIsNotNone(utilisateur_exists)

    ####A faire quand la fonction sera finie###
    """
    def test_afficher_profil(self):
        resultat_attendu = "Voici les informations de votre profil : '"
    """

    def test_modifier_nom(self):
        resultat_vrai = UtilisateurDao.modifier_nom("sophie.boubet@yahoo.com", "Boubet")
        resultat_attendu_vrai = True
        resultat_faux = UtilisateurDao.modifier_nom(None, "blabla")

        # on regarde si la modification a été faite
        self.assertTrue(resultat_vrai)

        # on regarde s'il est bien impossible de changer le nom sans email
        self.assertFalse(resultat_faux)

        # on recharge le nom pour pouvoir refaire le test plus tard
        modif = False
        mail = "sophie.boubet@yahoo.com"
        nombre = "s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    nom = %(nom)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": mail, "nom": nombre},
                )
                if cursor.rowcount:
                    modif = True
        self.assertTrue(modif)

    def test_modifier_prenom(self):
        resultat_vrai = UtilisateurDao.modifier_prenom(
            "sophie.boubet@yahoo.com", "Sophie"
        )
        resultat_faux = UtilisateurDao.modifier_prenom(None, "blabla")

        # on regarde si la modification a été faite
        self.assertTrue(resultat_vrai)

        # on regarde s'il est bien impossible de changer le prénom sans email
        self.assertFalse(resultat_faux)

        # on recharge le énom pour pouvoir refaire le test plus tard
        modif = False
        mail = "sophie.boubet@yahoo.com"
        nombre = "s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    prenom = %(prenom)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": mail, "prenom": nombre},
                )
                if cursor.rowcount:
                    modif = True
        self.assertTrue(modif)

    def test_modifier_mdp(self):
        resultat_vrai = UtilisateurDao.modifier_mdp(
            "sophie.boubet@yahoo.com", "testTEST25!"
        )
        resultat_faux = UtilisateurDao.modifier_mdp(None, "blabla")

        # on regarde si la modification a été faite
        self.assertTrue(resultat_vrai)

        # on regarde s'il est bien impossible de changer le mdp sans email
        self.assertFalse(resultat_faux)

        # on recharge le mot de passe pour pouvoir refaire le test plus tard
        modif = False
        mail = "sophie.boubet@yahoo.com"
        mdp = "Testtest356!"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    mot_de_passe = %(mdp)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": mail, "mdp": mdp},
                )
                if cursor.rowcount:
                    modif = True
        self.assertTrue(modif)

    def test_supprimer_profil(self):
        resultat_vrai = UtilisateurDao.supprimer_profil("sophie.boubet@yahoo.com")
        resultat_faux = UtilisateurDao.supprimer_profil(None)

        # on regarde si la suppression a été faite
        self.assertTrue(resultat_vrai)

        # on regarde s'il est bien impossible de supprimer sans email
        self.assertFalse(resultat_faux)

        # on réinscrie pour pouvoir refaire le test plus tard
        modif = False
        mail = "sophie.boubet@yahoo.com"
        nombre = "s"
        mdp = "TEST35!"
        stat = "eleve"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO "Projet_Info".Personne (adresse_mail, nom, prenom, mot_de_passe, statut)'
                    "VALUES                                                                              "
                    "(%(adresse_mail)s, %(nom)s, %(prenom)s, %(mot_de_passe)s, %(statut)s);                 ",
                    {
                        "adresse_mail": mail,
                        "nom": nombre,
                        "prenom": nombre,
                        "mot_de_passe": mdp,
                        "statut": stat,
                    },
                )
                if cursor.rowcount:
                    modif = True

        self.assertTrue(modif)


if __name__ == "__main__":
    unittest.main()
