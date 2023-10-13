from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from services.pokemon_service import PokemonService


class PokemonListView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Afficher 30 pokemon",
                    "Retour",
                    "Quit",
                ],
            }
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}")

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quit":
            pass

        elif reponse["choix"] == "Retour":
            from view.start_view import StartView

            return StartView()

        elif reponse["choix"] == "Afficher 30 pokemon":
            ListPokemonPrint = PokemonService.get_pokemon_from_webservice(
                self, limit=30
            )
            for i in ListPokemonPrint:
                print(i)

            return PokemonListView()
