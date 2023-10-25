from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.utilisateur_dao import UtilisateurDao

class ProfesseurDao(UtilisateurDao):
    