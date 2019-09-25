#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Sets
import os.path

dict1 = [Sets.Economia_fomento_y_turismo ,"Economia_fomento_y_turismo"]
dict2 = [Sets.Desarrollo_social,"Desarrollo_social"]
dict3 = [Sets.cultura_y_Educacion,"cultura_y_Educacion"]
dict4 = [Sets.justicia_y_derechos_humanos,"justicia_y_derechos_humanos"]
dict5 = [Sets.trabajo_y_prevision_social,"trabajo_y_prevision_social"]
dict6 = [Sets.obras_publicas,"obras_publicas"]
dict7 = [Sets.salud,"salud"]
dict8 = [Sets.vivienda_y_urbanismo,"vivienda_y_urbanismo"]
dict9 = [Sets.agricultura,"agricultura"]
dict10 = [Sets.mineria_y_energia,"mineria_y_energia"]
dict11 = [Sets.transporte_y_telecomunicaciones,"transporte_y_telecomunicaciones"]
dict12 = [Sets.medio_ambiente_y_bienes_nacionales,"medio_ambiente_y_bienes_nacionales"]
dict13 = [Sets.deporte,"deporte"]
dict14 = [Sets.mujer_y_la_equidad_de_genero,"mujer_y_la_equidad_de_genero"]
dict15 = [Sets.Defensa,"Defensa"]
dict16 = [Sets.Hacienda_y_relaciones_exteriores,"Hacienda_y_relaciones_exteriores"]
diccionarios=[dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13,dict14,dict15,dict16]


for k in range(1,3810):
        for z in range(1,17):
                if os.path.exists("palabras/boletin_sesion_"+str(k)+"-"+str(z)+".txt") == True:        
                        archivo = open("palabras/boletin_sesion_"+str(k)+"-"+str(z)+".txt","r")
                        palabras =[]
                        
                      
                        for i in archivo:
                            x = i.split("\n")
                            palabras.append(x[0])

                        for j in diccionarios:
                            palabras1=[]
                            for i in palabras:
                                if i in j[0]:
                                    if i not in palabras1:
                                        palabras1.append(i)
                            if len(palabras1) >= 3 :
                                print k,z
                                print j[1]
                                print palabras1
                        
                        
                       