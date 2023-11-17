"""
import unittest
from datetime import datetime
from business_object.recherche import lancerRecherche
from business_object.stage import Stage


class TestAlerte(unittest.TestCase):
    def setUp(self):
        # Initialisation des données pour les tests
        self.date_creation = datetime.now()
        self.last_check = [1, 2, 3]  # Exemple de liste de stages déjà vérifiés
        self.alerte = Alerte(
            1, {"critere1": "valeur1"}, self.date_creation, self.last_check
        )

    def test_verifierNouveauxStages(self):
        # Simulation de résultats de recherche
        def mock_lancerRecherche(criteres):
            # Retourne une liste de stages fictifs pour les tests
            return [
                Stage(4, {"critere1": "valeur2"}),
                Stage(5, {"critere1": "valeur3"}),
            ]

        # Remplacement de la fonction lancerRecherche par notre mock
        original_lancerRecherche = lancerRecherche
        lancerRecherche = mock_lancerRecherche

        try:
            nouveaux_stages = self.alerte.verifierNouveauxStages()
            self.assertEqual(
                nouveaux_stages,
                [Stage(4, {"critere1": "valeur2"}), Stage(5, {"critere1": "valeur3"})],
            )
            self.assertEqual(
                self.alerte.lastCheck, [4, 5]
            )  # Vérifie que lastCheck est mis à jour
        finally:
            # Restauration de la fonction lancerRecherche originale
            lancerRecherche = original_lancerRecherche

    def test_alerteNouveauxStages(self):
        # Simulation de nouveaux stages
        self.alerte.verifierNouveauxStages()

        # Test du message d'alerte
        alerte_message = self.alerte.alerteNouveauxStages()
        self.assertEqual(
            alerte_message,
            "Il y a 2 nouveaux stages qui pourraient vous intéresser : [Stage ID: 4, Stage ID: 5]",
        )


if __name__ == "__main__":
    unittest.main()
"""
