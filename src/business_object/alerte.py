from abc import ABC, abstractmethod

class Alerte(ABC):
    def __init__(
        self,
        ID_alerte,
        criteres,
        dateCreation,
        lastCheck
    ):
        self._ID_alerte = ID_alerte
        self._criteres = criteres
        self._dateCreation = dateCreation
        self._lastCheck = lastCheck

        @abstractmethod
        def methodeCheckNouveauxStages()
