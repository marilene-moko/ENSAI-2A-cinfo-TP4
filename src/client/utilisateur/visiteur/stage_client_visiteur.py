import os
import requests

from typing import List, Optional
from bs4 import BeautifulSoup
from business_object.stage.stage_factory import stageFactory
from business_object.stage.stage_layout import Stagelayout


class Stageclientvisiteur:
    def __init__(self, utility="faire des operations sur les stage"):
        self.utility = utility

    def get_stage(self, specialite: str, localisation):
        url = (
            """https://www.stage.fr/jobs/?q="""
            + specialite
            + "&l="
            + localisation
            + "&job_type[]=Stage&p=1"
            ""
        )

        response = requests.get(url)
        stage = None

        # On verifie si le lien vers la page fonctionne bien
        if response.status_code == 200:
            print("Bonjour")
            html = response.text
            soup = BeautifulSoup(html, "lxml")

            # On  veut recuperer les informations sur les stages

            # la date de publicaton
            date_pubstage = [
                str((elt).text)
                for elt in soup.find_all("div")
                if elt.get("class") == ["listing-item__date"]
            ]

            # noms des structures et localisation
            employeurs = []
            localisation_stage = []

            divs = soup.find_all("div", attrs={"class": "listing-item__info clearfix"})

            for c in divs:
                employeurs.append(
                    str(
                        c.find_next(
                            "span",
                            class_="listing-item__info--item listing-item__info--item-company",
                        ).text
                    )
                )

                localisation_stage.append(
                    str(
                        c.find_next(
                            "span",
                            class_="listing-item__info--item listing-item__info--item-location",
                        ).text
                    )
                )

            # intitulés des stages et leurs liens
            titre_stages = []
            liens_stages = []

            intitul_liens = soup.find_all(
                "div", attrs={"class": "media-heading listing-item__title"}
            )

            for c in intitul_liens:
                titre_stages.append(str(c.find_next("a").text))
                liens_stages.append(str((c.find_next("a"))["href"]))

            # description des stages
            description_stages = []
            descrip = soup.find_all("div", attrs={"class": "listing-item__desc"})

            for elt in descrip:
                description_stages.append(str((elt).text))

            # On affiche le nombre de resultats de la recherche
            resultat_recherche = str(
                soup.find(
                    "h1",
                    attrs={
                        "class": "search-results__title col-sm-offset-3 col-xs-offset-0"
                    },
                ).text
            )
            print(resultat_recherche)

            stages = []
            for i in range(0, len(liens_stages)):
                stages.append(
                    stageFactory.instantiate_stage(
                        titre=titre_stages[i],
                        description=description_stages[i],
                        specialite=specialite,
                        localisation=localisation_stage[i],
                        siteSource="stage.fr",
                        URL_stage=liens_stages[i],
                        employeur=employeurs[i],
                        date_publication=date_pubstage[i],
                    )
                )
            i = 0
            for stage in stages:
                i += 1
                print(
                    "******************* Informations relatives au stage "
                    + str(i)
                    + " *************************"
                )
                print("Titre  :")
                print(stage.titre)
                print("\n")
                print("Specialite : " + stage.specialite)
                print("\n")
                print("localisation :  " + stage.localisation)
                print("\n")
                print("site source :  " + stage.siteSource)
                print("\n")
                print("Lien vers le stage :")
                print(stage.URL_stage)
                print("\n")
                print("employeur :  " + stage.employeur)
                print("\n")
                print("date de publication : " + stage.date_publication)
                print("\n")
                print("Description : ")
                print(stage.description)
                print("\n\n")


if __name__ == "__main__":
    stagevisiteur = Stageclientvisiteur()
    stagevisiteur.get_stage("Architecture", "paris")
