from datetime import datetime
from bluepy.btle import Scanner
import datetime

#return_data recovers data from the sensor every 15 sec (temperature, id capteur, mac adresse, current date)
def return_data(list_test):
    scanner = Scanner()
    devices = scanner.scan(15.0)
    
    for dev in devices:
        for (adtype, desc, value) in dev.getScanData():
            if adtype == 22 and len(value) == 38 and value[4:10] == "113901" and value[32:39] == "000000":
                if int(value[12:20]) > 11000000 and int(value[12:20]) < 12000000:
                    
                    temp = int(value[24:28], 16)/100
                    id_capteur = (int(value[12:20]))
                    date = datetime.datetime.now().replace(microsecond = 0).isoformat()
                    adress_mac = dev.addr
                    print(date)
                    print(temp)
                    
                    each_capteur = [temp, id_capteur, date]
                    list_test.append(each_capteur)
                    
                    

              
                   
                    

     

        
