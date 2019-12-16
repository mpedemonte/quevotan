#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import json
import os.path
import Sets
from fuzzywuzzy import fuzz

dict1 = [Sets.Economia_fomento_y_turismo ,"Economia_fomento_y_turismo"]
dict2 = [Sets.Desarrollo_social,"Desarrollo_social"]
dict3 = [Sets.Cultura_y_Educacion,"cultura_y_Educacion"]
dict4 = [Sets.Justicia_y_derechos_humanos,"justicia_y_derechos_humanos"]
dict5 = [Sets.Trabajo_y_prevision_social,"trabajo_y_prevision_social"]
dict6 = [Sets.Obras_publicas,"obras_publicas"]
dict7 = [Sets.Salud,"salud"]
dict8 = [Sets.Vivienda_y_urbanismo,"vivienda_y_urbanismo"]
dict9 = [Sets.Agricultura,"agricultura"]
dict10 = [Sets.Transporte_y_telecomunicaciones,"transporte_y_telecomunicaciones"]
dict11 = [Sets.Medio_ambiente_y_bienes_nacionales,"medio_ambiente_y_bienes_nacionales"]
dict12 = [Sets.Deporte,"deporte"]
dict13 = [Sets.Mujer_y_la_equidad_de_genero,"mujer_y_la_equidad_de_genero"]
dict14 = [Sets.Defensa,"Defensa"]
dict15 = [Sets.Hacienda_y_relaciones_exteriores,"Hacienda_y_relaciones_exteriores"]
diccionarios=[dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13,dict14,dict15]
nume=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40"]

for nu in range(1435,3820):
    for num in range(1,13000):
            for num2 in nume:    
                if os.path.exists("palabras/boletin_sesion_"+str(nu)+"-"+str(num)+"-"+num2+".txt") == True:        
                    archivo = open("palabras/boletin_sesion_"+str(nu)+"-"+str(num)+"-"+num2+".txt","r")      
                    print nu,num,num2
                    palabras =[]
                    palabras2 =[]
                    for i in archivo:
                        x = i.split("\n")
                        palabras.append(x[0])
                    for j in diccionarios:
                        palabras1=[]
                        contar=[]
                        for k in palabras:
                            for l in j[0]:
                                contador = 0
                                if fuzz.token_sort_ratio(k,l) >= 78:
                                    if k not in palabras1:
                                        for palabra in palabras:
                                            if k == palabra:
                                                contador=contador+1
                                        if contador >=4:
                                            palabras1.append(k)
                                            contar.append(contador)
                        palabras2.append((len(palabras1),j[1]))
                        #if len(palabras1) >= 1 :
                            #print j[1]
                            #print len(palabras1)
                    palabras2.sort(reverse= True)
                    temas=[]
                    for lugar in range(1,4):
                        temas.append(palabras2[lugar][1])
                    #print temas
                    if os.path.exists("Votaciones/Votacion_boletin"+str(num)+"-"+num2+".xml") == True:
                        arbol = ET.parse("Votaciones/Votacion_boletin"+str(num)+"-"+num2+".xml")
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
                                    Votaciones["Temas"] = temas
                                if x[1] == "ID":
                                    c=j.text
                        with open('Nvotaciones/Votacion_'+c+'.json', 'w') as file:
                           json.dump(Votaciones, file, ensure_ascii=False)      

