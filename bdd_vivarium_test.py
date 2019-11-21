import sqlite3
from capteur_vivarium_test import *
from datetime import date, datetime, time


#connex_bdd() manages the connexion to the database
def connex_bdd():
    global connex
    global cursor
    
    connex = sqlite3.connect("vivariumbdd.db")
    cursor = connex.cursor()


# insert_data_req() inserts temperature, sensor ID, and date data into the database "bdd_vivarium_test.db"
def insert_data_req():
    
    capteur_list = []
    return_data(capteur_list)
    
    try:
        connex_bdd()
        for each_capteur in capteur_list:
            cursor.execute('INSERT INTO vivariumtable(temperature, id_capteur, current_date) VALUES(?,?,?)', each_capteur)
            connex.commit()
    except Exception as e:
        print("[ERREUR]", e)
        connex.rollback()
    finally:
        connex.close()


#delete_data_req() overwrite datas greater than 3 months
def delete_data_req():
    try:
        connex_bdd()
        cursor.execute('DELETE FROM vivariumtable WHERE current_date < DATETIME("NOW", "-3 months")')
    except Exception as e:
        print("[ERREUR]", e)
    finally:
        connex.close()



