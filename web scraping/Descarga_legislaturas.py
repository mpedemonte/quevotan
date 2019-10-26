#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os.path
import xml.etree.ElementTree as ET

URL="http://opendata.congreso.cl/wscamaradiputados.asmx/getLegislaturas"
response = requests.get(URL)
nombre = "Legislaturas/legislaturas.xml"
with open(nombre,"w") as file:
    file.write(response.content)

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