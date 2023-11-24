import unittest
from unittest.mock import MagicMock
from dao.historique_dao import HistoriqueDAO


class TestHistoriqueDAO(unittest.TestCase):
    def test_afficher_historique_utilisateur(self):
        # Create a mock DBConnection to replace the real one
        mock_db_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.connection.__enter__.return_value.cursor.return_value = (
            mock_cursor
        )

        # Set up the input parameters for the method
        adresse_mail = "test@example.com"

        # Set up the expected SQL query and result
        expected_query = (
            'SELECT * FROM "Projet_Info".page_visitee '
            "WHERE adresse_mail = %(adresse_mail)s;"
        )
        expected_params = {"adresse_mail": adresse_mail}
        expected_result = [("result1", "result2"), ("result3", "result4")]

        # Mockez la méthode fetchall pour renvoyer le résultat attendu
        mock_cursor.fetchall.return_value = expected_result

        # Mockez la classe DBConnection pour renvoyer la connexion fictive
        with unittest.mock.patch(
            "dao.historique_dao.DBConnection", return_value=mock_db_connection
        ):
            # Appelez la méthode à tester
            result = HistoriqueDAO.afficher_historique_utilisateur(adresse_mail)

        # Instructions de débogage
        print("Appels à execute sur le mock :", mock_cursor.execute.call_args_list)
        print("Nombre d'appels à execute sur le mock :", mock_cursor.execute.call_count)

        # Vérifiez que la requête SQL a été exécutée avec les bons paramètres
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

        # Vérifiez que la méthode a renvoyé le résultat attendu
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
