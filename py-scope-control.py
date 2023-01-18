#biblioteki: pyvisa   pyvisa-py   keyboard

import keyboard as key
import pyvisa as visa
rm = visa.ResourceManager()

sw = 1

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
    key.add_hotkey('1', lambda: chan(1))
    key.add_hotkey('2', lambda: chan(2))
    key.add_hotkey('3', lambda: chan(3))
    key.add_hotkey('4', lambda: chan(4))
    # key.add_hotkey('F1', lambda: chan(1))
    # key.add_hotkey('F2', lambda: chan(2))
    # key.add_hotkey('F3', lambda: chan(3))
    # key.add_hotkey('F4', lambda: chan(4))
    key.add_hotkey('b', lambda: inst.write(":BEEP"))
    key.add_hotkey('w', lambda: ampVert('up'))
    key.add_hotkey('s', lambda: ampVert('down'))
    key.add_hotkey('a', lambda: ampHoriz('left'))
    key.add_hotkey('d', lambda: ampHoriz('right'))
    key.add_hotkey('esc', lambda: close())
    while 1:
        print("wybierz komende: \
        \n1, 2, 3, 4 - załączanie kanału \
        \na - autoscale \
        \nb - bip \
        \nw, a, s, d - wzmocnienie, podstawa czasu \
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


def chan(ch: int):
    ch = str(ch)
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
    raise SystemExit()

while init(input("ip urządzenia: 192.168.0."))==0:
    pass
main()





    
    
    
    


