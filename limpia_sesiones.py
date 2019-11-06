import os.path
for x in range (4,52):
    if os.path.exists("Sesiones/sesion_"+str(x)+".xml") == True:
        nombre = "Sesiones/sesion_"+str(x)+".xml"
        aD=open(nombre,"r")
        texto=aD.read()
        texto=texto.replace('<?xml version="1.0" encoding="utf-8"?>',"")
        aD.close()
        aF=open(nombre,"w")
        aF.write(texto)