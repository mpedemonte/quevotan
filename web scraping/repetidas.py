#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
z=1
for k in range(1,3810):
        print (k)
        for z in range(1,17):
                if os.path.exists("palabras/boletin_sesion_"+str(k)+"-"+str(z)+".txt") == True:        
                        archivo = open("palabras/boletin_sesion_"+str(k)+"-"+str(z)+".txt","r")
                    

                        palabras = []
                        palabras2 = []
                        cantpala =[]
                        x=""
                        for i in archivo:
                                x = i.split("\n")
                                palabras.append(x[0])
                        for i in palabras:
                                if i not in palabras2:
                                        palabras2.append(i)
                                        contador = 0
                                        for j in palabras:
                                                if i == j:
                                                        contador=contador+1
                                
                                        cantpala.append((contador,i))
                        cantpala.sort(reverse=True)
                        tuplas =""
                        for i in cantpala:
                                tuplas = tuplas + str(i) +"\n"
                        with open("cantidad2/boletin_sesion_"+str(k)+"-"+str(z)+".txt","w") as file:
                                file.write(tuplas)
                
                