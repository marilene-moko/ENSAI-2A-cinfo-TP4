from client.utilisateur.utilisateur.utilisateur_factory import UtilisateurFactory
from dao.db_connection import DBConnection
from dao.visiteur_dao import VisiteurDao


class UtilisateurDao(VisiteurDao):
    @staticmethod
    def utilisateur_exists(adresse_mail: str, mot_de_passe: str):
        """
        Regarder si l'utilisateur existe bien

        Paramètres :
            adresse_mail : str : l'adresse mail de l'utilisateur
            mot_de_passe : str : le mot de passe de l'utilisateur

        Retour :
            None si l'utilisateur n'existe pas et les caractéristiques de l'utilisateur s'il existe
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                       "
                    'FROM "Projet_Info".Personne                    '
                    " WHERE adresse_mail=%(adresse_mail)s   AND mot_de_passe=%(mot_de_passe)s",
                    {"adresse_mail": adresse_mail, "mot_de_passe": mot_de_passe},
                )
                res = cursor.fetchone()
        if res:
            utilisateur = UtilisateurFactory.instantiate_utilisateur(
                email=res["adresse_mail"],
                nom=res["nom"],
                prenom=res["prenom"],
                mdp=res["mot_de_passe"],
                statut=res["statut"],
            )
        else:
            utilisateur = None
        return utilisateur

    @staticmethod
    def afficher_profil(adresse_mail, pseudo, nom, prenom, mot_de_passe):
        """
        Méthode qui permet d'afficher les caractéristiques d'un profil utilisateur.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur
            pseudo : str : pseudo de l'utilisateur
            nom : str : nom de l'utilisateur
            prenom : str : prénom de l'utilisateur
            mot_de_passe : str : mot de passe de l'utilisateur

        Retour :
            un str qui indique les caractéristiques du profil utilisateur
        """
        print(f"Voici les informations de votre profil: {adresse_mail}")

    @staticmethod
    def modifier_nom(adresse_mail, modification) -> bool:
        """
        Méthode qui permet à un utilisateur de changer son nom sur son profil.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur
            modification : str : le nouveau nom

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """

        updated = False

        # Get the email
        if adresse_mail is None:
            return updated

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    nom = %(nom)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": adresse_mail, "nom": modification},
                )
                if cursor.rowcount:
                    updated = True
        return updated

    @staticmethod
    def modifier_prenom(adresse_mail, modification) -> bool:
        """
        Méthode qui permet à un utilisateur de changer son prénom sur son profil.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur
            modification : str : le nouveau prénom

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """

        updated = False

        # Get the email
        if adresse_mail is None:
            return updated

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    prenom = %(prenom)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": adresse_mail, "prenom": modification},
                )
                if cursor.rowcount:
                    updated = True
        return updated

    @staticmethod
    def modifier_mdp(adresse_mail, modification) -> bool:
        """
        Méthode qui permet à un utilisateur de changer son mot de passe.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur
            modification : str : le nouveau mot de passe

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """

        updated = False

        # Get the email
        if adresse_mail is None:
            return updated

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'UPDATE "Projet_Info".Personne                        '
                    "   SET    mot_de_passe = %(mot_de_passe)s                     "
                    " WHERE adresse_mail = %(adresse_mail)s                             ",
                    {"adresse_mail": adresse_mail, "mot_de_passe": modification},
                )
                if cursor.rowcount:
                    updated = True
        return updated

    @staticmethod
    def supprimer_profil(adresse_mail):
        """
        Méthode qui permet à un utilisateur de supprimer son historique.

        Paramètres :
            adresse_mail : str : adresse mail de l'utilisateur

        Retour :
            un booléen qui indique si la tâche a été effectuée
        """

        supp = False

        if adresse_mail is None:
            return supp

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'DELETE FROM "Projet_Info".page_visitee WHERE adresse_mail = %s;',
                    (adresse_mail),
                )
                cursor.execute(
                    'DELETE FROM "Projet_Info".voeu WHERE adresse_mail = %s;',
                    (adresse_mail),
                )
                cursor.execute(
                    'DELETE FROM "Projet_Info".Personne WHERE adresse_mail = %s;',
                    (adresse_mail),
                )
                if cursor.rowcount == 1:
                    supp = True
        return supp
