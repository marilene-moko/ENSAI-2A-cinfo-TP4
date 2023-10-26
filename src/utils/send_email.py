import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

if __name__ == '__main__':
    receiver_email = "ebourrigan@gmail.com"
    body = "testtest"
    subject = "test"
    send_email(receiver_email, subject, body)
