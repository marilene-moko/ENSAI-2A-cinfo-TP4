from professeur import Professeur

class Administrateur(Professeur):
    def __init__(self):
        super().__init__()

    def admin_action(self):
        if self.authenticated:
            # Actions administratives sécurisées de l'application
            # ...

    # Autres méthodes de la classe Administrateur
