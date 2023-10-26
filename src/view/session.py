from utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        Le syntaxe
        ref:type = valeur
        permet de donner le type des variables. Utile pour l'autocompletion.
        """
        self.nom: str = "Visiteur"
        self.prenom: str = None
        self.pseudo: str = "Visiteur"
        self.email: str = None
        self.mot_de_passe: str = None
        self.statut: str = "Eleve"
