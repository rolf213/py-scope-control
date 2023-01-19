#biblioteki: pyvisa   pyvisa-py   keyboard

import keyboard as key
import pyvisa as visa
import os
rm = visa.ResourceManager()

Ch: str = str(1)

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

def main():
    key.add_hotkey('q', lambda: inst.write("AUToscale"))
#załączanie kanałów
    key.add_hotkey('1', lambda: chanSw('1'))
    key.add_hotkey('2', lambda: chanSw('2'))
    key.add_hotkey('3', lambda: chanSw('3'))
    key.add_hotkey('4', lambda: chanSw('4'))
#wybór kanału
    key.add_hotkey('F1', lambda: chanSel('1'))
    key.add_hotkey('F2', lambda: chanSel('2'))
    key.add_hotkey('F3', lambda: chanSel('3'))
    key.add_hotkey('F4', lambda: chanSel('4'))

    key.add_hotkey('b', lambda: inst.write(":BEEP"))
#wzmocnienie
    key.add_hotkey('w', lambda: ampVert('up'))
    key.add_hotkey('s', lambda: ampVert('down'))
    key.add_hotkey('a', lambda: ampHoriz('left'))
    key.add_hotkey('d', lambda: ampHoriz('right'))
#offset
    key.add_hotkey('ctrl + w', lambda: offVert('up'))
    key.add_hotkey('ctrl + s', lambda: offVert('down'))
    key.add_hotkey('ctrl + a', lambda: offHoriz('left'))
    key.add_hotkey('ctrl + d', lambda: offHoriz('right'))
    
    key.add_hotkey('escape', lambda: close())

    while 1:
        print("wybierz komende: \
        \n1, 2, 3, 4 - załączanie kanału \
        \nF1, F2, F3, F4 - wybór aktywnego kanału \
        \na - autoscale \
        \nb - bip \
        \nw, a, s, d - wzmocnienie, podstawa czasu \
        \nctrl + w, a ,s, d - offset \
        \nesc - przerwij połączenie, zakończ program")
        try:
            key.wait()
        except:
            print("złe polecenie")
        

def chanSw(ch: str):
    state = inst.query(":CHANnel" + ch + ":DISPlay?")
    state = str(1-int(state))
    inst.write(":CHANnel" + ch + ":DISPlay " + state)

def chanSel(ch: str):
    global Ch
    Ch=ch

def ampVert(op: str):
    global Ch
    Ch = str(Ch)
    print(inst.query(":CHANnel" + Ch + ":SCALe?"))
    scale = float(inst.query(":CHANnel" + Ch + ":SCALe?"))
    if op=="up":
        scale=str(scale/1.5)
    elif op=="down":
        scale=str(scale*1.5)
    else:
        print("złe polecenie")
    inst.write(":CHANnel" + Ch + ":SCALe " + scale)

def ampHoriz(op: str):
    print(inst.query(":TIMebase:RANGe?"))
    scale = float(inst.query(":TIMebase:RANGe?"))
    if op=="right":
        scale=str(scale/2)
    elif op=="left":
        scale=str(scale*2)
    else:
        print("złe polecenie")
    print(scale)
    inst.write(":TIMebase:RANGe " + scale)

def offVert(op: str):
    global Ch
    Ch=str(Ch)
    off = float(inst.query(":CHANnel" + Ch + ":SCALe?"))
    # print(inst.query(":CHANnel" + Ch + ":SCALe?"))
    # off = float(inst.query(":CHANnel" + Ch + ":SCALe?"))
    if op=="up":
        off=str(0.1*off)
    elif op=="down":
        off=str(-0.1*off)
    else:
        print("złe polecenie")
    print(off)
    inst.write(":CHANnel" + Ch + ":OFFset" + off)

def offHoriz(op: str):
    print(inst.query(":TIMebase:RANGe?"))
    off = float(inst.query(":TIMebase:RANGe?"))
    print(off)
    if op=="right":
        off=str(0.1*off)
    elif op=="left":
        off=str(-0.1*off)
    else:
        print("złe polecenie")
    print(off)
    inst.write(":TIMebase:WINDow:DELay" + off)

def close():
    inst.close()
    os._exit(1)

while init(input("ip urządzenia: 192.168.0."))==0:
    pass
main()





    
    
    
    


