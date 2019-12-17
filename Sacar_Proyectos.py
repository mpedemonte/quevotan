#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import xml.etree.ElementTree as ET

#TODOS LAS ETIQUETAS <br> DEL BOLETIN SON ELIMINADAS
for x in range (1,3816):
    if os.path.exists("Boletines/boletin_sesion_"+str(x)+".xml") == True:
        nombre = "Boletines/boletin_sesion_"+str(x)+".xml"
        aD=open(nombre,"r")
        texto=aD.read()
        texto=texto.replace("<br />","")
        aD.close()
        aF=open(nombre,"w")
        aF.write(texto)



#FOR QUE RECORRE TODOS LOS BOLETINES DESCARGADOS Y EXTRAE LOS PROYECTOS DE LOS BOLETINES

for arch in range(1,3816):
    #si existe el archivo busca los proyectos
    if os.path.exists("Boletines/boletin_sesion_"+str(arch)+".xml") == True:
        aBol=[]
        arbol=ET.parse('Boletines/boletin_sesion_'+str(arch)+'.xml')
        raiz= arbol.getroot()
        etiquetas=[]
        c=0
        k=0
        n=0
        a=1

        for i in raiz:
            for j in i:
                etiquetas.append(j.tag)
         
        if "FACIL_DESPACHO" in etiquetas:
            c=etiquetas.index("FACIL_DESPACHO")
        if "ORDEN_DIA" in etiquetas:
            k=etiquetas.index("ORDEN_DIA")
        if "TABLA" in etiquetas:
            n=etiquetas.index("TABLA")
        if etiquetas == []:
            continue
        
        #ETIQUETA FACIL DESPACHO
        for i in raiz[0][c].findall("PROYECTO_LEY"):
            palabra=""
            ar=[]
            boletin=i.get("BOLETIN").encode("UTF-8")
            boletin = boletin.replace("y","")
            boletin = boletin.replace("Y","")
            boletin = boletin.replace(";","*")
            boletin = boletin.replace(".","")
            boletin = boletin.replace(",","")
            boletin = boletin.replace("(S)","")
            boletin = boletin.replace("(S)\n","")
            boletin = boletin.replace("\n","")
            boletin = boletin.replace("BOLETINES NOS ","")
            boletin = boletin.replace("NOS ","")
            boletin = boletin.replace("BOLETÝN N° ","")
            boletin = boletin.replace("N° ","")
            boletin = boletin.replace("° ","")
            boletin = boletin.replace("Nº ","")
            boletin = boletin.replace("boletín ","")
            boletin = boletin.replace("  ","*")
            boletin = boletin.replace(" ","")
            boletin = boletin.replace("*","\n")
            boletin = boletin.replace("/","-")
            boletin=boletin.split("\n")
            for j in boletin:
                ar=j.split("-")
                if len(ar[0])>5:
                    aBol.append(j)
            if i.text != None:
                palabra=palabra+i.text.encode("UTF-8")+"\n"
            for j in i:
                if j.tag != "VOTACION" and j.tag != "INDICACIONES":
                    if j.text != None:
                        palabra=palabra+j.text.encode("UTF-8")+"\n"
            for j in boletin:
                with open("Proyectos/boletin_sesion_"+str(arch)+"-"+j+".txt","w") as file:
                    file.write(palabra)        
        #ETIQUETA ORDEN DIA
        for i in raiz[0][k].findall("PROYECTO_LEY"):
            palabra=""
            ar=[]
            boletin=i.get("BOLETIN").encode("UTF-8")
            boletin = boletin.replace("y","")
            boletin = boletin.replace("Y","")
            boletin = boletin.replace(";","*")
            boletin = boletin.replace(".","")
            boletin = boletin.replace(",","")
            boletin = boletin.replace("(S)","")
            boletin = boletin.replace("(S)\n","")
            boletin = boletin.replace("\n","")
            boletin = boletin.replace("BOLETINES NOS ","")
            boletin = boletin.replace("NOS ","")
            boletin = boletin.replace("BOLETÝN N° ","")
            boletin = boletin.replace("N° ","")
            boletin = boletin.replace("° ","")
            boletin = boletin.replace("Nº ","")
            boletin = boletin.replace("boletín ","")
            boletin = boletin.replace("  ","*")
            boletin = boletin.replace(" ","")
            boletin = boletin.replace("*","\n")
            boletin = boletin.replace("/","-")
            boletin=boletin.split("\n")
            for j in boletin:
                ar=j.split("-")
                if len(ar[0])>5:
                    aBol.append(j)
            if i.text != None:
                palabra=palabra+i.text.encode("UTF-8")+"\n"
            for j in i:
                if j.tag != "VOTACION" and j.tag != "INDICACIONES":
                    if j.text != None:
                        palabra=palabra+j.text.encode("UTF-8")+"\n"
            for j in boletin:
                with open("Proyectos/boletin_sesion_"+str(arch)+"-"+j+".txt","w") as file:
                    file.write(palabra)   
        #ETIQUETA TABLA
        for i in raiz[0][n].findall("PROYECTO_LEY"):
            palabra=""
            ar=[]
            boletin=i.get("BOLETIN").encode("UTF-8")
            boletin = boletin.replace("y","")
            boletin = boletin.replace("Y","")
            boletin = boletin.replace(";","*")
            boletin = boletin.replace(".","")
            boletin = boletin.replace(",","")
            boletin = boletin.replace("(S)","")
            boletin = boletin.replace("(S)\n","")
            boletin = boletin.replace("\n","")
            boletin = boletin.replace("BOLETINES NOS ","")
            boletin = boletin.replace("NOS ","")
            boletin = boletin.replace("BOLETÝN N° ","")
            boletin = boletin.replace("N° ","")
            boletin = boletin.replace("° ","")
            boletin = boletin.replace("Nº ","")
            boletin = boletin.replace("boletín ","")
            boletin = boletin.replace("  ","*")
            boletin = boletin.replace(" ","")
            boletin = boletin.replace("*","\n")
            boletin = boletin.replace("/","-")
            boletin=boletin.split("\n")
            for j in boletin:
                ar=j.split("-")
                if len(ar[0])>5:
                    aBol.append(j)
            if i.text != None:
                palabra=palabra+i.text.encode("UTF-8")+"\n"
            for j in i:
                if j.tag != "VOTACION" and j.tag != "INDICACIONES":
                    if j.text != None:
                        palabra=palabra+j.text.encode("UTF-8")+"\n"
            for j in boletin:
                with open("Proyectos/boletin_sesion_"+str(arch)+"-"+j+".txt","w") as file:
                    file.write(palabra)   
        if aBol != []:
            with open("NBoletines/boletin"+str(arch)+".txt","w") as file:
                for i in aBol:
                    file.write(i+"\n")
        