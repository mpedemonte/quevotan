#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import json
import os.path

for num in range(1,40):
    a=[]
    b=[]
    if os.path.exists("Proyectos_ley/Proyecto_ley_Boletin"+str(num)+".xml") == True:
        arbol = ET.parse("Proyectos_ley/Proyecto_ley_Boletin"+str(num)+".xml")
        raiz = arbol.getroot()
        print num

        for i in raiz:
            proyectos={}
            for j in i:
                print "-------"
                print j.tag
                sub={}
                for k in j:
                    print k.text
                    for m in k:
                        print m.tag
                    if k.text == None:
                        sub[k.tag] = ""
                    else:
                        texto = k.text.encode("utf8")
                        sub[k.tag] = texto
                print sub