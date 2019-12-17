#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import requests
import os.path
import xml.etree.ElementTree as ET

#DESCARGA LOS BOLETINES
x=1
for i in range(1,3842):
    URL="http://opendata.congreso.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+str(x)
    response = requests.get(URL)
    nombre = "Boletines/boletin_sesion_"+str(x)+".xml"
    if len(response.content)>38:
        with open(nombre,"w") as file:
            file.write(response.content)
    print (x)
    x+=1

#DESCARGA LAS LEGISLATURAS
URL="http://opendata.congreso.cl/wscamaradiputados.asmx/getLegislaturas"
response = requests.get(URL)
nombre = "Legislaturas/legislaturas.xml"
with open(nombre,"w") as file:
    file.write(response.content)


#DESCARGA LAS SESIONES

arbol = ET.parse("Legislaturas/legislaturas.xml")
raiz = arbol.getroot()    
for i in raiz:
    for j in i:
        x=[]
        x=j.tag.split("}")
        if x[1] == "ID":
            URL2="http://opendata.congreso.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+j.text.encode("UTF-8")
            response = requests.get(URL2)
            if os.path.exists("Sesiones/Sesion_Legislatura_"+j.text.encode("UTF-8")+".xml") == False:
                nombre = "Sesiones/Sesion_Legislatura_"+j.text.encode("UTF-8")+".xml"
                with open(nombre,"w") as file:
                    file.write(response.content)
