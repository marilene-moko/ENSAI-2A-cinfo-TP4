import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


class Notification:
    @staticmethod
    def send_email(receiver_email, subject, body):
        # Récupérez les informations sensibles à partir des variables d'environnement
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "smartinternshipnotifications@gmail.com"
        password = "ojwj nxoq ider axps"

        # Créez un objet MIMEMultipart
        message = MIMEMultipart()

        # Ajoutez des informations à l'e-mail
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

    @staticmethod
    def notify_internship(
        notif_sender,
        internship_name,
        intership_specialite,
        internship_date,
        internship_localisation,
        receiver_email,
    ):
        cwd = os.getcwd()
        # Charger le contenu du modèle d'e-mail depuis le fichier email_template.txt
        with open(cwd + "/src/utils/email_template.txt", "r") as file:
            email_template = file.read()

        # Remplacer les placeholders dans le modèle
        email_template = email_template.replace("{notif_sender}", notif_sender)
        email_template = email_template.replace("{internship_name}", internship_name)
        email_template = email_template.replace(
            "{internship_specialite}", intership_specialite
        )
        email_template = email_template.replace("{intership_date}", internship_date)
        email_template = email_template.replace(
            "{internship_localisation}", internship_localisation
        )

        # Sujet de l'e-mail
        subject = "Nouvelle offre de stage : " + internship_name

        # Envoyer l'e-mail
        Notification().send_email(receiver_email, subject, email_template)


if __name__ == "__main__":
    receiver_email = "suzanne.heidsieck@eleve.ensai.fr"
    body = "testtest"
    subject = "test"
    send_email(receiver_email, subject, body)
    # Exemple d'utilisation de la fonction notify_internship
    receiver = "suzanne.heidsieck@eleve.ensai.fr"
    notify_internship(
        "Maude Mathieu", "Offre de stage chez Bacchus Corporation", receiver
    )
