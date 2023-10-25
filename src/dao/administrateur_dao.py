from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.professeur_dao import ProfesseurDao

class AdministrateurDao(ProfesseurDao):
    