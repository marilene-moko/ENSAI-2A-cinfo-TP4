from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from services.listeenvie_service import ListeEnvieService
from view.fct_statut import Statut


class ListeEnvieView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f" {Session().pseudo}",
                "choices": [
                    "Afficher sa liste d'envie",
                    "Sauvegarder une offre dans sa liste",
                    "Modifier sa liste d'envie",
                    "Importer sa liste d'envie",
                    "Exporter sa liste d'envie",
                    "Quitter",
                ],
            }
        ]
        self.__choix = [
            {
                "type": "confirm",
                "message": "Souhaitez-vous ajouter un voeux grâce à son identifiant ?",
                "default": False,
            }
        ]
        self.__parcourir_question = [
            {
                "type": "confirm",
                "message": "Souhaitez-vous parcourir votre recherche ?",
                "default": False,
            }
        ]
        self.__revenir_menu = [
            {
                "type": "confirm",
                "message": "Souhaitez-vous continuer votre parcourt de recherche ?",
                "default": False,
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/border.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Afficher sa liste d'envie":
            liste_envie = ListeEnvieService.afficher_listeEnvie_utilisateur(
                adresse_mail=Session().email
            )
            Statut.def_statut(Session().statut)
            print(liste_envie)

        elif reponse["choix"] == "Sauvegarder une offre dans sa liste":
            choix = prompt(self.__choix)
            if choix is True:
                choix = input(
                    "Choississez l'identifiant du voeux que vous voulez sauvegarder: "
                )
                sauvegarder = ListeEnvieService.ajouter_stage_listeEnvie_utilisateur(
                    adresse_mail=Session().email, identifiant_stage=choix
                )
                Statut.def_statut(Session().statut)
                if sauvegarder is True:
                    print("Votre voeux a bien été sauvegardé")
                else:
                    print(sauvegarder)
            else:

            answers = prompt(self.__questions)
        if (answers[0] is True) & (answers[1] is True):
            localisation = input("Localisation: ")
            specialite = input("Spécialité: ")
            liste_stage = Stageclientvisiteur().get_stage_spe_loc(
                specialite, localisation
            )
            liste_stage_modif = {
                "titre": [
                    liste_stage[stage][1][0:75] for stage in range(0, len(liste_stage))
                ],
                "description": [
                    liste_stage[stage][2][0:100] for stage in range(0, len(liste_stage))
                ],
                "specialite": [
                    liste_stage[stage][3] for stage in range(0, len(liste_stage))
                ],
                "localisation": [
                    liste_stage[stage][4] for stage in range(0, len(liste_stage))
                ],
                "date_publication": [
                    liste_stage[stage][8] for stage in range(0, len(liste_stage))
                ],
            }
            if liste_stage is not None:
                table = tabulate(
                    liste_stage_modif,
                    headers=[
                        "titre",
                        "description",
                        "specialite",
                        "localisation",
                        "date_publication",
                    ],
                    tablefmt="fancy_grid",
                    disable_numparse=True,
                    colalign=["left", "center", "center", "center", "center"],
                )
                print(table)
                # Proposer à l'utilisateur de parcourir la liste des voeux
                parcours = prompt(self.__parcourir_question)
                while parcours[0]:
                    choix_recherche = [
                        {
                            "name": f"Titre: {recherche[1]}, Specialite: {recherche[3]}, Localisation: {recherche[4]}",
                            "value": recherche,
                        }
                        for recherche in liste_stage
                    ]
                    questions = [
                        {
                            "type": "list",
                            "message": "Sélectionnez la recherche que vous voulez approfondir :",
                            "name": "recherche_selectionnee",
                            "choices": choix_recherche,
                        }
                    ]
                    recherche = prompt(questions).get("recherche_selectionnee")
                    affichage = Stageclientvisiteur().afficher_stage(recherche)
                    parcours = prompt(self.__revenir_menu)
                from view.start_view_sans_logo import StartViewSimple

        elif reponse["choix"] == "Modifier sa liste d'envie":
            choix = input(
                "Choississez l'identifiant du voeux que vous voulez supprimer: "
            )
            modif = ListeEnvieService.supprimer_listeEnvie_utilisateur(
                adresse_mail=Session().email, identifiant_voeu=choix
            )
            Statut.def_statut(Session().statut)
            if modif is True:
                print("Votre voeux a bien été supprimé")
            else:
                print(modif)

        elif reponse["choix"] == "Importer sa liste d'envie":
            importer = ListeEnvieService.importer_voeux(adresse_mail=Session().email)
            Statut.def_statut(Session().statut)
            if importer is True:
                print("Votre liste a bien été importée")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")

        elif reponse["choix"] == "Exporter sa liste d'envie":
            exporter = ListeEnvieService.exporter_voeux(adresse_mail=Session().email)
            Statut.def_statut(Session().statut)
            if exporter is True:
                print("Votre liste a bien été exportée")
            else:
                print("Une erreur s'est produite. Veuillez essayer ultérieurement.")
