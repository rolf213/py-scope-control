#biblioteki: pyvisa   pyvisa-py

import keyboard as key
import pyvisa as visa
rm = visa.ResourceManager()

def init(ip):
    try:
        global inst
        global idn
        inst = rm.open_resource("TCPIP0::192.168.0." + ip + "::INSTR")
        idn = inst.query("*IDN?")
        print("połączenie udane \n" + "IDN: \n" + idn + "\n\n")
        return 1
    except:
        print("\npołączenie nieudane\n")
        return 0

def autoscale():
    inst.write(":AUToscale")

def hello():
    inst.write(':DISP:ANN1 ON')
    inst.write(':DISP:ANN1:COL RED')
    inst.write(':DISP:ANN1:BACK INV')
    inst.write(':DISP:ANN1:TEXT "witamy"')

def clear():
    inst.write(":DISP:ANN1 OFF")

def chan(ch: int):#(ch: int):
    ch = str(ch)
    #ch = '1'
    state = inst.query(":CHANnel" + ch + ":DISPlay?")
    state = str(1-int(state))
    inst.write(":CHANnel" + ch + ":DISPlay " + state)
    print("test")

def ampVert(op: str):
    # ch = input("wybierz kanał: ")
    # ch = 1
    # ch = str(ch)
    # print(inst.query(":CHANnel" + ch + ":SCALe?"))
    # scale = float(inst.query(":CHANnel" + ch + ":SCALe?"))
    # #op = input("up - zwiększ \ndown - zmniejsz \n")
    print(inst.query(":CHANnel" + "1" + ":SCALe?"))
    scale = float(inst.query(":CHANnel" + "1" + ":SCALe?"))
    if op=="up":
        scale=str(scale/1.5)
    elif op=="down":
        scale=str(scale*1.5)
    else:
        print("złe polecenie")
    inst.write(":CHANnel" + "1" + ":SCALe " + scale)

def ampHoriz(op: str):
    print(inst.query(":TIMebase:RANGe?"))
    scale = float(inst.query(":TIMebase:RANGe?"))
    print(scale)
    #op = input("up - zwiększ \ndown - zmniejsz \n")
    if op=="right":
        scale=str(scale/2)
    elif op=="left":
        scale=str(scale*2)
    else:
        print("złe polecenie")

    print(scale)
    inst.write(":TIMebase:RANGe " + scale)

def close():
    inst.close()
    return






    
    
    
    


