from dao.visiteur_dao import VisiteurDao

class VisiteurClient:
    def __init__(self):
        self.authenticated = False
        self.search_history = []

"""
    def authenticate(self, username, password):
        # Vérification de l'authentification sécurisée ici
        if not self.authenticated:
            if self._validate_credentials(username, password):
                self.authenticated = True
                return True
        return False

    def register(self, username, password, email):
        if not self.authenticated:
            # Inscription sécurisée ici
            if self._validate_registration_data(username, password, email):
                self._create_user_account(username, password, email)
                self.authenticated = True
                return True
        return False
"""

    def hash_mdp(mdp):
        """ 
        Méthode qui permet de hasher un mot de passe.

        Paramètres :
            mdp : str : mot de passe à hasher

        Retour :
            str : le mot de passe hasher
        """ 
        return VisiteurDao.hash_mdp(self, mdp)

    def inscription(email, nom, prenom, mdp, statut):
        """ 
        Méthode qui permet de hasher un mot de passe.

        Paramètres :
            email : str : adresse mail du visiteur
            nom : str : nom du visiteur
            prenom : str : prénom du visiteur
            mdp : str : mot de passe que le visiteur souhaite
            statut : str : statut du visiteur (automatiquement "eleve") 

        Retour :
            un booléen qui indique si l'inscription a bien été faite
        """
        return VisiteurDao.inscription(email, nom, prenom, mdp, statut)
