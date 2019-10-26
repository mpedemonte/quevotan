import os.path
for x in range (1,3816):
    if os.path.exists("Boletines/boletin_sesion_"+str(x)+".xml") == True:
        nombre = "Boletines/boletin_sesion_"+str(x)+".xml"
        aD=open(nombre,"r")
        texto=aD.read()
        texto=texto.replace("<br />","")
        aD.close()
        aF=open(nombre,"w")
        aF.write(texto)
