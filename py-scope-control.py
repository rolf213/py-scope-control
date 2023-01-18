#biblioteki: pyvisa   pyvisa-py   keyboard

import keyboard as key
import pyvisa as visa
rm = visa.ResourceManager()

ch = 1

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
    key.add_hotkey('1', lambda: chan(1,1))
    key.add_hotkey('2', lambda: chan(2,1))
    key.add_hotkey('3', lambda: chan(3,1))
    key.add_hotkey('4', lambda: chan(4,1))
    key.add_hotkey('ctrl + 1', lambda: chan(1,0))
    key.add_hotkey('ctrl + 2', lambda: chan(2,0))
    key.add_hotkey('ctrl + 3', lambda: chan(3,0))
    key.add_hotkey('ctrl + 4', lambda: chan(4,0))
    # key.add_hotkey('F1', lambda: chan(1))
    # key.add_hotkey('F2', lambda: chan(2))
    # key.add_hotkey('F3', lambda: chan(3))
    # key.add_hotkey('F4', lambda: chan(4))
    key.add_hotkey('b', lambda: inst.write(":BEEP"))
    key.add_hotkey('w', lambda: ampVert('up'))
    key.add_hotkey('s', lambda: ampVert('down'))
    key.add_hotkey('a', lambda: ampHoriz('left'))
    key.add_hotkey('d', lambda: ampHoriz('right'))
    key.add_hotkey('ctrl + w', lambda: ampVert('up'))
    key.add_hotkey('ctrl + s', lambda: ampVert('down'))
    key.add_hotkey('ctrl + a', lambda: ampHoriz('left'))
    key.add_hotkey('ctrl + d', lambda: ampHoriz('right'))
    key.add_hotkey('esc', lambda: close())
    while 1:
        print("wybierz komende: \
        \n1, 2, 3, 4 - załączanie kanału \
        \nctrl + 1, 2, 3, 4 - wybór aktywnego kanału \
        \na - autoscale \
        \nb - bip \
        \nw, a, s, d - wzmocnienie, podstawa czasu \
        \nctrl + w, a ,s, d - offset \
        \nesc - przerwij połączenie")
        try:
            key.wait()
        except:
            print("złe polecenie")

        # if k=="1":
        #     inst.write(":AUToscale")
        # elif k=="2":
        #     chan()
        # elif k=="3":
        #     vert()
        # elif k=="4":
        #     horiz()
        # elif k=="5":
        #     inst.write(":BEEP")
        # elif k=="6":
        #     inst.close()
        #     break
        # else:
        #     print("złe polecenie")
        # print("\n\n\n")


def chan(ch: int, sw: int):
    ch = str(ch)
    state = inst.query(":CHANnel" + ch + ":DISPlay?")
    if sw==1:
        state = str(1-int(state))
        inst.write(":CHANnel" + ch + ":DISPlay " + state)


def ampVert(op: str):
    # ch = input("wybierz kanał: ")
    # ch = 1
    # ch = str(ch)
    # print(inst.query(":CHANnel" + ch + ":SCALe?"))
    # scale = float(inst.query(":CHANnel" + ch + ":SCALe?"))
    # #op = input("up - zwiększ \ndown - zmniejsz \n")
    print(inst.query(":CHANnel" + ch + ":SCALe?"))
    scale = float(inst.query(":CHANnel" + ch + ":SCALe?"))
    if op=="up":
        scale=str(scale/1.5)
    elif op=="down":
        scale=str(scale*1.5)
    else:
        print("złe polecenie")
    inst.write(":CHANnel" + ch + ":SCALe " + scale)

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

def offVert(op: str):
    print(inst.query(":CHANnel" + ch + ":SCALe?"))
    off = float(inst.query(":CHANnel" + ch + ":SCALe?"))
    if op=="up":
        off=str(off+0.1*off)
    elif op=="down":
        off=str(off-0.1*off)
    else:
        print("złe polecenie")
    inst.write(":CHANnel" + ch + ":OFFset" + off)

def offHoriz(op: str):
    print(inst.query(":TIMebase:RANGe?"))
    off = float(inst.query(":TIMebase:RANGe?"))
    print(off)
    if op=="right":
        off=str(off+0.1*off)
    elif op=="left":
        off=str(off-0.1*off)
    else:
        print("złe polecenie")

    print(off)
    inst.write(":TIMebase:WINDow:POSition" + off)


def close():
    inst.close()
    raise SystemExit()

while init(input("ip urządzenia: 192.168.0."))==0:
    pass
main()





    
    
    
    


