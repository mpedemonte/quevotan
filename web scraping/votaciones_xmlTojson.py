#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import json
import os.path

for num in range(1,13000):
    a=[]
    b=[]
    if os.path.exists("Votaciones/Votacion_boletin"+str(num)+".xml") == True:
        arbol = ET.parse("Votaciones/Votacion_boletin"+str(num)+".xml")
        raiz = arbol.getroot()
        for i in raiz:
            Votaciones={}
            for j in i:
                x=[]
                x=j.tag.split("}")
                if j.text == None:
                    Votaciones[x[1]] = ""
                else:
                    if j.text == "\n      ":
                        lsesion={}    
                        for k in j:
                            y=[]
                            y=k.tag.split("}")
                            lsesion[y[1]] = k.text.encode("utf8")
                        Votaciones[x[1]] = lsesion
                    else:
                        Votaciones[x[1]] = j.text.encode("utf8")
                if x[1] == "ID":
                    c=j.text
        with open('Nvotaciones/Votacion_'+c+'.json', 'w') as file:
            json.dump(Votaciones, file, ensure_ascii=False)      
        