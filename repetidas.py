#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
z=428
y=float(0)
for z in range(z,3810):
        if os.path.exists("palabras/boletin_sesion_"+str(z)+".txt") == True:        
                archivo = open("palabras/boletin_sesion_"+str(z)+".txt","r")
                texto = archivo.readline()

                palabras = []
                palabras2 = []
                cantpala =[]
                x=""
                for i in archivo:
                        x = i.split("\n")
                        palabras.append(x[0])
                for i in palabras:
                        contador = 0
                        for j in palabras:
                                if i == j:
                                        contador=contador+1
                        if i not in palabras2:
                                palabras2.append(i)
                                cantpala.append((contador,i))
                cantpala.sort()
                tuplas =""
                for i in cantpala:
                        tuplas = tuplas + str(i) +"\n"
                with open("cantidad/boletin_sesion_"+str(z)+".txt","w") as file:
                        file.write(tuplas)
        print (z)
        y = y+(float(100)/float(3810-z))
        print (str("{0:.2f}".format(y))+"%")
        z+=1