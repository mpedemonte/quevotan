#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import codecs
import os.path
import xmltodict

for num in range(1,12830):
    if os.path.exists("Proyectos_ley/Proyecto_ley_Boletin"+str(num)+".xml") == True:
        with open("Proyectos_ley/Proyecto_ley_Boletin"+str(num)+".xml") as fd:
            doc = xmltodict.parse(fd.read())
        with codecs.open("Jsons/Nproyecto_ley/Proyecto_ley_Boletin"+str(num)+".json", 'w',encoding='utf-8') as file:
            json.dump(doc, file, ensure_ascii=False)     
