import requests
from bs4 import BeautifulSoup
from business_object.stage.stage_factory import stageFactory
import time


### Version du scraping à utiliser
class Stageclientvisiteur:
    def __init__(self, utility="faire des operations sur les stage"):
        self.utility = utility

    def get_stage_spe_loc(
        self,
        specialite: str = "0",
        localisation: str = " 0",
        plage_pub: str = "0",
        num_page=1,
    ):
        stages = None
        resultat_recherche = None
        response = requests.get("""https://www.stage.fr/""")
        url = None
        stages = []
        stages_for_plage = []

        if specialite != "0" and localisation != "0":
            url = (
                """https://www.stage.fr/jobs/?q="""
                + specialite
                + "&l="
                + localisation
                + "&job_type[]=Stage&p="
                + str(num_page)
            )

            response = requests.get(url)

        if specialite != "0" and localisation == "0":
            url = (
                """https://www.stage.fr/jobs/?q="""
                + specialite
                + """&job_type[]=Stage&job_type[]=Stage&p="""
                + str(num_page)
            )
            response = requests.get(url)

        if specialite == "0" and localisation != "0":
            url = (
                """https://www.stage.fr/jobs/?q=&l="""
                + localisation
                + """&job_type%5B%5D=Stage&job_type%5B%5D=Stage&p="""
                + str(num_page)
            )

            response = requests.get(url)
        print(url)

        # On verifie si le lien vers la page fonctionne bien
        while response.status_code == 200 and num_page <= 5:
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
            # if resultat_recherche is not None:
            # print(str(resultat_recherche.text))

            # On veut formater la plage de publication renseignée dans un format compatible avec celui du site scrapé
            mois_check = [
                "janvier",
                "fevrier",
                "mars",
                "avril",
                "mai",
                "juin",
                "juillet",
                "aout",
                "septembre",
                "octobre",
                "novembre",
                "decembre",
            ]

            mois_format = [
                "janv",
                "fev",
                "mars",
                "avril",
                "mai",
                "juin",
                "juillet",
                "aout",
                "sept",
                "oct",
                "nov",
                "dec",
            ]
            jour = "0"
            mois = ""
            annee = ""
            plage_pub_split = plage_pub.split(" ")

            if len(plage_pub_split) == 3:
                jour = str(plage_pub_split[0])
                for i in range(12):
                    if str(plage_pub_split[1]).lower() in mois_check[i]:
                        mois = mois_format[i]
                annee = plage_pub_split[2]
                plage_pub_format = jour + " " + mois + ".," + " " + annee
            if len(plage_pub_split) == 2:
                if plage_pub_split[0].isdigit() == True:
                    jour = plage_pub_split[0]
                    for i in range(12):
                        if str(plage_pub_split[1]).lower() in mois_check[i]:
                            mois = mois_format[i]
                    plage_pub_format = jour + " " + mois + ".,"

                else:
                    for i in range(12):
                        if str(plage_pub_split[0]).lower() in mois_check[i]:
                            mois = mois_format[i]
                    annee = plage_pub_split[1]
                    plage_pub_format = mois + ".," + " " + annee

            if len(plage_pub_split) == 1:
                annee = plage_pub_split[0]
                plage_pub_format = annee

            # for i in range(0, len(liens_stages)):
            for i in range(0, min(20, len(liens_stages) - 20 * (num_page - 1))):
                stages.append(
                    stageFactory.instantiate_stage(
                        titre=titre_stages[20 * (num_page - 1) + i - 1],
                        description=description_stages[20 * (num_page - 1) + i - 1],
                        specialite=specialite,
                        localisation=localisation_stage[20 * (num_page - 1) + i - 1],
                        siteSource="stage.fr",
                        URL_stage=liens_stages[20 * (num_page - 1) + i - 1],
                        employeur=employeurs[20 * (num_page - 1) + i - 1],
                        date_publication=date_pubstage[20 * (num_page - 1) + i - 1],
                    )
                )
                if plage_pub_format in str(date_pubstage[20 * (num_page - 1) + i - 1]):
                    stages_for_plage.append(
                        stageFactory.instantiate_stage(
                            titre=titre_stages[20 * (num_page - 1) + i - 1],
                            description=description_stages[20 * (num_page - 1) + i - 1],
                            specialite=specialite,
                            localisation=localisation_stage[
                                20 * (num_page - 1) + i - 1
                            ],
                            siteSource="stage.fr",
                            URL_stage=liens_stages[20 * (num_page - 1) + i - 1],
                            employeur=employeurs[20 * (num_page - 1) + i - 1],
                            date_publication=date_pubstage[20 * (num_page - 1) + i - 1],
                        )
                    )

            num_page = num_page + 1
            if specialite != "0" and localisation != "0":
                url = (
                    """https://www.stage.fr/jobs/?q="""
                    + specialite
                    + "&l="
                    + localisation
                    + "&job_type[]=Stage&p="
                    + str(num_page)
                )

                response = requests.get(url)

            if specialite != "0" and localisation == "0":
                url = (
                    """https://www.stage.fr/jobs/?q="""
                    + specialite
                    + """&job_type[]=Stage&job_type[]=Stage&p="""
                    + str(num_page)
                )
                response = requests.get(url)

            if specialite == "0" and localisation != "0":
                url = (
                    """https://www.stage.fr/jobs/?q=&l="""
                    + localisation
                    + """&job_type%5B%5D=Stage&job_type%5B%5D=Stage&p="""
                    + str(num_page)
                )

                response = requests.get(url)

            time.sleep(10)  # pour contourner les erreurs de type 409

        if len(stages) == 0:
            print(
                "aucun stage ne correspond aux modalités choisies sur le site stage.fr",
            )
        else:
            if plage_pub == "0":
                if specialite != 0 and localisation != 0:
                    print(
                        len(stages_for_plage),
                        " stages ont été trouvés  pour la  plage de temps renseignée correspondant à la specialité",
                        specialite,
                        "et à la localisation",
                        localisation,
                    )
                if specialite != 0 and localisation == 0:
                    print(
                        len(stages_for_plage),
                        " stages ont été trouvés  pour la  plage de temps renseignée et correspondent à la specialité",
                        specialite,
                    )
                if specialite == 0 and localisation != 0:
                    print(
                        len(stages_for_plage),
                        " stages ont été trouvés  pour la  plage de temps renseignée et correspondent à la localisation",
                        localisation,
                    )
            if plage_pub != "0":
                if specialite != 0 and localisation != 0:
                    print(
                        len(stages_for_plage),
                        " stages ont été trouvés  pour la  plage de temps",
                        plage_pub,
                        "correspondant à la specialité",
                        specialite,
                        "et à la localisation",
                        localisation,
                    )
                if specialite != 0 and localisation == 0:
                    print(
                        len(stages_for_plage),
                        " stages ont été trouvés  pour la  plage de temps",
                        plage_pub,
                        "correspondant à la specialité",
                        specialite,
                    )
                if specialite == 0 and localisation != 0:
                    print(
                        len(stages_for_plage),
                        " stages ont été trouvés  pour la  plage de temps",
                        plage_pub,
                        "et à la localisation",
                        localisation,
                    )

        return stages_for_plage

    def afficher_stage(self, stages):
        page = 1
        while page >= 0:
            if len(stages) == 0:
                print(
                    "aucun stage correspondant à votre/ vos critère(s) n'a été trouvé "
                )
            if len(stages) >= 20 * (page - 1) + 1:
                i = 0
                for i in range(0, min(len(stages) - 20 * (page - 1), 20)):
                    print(
                        "******************* Informations relatives au stage ",
                        20 * (page - 1) + i + 1,
                        " *************************",
                    )
                    print("Titre  :")
                    print(stages[1])
                    print("\n")
                    print("Specialite : ")
                    print(stages[3])
                    print("\n")
                    print("localisation :  ")
                    print(stages[4])
                    print("\n")
                    print("site source :  ")
                    print(stages[5])
                    print("\n")
                    print("Lien vers le stage :")
                    print(stages[6])
                    print("\n")
                    print("employeur :  ")
                    print(stages[7])
                    print("\n")
                    print("date de publication :")
                    print(stages[8])
                    print("\n")
                    print("Description : ")
                    print(stages[2])
                    print("\n\n")

                if min(len(stages), 20) < 20:
                    page = -1
                if min(len(stages), 20) == 20:
                    rep = "0"
                    while rep.upper() != "N" and rep.upper() != "Y":
                        rep = input("Voulez vous voir davantage de stages? : Y/N ")
                        if rep.upper() == "N":
                            page = -1

                        if rep.upper() == "Y":
                            page = page + 1

                        if rep.upper() != "N" and rep.upper() != "Y":
                            print("votre reponse est invalide")

            else:
                page = -1
        print("les stages correspondants à votre recherche ont tous été parcourus")


if __name__ == "__main__":
    stagevisiteur = Stageclientvisiteur()
    stages = stagevisiteur.get_stage_spe_loc(
        specialite="architecture", localisation="Rennes"
    )
    print(len(stages))
    stagevisiteur.afficher_stage(stages=stages)
