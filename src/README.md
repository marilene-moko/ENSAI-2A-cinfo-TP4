La classe commentée :

Quasiment toutes les classes business objects, clients, DAO sont commentées.
Cependant, pour la correction, s'il fallait se pencher particulièrement sur une, il faudrait prendre src/dao/utilisateur_dao.py 


La classe testée :

De même toutes les classes DAO sont testées par des tests unitaires.
Cependant, pour la correction, s'il fallait se pencher particulièrement sur une, il faudrait prendre src/dao/utilisateur_dao.py et src/tests/test_dao/test_utilisateur_dao.py


Pourquoi ce choix ? :

La classe utilisateur est la classe "fondatrice" (classe mère) de toutes les classes utilisateurs connectés, donc il nous paressait intéressant de tester cette classe en particulier.
En effet, si un dysfonctionnement est présent dans une des méthodes de UtilisateurDAO alors cela se répercutera dans les autres classes qui hérite de UtilisateurDAO.
