from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.professeur_dao import ProfesseurDao


class AdministrateurDao(ProfesseurDao):
    @staticmethod
    def modifierDroitsUtilisateur(email_utilisateur, nv_statut):
        """
        Modifier les droits d'un utilisateur : utilisateur ou professeur ou administrateur

        Paramètres :
            email_utilisateur : str : l'adresse mail de l'utilisateur dont l'administrateur veut changer le statut
            nv_statut : str : le statut que l'administrateur veut attribuer à l'utilisateur
                            ce statut ne peut qu'être : 'utilisateur', 'professeur', 'administrateur'

        Retour :
            un str qui indique si la modification des droits a bien été faite
        """

        # Vérifier que l'utilisateur avec cet email existe
        modif = False

        if email_utilisateur is None:
            return modif

        # Si l'utilisateur existe bien on modifie son statut
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne '
                    "SET statut = %s "
                    "WHERE adresse_mail = %s;",
                    (nv_statut, email_utilisateur),
                )

                if cursor.rowcount:
                    return True

    @staticmethod
    def get_users():
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT nom, prenom, adresse_mail, statut FROM "Projet_Info".Personne;',
                )
                users = cursor.fetchall()  # Récupérer tous les utilisateurs
        return users
