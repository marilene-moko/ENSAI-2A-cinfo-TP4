from utils.send_email import send_email
import os


def notify_internship(notif_sender, internship_name, receiver_email):
    cwd = os.getcwd()
    # Charger le contenu du modèle d'e-mail depuis le fichier email_template.txt
    with open(cwd + "/src/utils/email_template.txt", "r") as file:
        email_template = file.read()

    # Remplacer les placeholders dans le modèle
    email_template = email_template.replace("{notif_sender}", notif_sender)
    email_template = email_template.replace("{internship_name}", internship_name)

    # Sujet de l'e-mail
    subject = "Nouvelle offre de stage : " + internship_name

    # Envoyer l'e-mail
    send_email(receiver_email, subject, email_template)


if __name__ == "__main__":
    # Exemple d'utilisation de la fonction notify_internship
    receiver = "suzanne.heidsieck@eleve.ensai.fr"
    notify_internship(
        "Maude Mathieu", "Offre de stage chez Bacchus Corporation", receiver
    )
