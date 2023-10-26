from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.professeur_dao import ProfesseurDao


class AdministrateurDao(ProfesseurDao):
    def modifierDroitsUtilisateur(self, email_utilisateur, nv_statut):
        """
        Modifier les droits d'un utilisateur : utilisateur ou professeur ou administrateur
        """

        # Vérifier que l'utilisateur avec cet email existe
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * " 'FROM "Projet_Info".Personne ' "WHERE email = %s;",
                    (email_utilisateur,),
                )
                res = cursor.fetchone()

        # Si l'utilisateur existe bien on modifie son statut
        if res:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        'UPDATE "Projet_Info".Personne '
                        "SET statut = %s "
                        "WHERE email = %s;",
                        (nv_statut, email_utilisateur),
                    )

                    if cursor.rowcount > 0:
                        return "Le statut de cet utilisateur a bien été mis à jour."
                    else:
                        return "Un problème est survenu et le statut n'a pas pu être mis à jour."
        return "Cet utilisateur n'existe pas."
