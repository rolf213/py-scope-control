def kan():
    k = str(input("wybierz kanał: "))
    stan = inst.query(":CHANnel" + k + ":DISPlay?")
    stan = str(1-int(stan))
    inst.write(":CHANnel" + k + ":DISPlay " + stan)





    
    
    
    


