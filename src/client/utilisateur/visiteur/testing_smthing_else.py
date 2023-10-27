import os
import requests

from typing import List, Optional
from bs4 import BeautifulSoup
from business_object.stage.stage_factory import stageFactory
from business_object.stage.stage_layout import Stagelayout


class Stageclientvisiteur:
    def __init__(self, utility="faire des operations sur les stage"):
        self.utility = utility

    def get_stage(self, specialite: str, localisation: str, num_page=1):
        url = (
            """https://www.stage.fr/jobs/?q="""
            + specialite
            + "&l="
            + localisation
            + "&job_type[]=Stage&p="
            + str(num_page)
        )

        response = requests.get(url)
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
                a = c.find_next(
                    "span",
                    class_="listing-item__info--item listing-item__info--item-company",
                )
                if a is not None:
                    employeurs.append(str((a).text))
                else:
                    employeurs.append("Nom de l'employeur non spécifié")

                b = c.find_next(
                    "span",
                    class_="listing-item__info--item listing-item__info--item-location",
                )
                if b is not None:
                    localisation_stage.append(str((b).text))
                else:
                    localisation_stage.append("localisation non specifiée")

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

            resultat_recherche = soup.find(
                "h1",
                attrs={
                    "class": "search-results__title col-sm-offset-3 col-xs-offset-0"
                },
            )
            if resultat_recherche is not None:
                print(str(resultat_recherche).text)

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


def afficher_stage(stages, compteur=1):
    if stages is not None:
        i = 0
        localisation = stages[0].localisation
        specialite = stages[0].specialite

        while i < 21:
            print(
                "******************* Informations relatives au stage "
                + str(i + 1)
                + " *************************"
            )
            print("Titre  :")
            print(stages[i].titre)
            print("\n")
            print("Specialite : " + stages[i].specialite)
            print("\n")
            print("localisation :  " + stages[i].localisation)
            print("\n")
            print("site source :  " + stages[i].siteSource)
            print("\n")
            print("Lien vers le stage :")
            print(stages[i].URL_stage)
            print("\n")
            print("employeur :  " + stages[i].employeur)
            print("\n")
            print("date de publication : " + stages[i].date_publication)
            print("\n")
            print("Description : ")
            print(stages[i].description)
            print("\n\n")

            print("Choisissez l'action que vous souhaitez à présent executer:")
            print("1-  Voir davantage d'offres de stages:")
            print("2-  Ajouter ce stage à votre liste de voeux:")
            print("3-  Retourner à la page précédente:")
            print("4-  Retourner à la page d'accueil")

            rep = input("Faites votre choix: ")

            if rep == "1":
                i = i + 1
            if rep == "3":
                if i >= 1:
                    i = i - 1
                if i == 0:
                    print("on retourne à la page d'accueil so suzanne à toi de jouer")
                    break
            if rep == "2":
                # importer le voeu via le DAO
                print("clémént à toi de jouer")
            if i == 4:
                print("on retourne à la page d'accueil so, suzanne à toi de jouer")
                break
            compteur = compteur + 1
            stagevisiteur = Stageclientvisiteur()
            stagevisiteur.get_stage_spe_loc(
                localisation=localisation, specialite=specialite, num_page=compteur
            )
            afficher_stage(stages=stages, compteur=compteur)


if __name__ == "__main__":
    stagevisiteur = Stageclientvisiteur()
    stages_info = stagevisiteur.get_stage(
        specialite="architecture", localisation="Paris"
    )
    #  afficher_stage(stages=stages_info)
