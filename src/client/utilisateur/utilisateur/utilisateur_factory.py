from client.utilisateur.utilisateur.utilisateur_layout import Utilisateurlayout
from utils.singleton import Singleton


class UtilisateurFactory(metaclass=Singleton):
    def instantiate_utilisateur(
        email: str = None,
        nom: str = None,
        prenom: str = None,
        mdp: str = None,
        statut: str = None,
    ) -> Utilisateurlayout:
        utilisateur = None

        if email is not None:
            utilisateur = Utilisateurlayout(
                adresse_mail=email,
                nom=nom,
                prenom=prenom,
                mot_de_passe=mdp,
                statut=statut,
            )

        return utilisateur
