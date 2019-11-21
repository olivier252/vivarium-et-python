from bdd_vivarium_test import *
from mail_vivarium_test import *
from capteur_vivarium_test import *
import time


#check_list_scanner manages the temperature level of each capteur
def check_list_scanner():
    list_capteur = []
    return_data(list_capteur) 
    for each_capteur in list_capteur:
        range_temp = each_capteur[0]
        scanner(each_capteur, range_temp)
        
first_alert_temp = False

# scanner() manages the sending of mail and data backup in case of temperature alert
def scanner(each_capteur, temp):
    global first_alert_temp
    if (temp < 24 or temp > 30) and (first_alert_temp is False):
        insert_data_req()
        send_alert_mail(True, each_capteur)
        first_alert_temp = True

    elif (temp > 24 and temp < 30) and (first_alert_temp is True):
        send_alert_mail(False, each_capteur)
        first_alert_temp = False
