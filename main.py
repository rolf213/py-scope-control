#biblioteki: pyvisa   pyvisa-py   keyboard

import keyboard as key
import pyvisa as visa
import inicjalizacja as ini
import kanały
import pion
import poziom
rm = visa.ResourceManager()



while ini.ini(input("ip urządzenia: 192.168.0."))==0:
    pass
while 1:
    k = input ("wybierz komende: \
        \n1. autoscale \
        \n2. kanały \
        \n3. skala pionowa \
        \n4. skala pozioma \
        \n5. bip \
        \n6. zamknij \n")
    if k=="1":
        inst.write(":AUToscale")
    elif k=="2":
        kanały.kan()
    elif k=="3":
        pion.pion()
    elif k=="4":
        poziom.poziom()
    elif k=="5":
        inst.write(":BEEP")
    elif k=="6":
        inst.close()
        break
    else:
        print("złe polecenie")
    print("\n\n\n")





    
    
    
    


