import lancerRecherche from src.business_object.recherche
import __str__ from src.business_object.stage

class Alerte:
    def __init__(self, ID_alerte, criteres, dateCreation, lastCheck):
        self._ID_alerte = ID_alerte
        self._criteres = criteres
        self._dateCreation = dateCreation
        self._lastCheck = lastCheck #liste de id de stages

    def verifierNouveauxStages(self):
        """
        Méthode permettant de vérifier s'il y a des nouveaux stages qui correspond à l'alerte.

        retourne : une liste de (nouveaux) stages (éventuellement vide)
        """
        nouveaux_stages = []
        
        for s in lancerRecherche(self.criteres) : #on parcoure tous les résultats de la recherche
            if not s in self.lastCheck : #on vérifie que nous avions pas déjà ce stage dans la dernière liste de stages cherchés par cette alerte
                nouveaux_stages.append(s)
        
        self._lastCheck = nouveaux_stages #on met à jour lastCheck
        
        return nouveaux_stages

    def alerteNouveauxStages(self):
        """
        Méthode qui renvoie des alertes pour les nouveaux stages

        retourne : un message d'alerte : str
        """
        nvx_stages = verifierNouveauxStages(self)

        if not nvx_stages == [] :
            nbr_stage = len(nvx_stages)
            
            if nbr_stage == 1 :
                return "Il y a un nouveau stage qui pourrait vous intéresser : {}".format(nvx_stages)
            return "Il y a {} nouveaux stages qui pourraient vous intéresser : {}".format(nbr_stage, nvx_stages)




