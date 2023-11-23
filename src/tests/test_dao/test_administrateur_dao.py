"""
import unittest
from unittest.mock import patch, MagicMock
from dao.administrateur_dao import AdministrateurDao
from dao.db_connection import DBConnection


class TestAdministrateurDao(unittest.TestCase):
    def setUp(self):
        # Créer un mock_cursor une seule fois pour être utilisé dans tous les tests
        self.mock_cursor = MagicMock()

    @patch.object(DBConnection, "connection")
    def test_modifierDroitsUtilisateur_utilisateur_existe(self, mock_connection):
        # Configurer le mock_connection pour retourner un MagicMock pour cursor
        mock_cursor = MagicMock()
        mock_connection.__enter__.return_value.cursor.return_value = mock_cursor

        # Configurer le comportement du mock_cursor pour simuler une ligne affectée dans la base de données
        mock_cursor.execute.return_value.rowcount = 1

        # Exécuter la méthode que vous testez
        result = AdministrateurDao.modifierDroitsUtilisateur(
            "test@example.com", "professeur"
        )

        # Vérification que la requête SQL correcte a été exécutée et que le résultat est celui attendu
        mock_cursor.execute.assert_called_with(
            'UPDATE "Projet_Info".Personne SET statut = %s WHERE email = %s;',
            ("professeur", "test@example.com"),
        )
        self.assertEqual(result, "Le statut de cet utilisateur a bien été mis à jour.")

    @patch.object(DBConnection, "connection")
    def test_modifierDroitsUtilisateur_utilisateur_nexiste_pas(self, mock_connection):
        # Configurer le mock_connection pour retourner un MagicMock pour cursor
        mock_cursor = MagicMock()
        mock_connection.__enter__.return_value.cursor.return_value = mock_cursor

        # Configurer le comportement du mock_cursor pour simuler aucune ligne affectée dans la base de données
        mock_cursor.execute.return_value.rowcount = 0

        # Exécuter la méthode que vous testez
        result = AdministrateurDao.modifierDroitsUtilisateur(
            "utilisateur_inexistant@example.com", "administrateur"
        )

        # Vérification que la requête SELECT a été exécutée et que le résultat est celui attendu
        mock_cursor.execute.assert_not_called()
        self.assertEqual(result, "Cet utilisateur n'existe pas.")


if __name__ == "__main__":
    unittest.main()
"""
