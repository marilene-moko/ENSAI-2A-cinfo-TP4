import unittest

from dao.historique_dao import HistoriqueDAO


class TestHistoriqueDao(unittest.TestCase):
    def test_afficher_historique_utilisateur(self):
        # on teste si la fonction affiche bien un historique vide
        vide = HistoriqueDAO.afficher_historique_utilisateur("sophie.boubet@yahoo.com")
        self.assertEqual(vide, [])
        self.assertIsInstance(vide, list)

        # ici pour un historique non vide
        remplie = HistoriqueDAO.afficher_historique_utilisateur("t")
        self.assertNotEqual(remplie, [])
        self.assertIsNotNone(remplie)
        self.assertIsInstance(remplie, list)

    def test_importer_historique(self):
        # on veut voir si sans mail l'importation ne se fait bien pas
        sansmail = HistoriqueDAO.importer_historique(None)
        self.assertFalse(sansmail)

        # on veut voir si l'importation marche
        test = HistoriqueDAO.importer_historique("t")
        self.assertTrue(test)

    def test_importer_historique_modifed(self):
        # on veut voir si sans mail ou sans stage l'importation ne se fait bien pas
        sansmail = HistoriqueDAO.importer_historique_modified(None, None)
        self.assertFalse(sansmail)
        sansstage = HistoriqueDAO.importer_historique_modified(
            adresse_mail="t", stage=None
        )
        self.assertFalse(sansstage)

    def test_exporter_historique(self):
        test = HistoriqueDAO.exporter_historique("t")
        self.assertTrue(test)

    def test_supprimer_historique(self):
        test = HistoriqueDAO.supprimer_historique_utilisateur("sophie.boubet@yahoo.com")
        self.assertTrue(test)

    def test_ajouter_historique(self):
        # on teste si y'a bien erreur sans mail
        sansmail = HistoriqueDAO.ajouter_historique(None, None, None)
        self.assertFalse(sansmail)  # il y aura aussi un print expliquant l'erreur

        # on teste si l'ajout marche bien quand les paramètres existent
        test_vrai = HistoriqueDAO.ajouter_historique(
            "t",
            "https://www.stage.fr/job/6548418/stage-chargé-e-de-projets-sirh-h-f-janvier-2024-6-mois/",
            "Stage - Chargé(e) de projets SIRH (H/F) - Janvier 2024 - 6 mois",
        )
        self.assertTrue(test_vrai)


if __name__ == "__main__":
    unittest.main()
