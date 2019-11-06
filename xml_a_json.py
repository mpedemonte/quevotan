#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json, xmljson, os.path
from lxml.etree import fromstring, tostring
for x in range (3,52):
    if os.path.exists("Sesiones/sesion_"+str(x)+".xml") == True:
        aD=open("Sesiones/sesion_"+str(x)+".xml","r")
        datos=aD.readlines()
        texto=""
        for i in datos:
            texto+=i
        xml = fromstring(texto)
        texto_completo=json.dumps(xmljson.badgerfish.data(xml))
        aD.close()
        aF=open("Sesiones/sesion_"+str(x)+".json","w")
        aF.write(texto_completo)