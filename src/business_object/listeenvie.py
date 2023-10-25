class ListeEnvie:
    def __init__(self, id_list, envies):
        self.id_list = id_list
        self.envies = envies  # liste des id de stages

    def ajouterEnvie(self, stage_id):
        """
        Méthode qui permet d'ajouter un stage à la liste envies

        prend en paramètre : stage_id : l'id du stage à rajouter dans la liste d'envie

        retourne : retourne rien met à mis à jour la liste envies
        """
        if not stage_id in self.envies:
            self.envies.append(stage_id)

    def retirerEnvie(self, stage_id):
        """
        Méthode qui permet de retirer un stage à la liste envies

        prend en paramètre : stage_id : l'id du stage à retirer de la liste d'envie

        retourne : retourne rien met à mis à jour la liste envies
        """
        if stage_id in self.envies:
            self.envies.remove(stage_id)
