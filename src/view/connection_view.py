from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class ConnectionView:
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "email",
                "message": "Email:",
            },
            {
                "type": "password",
                "name": "password",
                "message": "Password:",
            }
        ]

    def display_info(self):
        print("Welcome, please log in")

    def make_choice(self):
        answers = prompt(self.__questions)
        user_email = answers["email"]
        user_password = answers["password"]

        if user_email in users and users[user_email] == user_password:
            print("Login successful!")
            # Vous pouvez ajouter ici la logique pour rediriger l'utilisateur connecté vers la page suivante.
        else:
            print("Login failed. Incorrect email or password.")
            # Vous pouvez ajouter ici la logique pour gérer l'échec de la connexion, par exemple, rediriger l'utilisateur vers la page de connexion.

if __name__ == "__main__":
    connection_view = ConnectionView()
    connection_view.display_info()
    connection_view.make_choice()

