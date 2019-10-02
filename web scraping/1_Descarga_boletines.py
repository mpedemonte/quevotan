#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
x=1
for i in range(1,24):
    URL="http://opendata.congreso.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+str(x)
    response = requests.get(URL)
    nombre = "Boletines/boletin_sesion_"+str(x)+".xml"
    if len(response.content)>38:
        with open(nombre,"w") as file:
            file.write(response.content)
    print (x)
    x+=1
