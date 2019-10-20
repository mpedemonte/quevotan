import requests
import xml.etree.ElementTree as ET

x=1
Temas=[]
for i in range(1,60):
    URL="http://opendata.congreso.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+str(x)
    response = requests.get(URL)
    nombre = "Sesiones/sesion_"+str(x)+".xml"
    if len(response.content)>200:
        with open(nombre,"w") as file:
            file.write(response.content)
    print (x)
    x+=1


