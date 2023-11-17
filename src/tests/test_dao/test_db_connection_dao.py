import os
from unittest.mock import patch, Mock
import pytest
from dao.db_connection import DBConnection


@pytest.fixture
def mock_psycopg2_connect(mocker):
    return mocker.patch("psycopg2.connect")


@pytest.fixture
def mock_os_environ(mocker):
    return mocker.patch.dict(
        os.environ,
        {
            "HOST": "sgbd-eleves.domensai.ecole",
            "PORT": "5432",
            "DATABASE": "id2241",
            "USER": "id2241",
            "PASSWORD": "id2241",
        },
    )


def test_connection_opened_with_correct_parameters(
    mock_os_environ, mock_psycopg2_connect
):
    # Arrange
    db_connection = DBConnection()

    # Act
    connection = db_connection.connection

    # Assert
    expected_kwargs = {
        "host": "votre_hote",
        "port": "votre_port",
        "database": "votre_base_de_donnees",
        "user": "votre_utilisateur",
        "password": "votre_mot_de_passe",
        "cursor_factory": RealDictCursor,
    }
    mock_psycopg2_connect.assert_called_once_with(**expected_kwargs)
    assert connection == mock_psycopg2_connect.return_value


def test_connection_open_failed(mock_os_environ, mock_psycopg2_connect):
    # Arrange
    mock_psycopg2_connect.side_effect = Exception("Erreur de connexion")
    db_connection = DBConnection()

    # Act & Assert
    with pytest.raises(Exception, match="Erreur de connexion"):
        _ = db_connection.connection


# Exécuter les tests avec pytest
# pytest -v nom_du_fichier_test.py
