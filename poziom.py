def poziom():
    print(inst.query(":TIMebase:RANGe?"))
    skala = float(inst.query(":TIMebase:RANGe?"))
    op = input("up - zwiększ \ndown - zmniejsz \n")
    if op=="up":
        skala=str(skala/2)
    elif op=="down":
        skala=str(skala*2)
    else:
        print("złe polecenie")
    inst.write(":TIMebase:RANGe " + skala)
