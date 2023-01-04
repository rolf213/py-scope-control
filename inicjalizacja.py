def ini(ip):
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
