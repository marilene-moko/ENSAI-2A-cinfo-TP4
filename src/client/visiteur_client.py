from dao.visiteur_dao import VisiteurDao


class VisiteurClient:
    def __init__(self):
        self.authenticated = False
        self.search_history = []

    @staticmethod
    def hash_mdp(mot_de_passe):
        """
        Méthode qui permet de hasher un mot de passe.

        Paramètres :
            mot_de_passe : str : mot de passe à hasher

        Retour :
            str : le mot de passe hasher
        """
        return VisiteurDao.hash_mdp(mot_de_passe)

    @staticmethod
    def inscription(adresse_mail, nom, prenom, mot_de_passe, statut):
        """
        Méthode qui permet de hasher un mot de passe.

        Paramètres :
            adresse_mail : str : adresse mail du visiteur
            nom : str : nom du visiteur
            prenom : str : prénom du visiteur
            mot_de_passe : str : mot de passe que le visiteur souhaite
            statut : str : statut du visiteur (automatiquement "eleve")

        Retour :
            un booléen qui indique si l'inscription a bien été faite
        """
        return VisiteurDao.inscription(adresse_mail, nom, prenom, mot_de_passe, statut)
