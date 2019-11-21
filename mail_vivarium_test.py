import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


#send_alert_mail() send an email in case of temperature alert or return to normal
def send_alert_mail(set_alert, capt):
    temperature = capt[0]
    id_sensor = capt[1]
    current_date = datetime.datetime.now().strftime("%d-%m-%Y à %H:%M:%S")
    

    msg = MIMEMultipart()  ## Message à envoyer
    msg['From'] = 'cesiapgroupe1@gmail.com'
    msg['To'] = 'chiniolivier@gmail.com'
    if set_alert:
        msg['Subject'] = "Alerte de température sur le vivarium n° " + str(id_sensor)
        message = "Bonjour, à la date et heure du " + str(current_date) + " le vivarium n° " + str(
        id_sensor) + " est défectueux et présente une température de " + str(temperature)
    else:
        msg['Subject'] = "Fin d'alerte de température sur le vivarium n° " + str(id_sensor)
        message = "A la date du  " + str(current_date) + ", le vivarium n° " + str(
        id_sensor) + " est revenue à une température normale de " + str(temperature)


    msg.attach(MIMEText(message)) ## Corps du message
    mailserver = smtplib.SMTP_SSL('smtp.gmail.com', 465) ## Connexion au serveur sortant (en précisant son nom et son port)
    mailserver.login('cesiapgroupe1@gmail.com', 'V1V4r1um!')## Authentification
    mailserver.sendmail('cesiapgroupe1@gmail.com', 'chiniolivier@gmail.com', msg.as_string())## Envoi du message
    mailserver.quit()## Déconnexion du serveur

