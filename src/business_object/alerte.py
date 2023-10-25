import lancerRecherche from src.business_object.recherche

class Alerte:
    def __init__(self, ID_alerte, criteres, dateCreation, lastCheck):
        self._ID_alerte = ID_alerte
        self._criteres = criteres
        self._dateCreation = dateCreation
        self._lastCheck = lastCheck #liste de stage

    def verifierNouveauxStages(self, criteres, lastCheck):
        """
        Méthode permettant de vérifier s'il y a des nouveaux stages qui correspond à l'alerte.

        retourne : une liste de (nouveaux) stages (éventuellement vide)
        """
        nouveaux_stages = []
        
        for s in lancerRecherche(criteres) : #on parcoure tous les résultats de la recherche
            if not s in lastCheck : #on vérifie que nous avions pas déjà ce stage dans la dernière liste de stages cherchés par cette alerte
                nouveaux_stages.append(s)
        
        return nouveaux_stages

