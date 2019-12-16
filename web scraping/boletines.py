#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import requests


for i in range(1,3816):
    a=[]
    b=[]
    if os.path.exists("NBoletines/boletin"+str(i)+".txt") == True:
        datos = open("NBoletines/boletin"+str(i)+".txt","r")
        print i
        text = datos.readlines()
        #print text
        for m in text:

            text = m.replace("y","")
            text = text.replace("Y","")
            text = text.replace(";","*")
            text = text.replace(".","")
            text = text.replace(",","")
            text = text.replace("(S)","")
            text = text.replace("(S)\n","")
            text = text.replace("\n","")
            text = text.replace("BOLETINES NOS ","")
            text = text.replace("NOS ","")
            text = text.replace("BOLETÝN N° ","")
            text = text.replace("N° ","")
            text = text.replace("° ","")
            text = text.replace("Nº ","")
            text = text.replace("boletín ","")
            text = text.replace("  ","*")
            text = text.replace(" ","")
            text = text.replace("*","\n")
            text = text.replace("/","-")
            text=text.split("\n")
            #print text
            for j in text:
                a=j.split("-")
                if len(a[0])>5:
                    a[0]=""
                if a[0] != "":
                    b.append(j)
     
        print b
        if len(b)!=0:
            for k in b:
                if os.path.exists("Proyectos_ley/Proyecto_ley_Boletin"+str(k)+".xml") == False:
                    URL="https://www.senado.cl/wspublico/tramitacion.php?boletin="+str(k)
                    response = requests.get(URL)
                    if len(response.content)>244 :
                        nombre = "Proyectos_ley/Proyecto_ley_Boletin"+str(k)+".xml"
                        with open(nombre,"w") as file:
                            file.write(response.content)
        
            for q in b:
                if os.path.exists("Votaciones/Votacion_boletin"+str(q)+".xml")== False:
                    URL="http://opendata.congreso.cl/wscamaradiputados.asmx/getVotaciones_Boletin?prmBoletin="+str(q)
                    response = requests.get(URL)
                    if len(response.content) >181:
                        nombre = "Votaciones/Votacion_boletin"+str(q)+".xml"
                        with open(nombre,"w") as file:
                            file.write(response.content)
        