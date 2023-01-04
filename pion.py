def pion():
    k = input("wybierz kanał: ")
    print(inst.query(":CHANnel" + k + ":SCALe?"))
    skala = float(inst.query(":CHANnel" + k + ":SCALe?"))
    op = input("up - zwiększ \ndown - zmniejsz \n")
    if op=="up":
        skala=str(skala/2)
    elif op=="down":
        skala=str(skala*2)
    else:
        print("złe polecenie")
    inst.write(":CHANnel" + k + ":SCALe " + skala)
    
    
    
    


