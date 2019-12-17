#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import json
import os.path
import Sets
from fuzzywuzzy import fuzz

dict1 = [Sets.Economia_fomento_y_turismo ,"Economia_fomento_y_turismo"]
dict2 = [Sets.Desarrollo_social,"Desarrollo_social"]
dict3 = [Sets.Cultura_y_Educacion,"Cultura_y_Educacion"]
dict4 = [Sets.Justicia_y_derechos_humanos,"Justicia_y_derechos_humanos"]
dict5 = [Sets.Trabajo_y_prevision_social,"Trabajo_y_prevision_social"]
dict6 = [Sets.Obras_publicas,"Obras_publicas"]
dict7 = [Sets.Salud,"Salud"]
dict8 = [Sets.Vivienda_y_urbanismo,"Vivienda_y_urbanismo"]
dict9 = [Sets.Agricultura,"Agricultura"]
dict10 = [Sets.Transporte_y_telecomunicaciones,"Transporte_y_telecomunicaciones"]
dict11 = [Sets.Medio_ambiente_y_bienes_nacionales,"Medio_ambiente_y_bienes_nacionales"]
dict12 = [Sets.Deporte,"Deporte"]
dict13 = [Sets.Mujer_y_la_equidad_de_genero,"Mujer_y_la_equidad_de_genero"]
dict14 = [Sets.Defensa,"Defensa"]
dict15 = [Sets.Hacienda_y_relaciones_exteriores,"Hacienda_y_relaciones_exteriores"]
diccionarios=[dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13,dict14,dict15]
nume=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34"]
#1957
#3820
def operacion(dic,d):
    for q in dic:
        if q not in d:
            d.append(q)
    nd=[]
    for w in d:
        contar=0
        for e in dic:
            if w == e:
                contar=contar+1     
        if contar>=6:
            nd.append(w+"("+str(contar)+")")
    ndd=[(len(nd),nd)] 
    return ndd
for num in range(8000,12827):
    for num2 in nume:
        if os.path.exists("Votaciones/Votacion_boletin"+str(num)+"-"+num2+".xml") == True:
            #palabras2 =[]    
            #words=[]
            d1=[];d2=[];d3=[];d4=[];d5=[];d6=[];d7=[];d8=[];d9=[];d10=[];d11=[];d12=[];d13=[];d14=[];d15=[]
            dic1=[];dic2=[];dic3=[];dic4=[];dic5=[];dic6=[];dic7=[];dic8=[];dic9=[];dic10=[];dic11=[];dic12=[];dic13=[];dic14=[];dic15=[]
            
            for nu in range(1,3816):
                if os.path.exists("palabras/boletin_sesion_"+str(nu)+"-"+str(num)+"-"+num2+".txt") == True:        
                    archivo = open("palabras/boletin_sesion_"+str(nu)+"-"+str(num)+"-"+num2+".txt","r")      
                    print nu,num,num2
                    palabras =[]
                    for i in archivo:
                        x = i.split("\n")
                        palabras.append(x[0])
                    contador = 1
                    for j in diccionarios:
                        for k in palabras:
                            for l in j[0]:
                                if fuzz.token_sort_ratio(k,l) >= 78:
                                    if contador == 1: 
                                        d1.append(k)
                                    if contador == 2: 
                                        d2.append(k)
                                    if contador == 3: 
                                        d3.append(k)
                                    if contador == 4: 
                                        d4.append(k)
                                    if contador == 5: 
                                        d5.append(k)
                                    if contador == 6: 
                                        d6.append(k)
                                    if contador == 7: 
                                        d7.append(k)
                                    if contador == 8: 
                                        d8.append(k)
                                    if contador == 9: 
                                        d9.append(k)
                                    if contador == 10: 
                                        d10.append(k)
                                    if contador == 11: 
                                        d11.append(k)
                                    if contador == 12: 
                                        d12.append(k)
                                    if contador == 13: 
                                        d13.append(k)
                                    if contador == 14: 
                                        d14.append(k)
                                    if contador == 15: 
                                        d15.append(k)
                        contador=contador+1
                    dic1 = dic1 + d1
                    dic2 = dic2 + d2
                    dic3 = dic3 + d3
                    dic4 = dic4 + d4
                    dic5 = dic5 + d5
                    dic6 = dic6 + d6
                    dic7 = dic7 + d7
                    dic8 = dic8 + d8
                    dic9 = dic9 + d9
                    dic10 = dic10 + d10
                    dic11 = dic11 + d11
                    dic12 = dic12 + d12
                    dic13 = dic13 + d13
                    dic14 = dic14 + d14
                    dic15 = dic15 + d15
            nd1=[];nd2=[];nd3=[];nd4=[];nd5=[];nd6=[];nd7=[];nd8=[];nd9=[];nd10=[];nd11=[];nd12=[];nd13=[];nd14=[];nd15=[] 
            nd1 = operacion(dic1,nd1)
            nd2 = operacion(dic2,nd2)
            nd3 = operacion(dic3,nd3)
            nd4 = operacion(dic4,nd4)
            nd5 = operacion(dic5,nd5)
            nd6 = operacion(dic6,nd6)
            nd7 = operacion(dic7,nd7)
            nd8 = operacion(dic8,nd8)
            nd9 = operacion(dic9,nd9)
            nd10 = operacion(dic10,nd10)
            nd11 = operacion(dic11,nd11)
            nd12 = operacion(dic12,nd12)
            nd13 = operacion(dic13,nd13)
            nd14 = operacion(dic14,nd14)
            nd15 = operacion(dic15,nd15)
            nd =[nd1,nd2,nd3,nd4,nd5,nd6,nd7,nd8,nd9,nd10,nd11,nd12,nd13,nd14,nd15]
            word = []
            c=0
            for i in diccionarios:
                word.append((nd[c],i[1]))
                c=c+1
            word.sort(reverse=True)
            temas=[]
            for lugar in range(0,3):
                temas.append((word[lugar][1],word[lugar][0][0][1]))
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
                with open('Nvota/Votacion_'+c+'.json', 'w') as file:
                    json.dump(Votaciones, file, ensure_ascii=False)      

