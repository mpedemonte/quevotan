#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
URL="http://opendata.congreso.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+str(x)
response = requests.get(URL)
nombre = "Boletines/boletin_sesion_"+str(x)+".xml"
with open(nombre,"w") as file:
    file.write(response.content)
    