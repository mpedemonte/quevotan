#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import codecs
import os.path
import xmltodict
import xml.etree.ElementTree as ET


#PASA LOS ARCHIVOS DE LEGISLATURAS Y SESIONES(XML) A JSON
arbol = ET.parse("Legislaturas/legislaturas.xml")
raiz = arbol.getroot()
for i in raiz:
    legislaturas={}
    for j in i:
        x=[]
        x=j.tag.split("}")
        legislaturas[x[1]] = j.text.encode("UTF-8")
        if x[1] == "ID":
            lsesion=[]
            c=j.text
            arbol2 = ET.parse("Sesiones/Sesion_Legislatura_"+j.text.encode("UTF-8")+".xml")
            raiz2 = arbol2.getroot()
            for k in raiz2:
                sesiones={}
                
                for l in k:
                    y=[]
                    y=l.tag.split("}")
                    sesiones[y[1]] = l.text.encode("UTF-8")
                    if y[1] == "ID":
                        n=l.text
                        lsesion.append(n)
                sesiones["ID_Legislatura"] = j.text.encode("UTF-8")        
                with open('Jsons/Nsesiones/Sesion_'+n+'.json', 'w') as file:
                    json.dump(sesiones, file, ensure_ascii=False)
        legislaturas["Sesiones"] = lsesion 


    with open('Jsons/Nlegislaturas/Legislatura_'+c+'.json', 'w') as file:
        json.dump(legislaturas, file, ensure_ascii=False)      




#PASA LOS ARCHIVOS DE PROYECTOS DE LEY A JSON
for num in range(1,12830):
    if os.path.exists("Proyectos_ley/Proyecto_ley_Boletin"+str(num)+".xml") == True:
        with open("Proyectos_ley/Proyecto_ley_Boletin"+str(num)+".xml") as fd:
            doc = xmltodict.parse(fd.read())
            doc["ID"]= str(num)
        with codecs.open("Jsons/Nproyecto_ley/Proyecto_ley_Boletin"+str(num)+".json", 'w',encoding='utf-8') as file:
            json.dump(doc, file, ensure_ascii=False)     
