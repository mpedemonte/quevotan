#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

URL = "http://opendata.congreso.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=3162"

response = requests.get(URL)
with open("feed.xml","w") as file:
    file.write(response.content)


