import requests
from bs4 import BeautifulSoup
from business_object.stage.stage_factory import stageFactory
import time


class Stageclientvisiteur_sd:
    def __init__(self, utility="faire des operations sur les stage"):
        self.utility = utility

    def get_stage_etudiant(
        self,
        specialite: str = "0",
        localisation: str = "0",
        plage_pub: str = "0",
        num_page=1,
        niveau_etude: str = "0",
    ):
        stages = None
        resultat_recherche = None
        response = requests.get("""https://www.stage.fr/""")
        url = None
        stages = []
        stages_for_plage = []

        if specialite != "0" and localisation == "0" and niveau_etude == "0":
            url = (
                """https://jobs-stages.letudiant.fr/stages-etudiants/offres/libelle_libre-"""
                + specialite.lower()
                + """.html"""
            )
            response = requests.get(url)

        if specialite == "0" and localisation != "0" and niveau_etude == "0":
            url = (
                """https://jobs-stages.letudiant.fr/stages-etudiants/offres/ville-"""
                + localisation.lower()
                + """.html"""
            )
        if specialite == "0" and localisation == "0" and niveau_etude != "0":
            url = (
                """https://jobs-stages.letudiant.fr/stages-etudiants/offres/niveaux-"""
                + niveau_etude.lower()
                + """.html"""
            )
            response = requests.get(url)

        if specialite != "0" and localisation != "0" and niveau_etude == "0":
            url = (
                """https://jobs-stages.letudiant.fr/stages-etudiants/offres/libelle_libre-"""
                + specialite.lower()
                + """/ville-"""
                + localisation.lower()
                + ".html"
            )

            response = requests.get(url)

        if specialite != "0" and localisation == "0" and niveau_etude != 0:
            url = (
                """https://jobs-stages.letudiant.fr/stages-etudiants/offres/libelle_libre-"""
                + specialite.lower()
                + """/niveaux-"""
                + niveau_etude.lower()
                + ".html"
            )

        if specialite == "0" and localisation != "0" and niveau_etude != 0:
            url = (
                """https://jobs-stages.letudiant.fr/stages-etudiants/offres/niveaux-"""
                + niveau_etude.lower()
                + """/ville-"""
                + localisation.lower()
                + ".html"
            )

        if specialite != "0" and localisation != "0" and niveau_etude != "0":
            url = (
                """ https://jobs-stages.letudiant.fr/stages-etudiants/offres/libelle_libre-"""
                + specialite.lower()
                + """/niveaux-"""
                + niveau_etude.lower()
                + """/ville-"""
                + localisation.lower()
                + ".html"
            )

        print(url)

        # On verifie si le lien vers la page fonctionne bien
        if response.status_code == 200:
            print(response.status_code)
            html = response.text
            soup = BeautifulSoup(html, "lxml")

            # On recupere les liens des differents stages présents sur la page
            links_stages = []
            titres_stages = []
            divs = soup.find_all("div", attrs={"class": "tw-w-full tw-mb-2 sm:tw-mb-4"})

            for c in divs:
                titres_stages.append(str(c.find_next("a").get("title")))
                links_stages.append(str(((c.find_next("a"))["href"])))
            # print(titres_stages[0])
            # print(links_stages[0])
            # print(titres_stages[18])
            # print(links_stages[18])
            # print(len(titres_stages))
            # print(len(links_stages))


if __name__ == "__main__":
    stagevisiteur = Stageclientvisiteur_sd()
    stages = stagevisiteur.get_stage_etudiant(specialite="data", localisation="Paris")
