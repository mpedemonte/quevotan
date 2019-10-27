
#Boletines/boletin_sesion_23.xml
import os.path

import xml.etree.ElementTree as ET

#for que recorre todos los xml

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
            boletin=i.get("BOLETIN").encode("UTF-8")
            #if boletin == "":
             #   if i.text != None:
              #      boletin = filter(str.isdigit, i.text.encode("UTF-8"))
               #     boletin = boletin[0:-2]
            #print boletin
            aBol.append(boletin)
            if i.text != None:
                palabra=palabra+i.text.encode("UTF-8")+"\n"
            for j in i:
                if j.tag != "VOTACION" and j.tag != "INDICACIONES":
                    if j.text != None:
                        
                        palabra=palabra+j.text.encode("UTF-8")+"\n"
            with open("proyectos/boletin_sesion_"+str(arch)+"-"+str(a)+".txt","w") as file:
                file.write(palabra)
                a+=1        
        #ETIQUETA ORDEN DIA
        for i in raiz[0][k].findall("PROYECTO_LEY"):
            palabra=""
            boletin=i.get("BOLETIN").encode("UTF-8")
            #if boletin == "":
             #   if i.text != None:
              #      boletin = filter(str.isdigit, i.text.encode("UTF-8"))
               #     boletin = boletin[0:-2]
            #print boletin  
            aBol.append(boletin)
            if i.text != None:
                palabra=palabra+i.text.encode("UTF-8")+"\n"
            for j in i:
                if j.tag != "VOTACION" and j.tag != "INDICACIONES":
                    if j.text != None:
                        
                        palabra=palabra+j.text.encode("UTF-8")+"\n"
            with open("proyectos/boletin_sesion_"+str(arch)+"-"+str(a)+".txt","w") as file:
                file.write(palabra)
                a+=1
        #ETIQUETA TABLA
        for i in raiz[0][n].findall("PROYECTO_LEY"):
            palabra=""
            boletin=i.get("BOLETIN").encode("UTF-8")
            #if boletin == "":
             #   if i.text != None:
              #      boletin = filter(str.isdigit, i.text.encode("UTF-8"))
               #     boletin = boletin[0:-2]
            #print boletin
            aBol.append(boletin)
            if i.text != None:
                
                palabra=palabra+i.text.encode("UTF-8")+"\n"
            for j in i:
                if j.tag != "VOTACION" and j.tag != "INDICACIONES":
                    if j.text != None:
                        
                        palabra=palabra+j.text.encode("UTF-8")+"\n"
            with open("proyectos/boletin_sesion_"+str(arch)+"-"+str(a)+".txt","w") as file:
                file.write(palabra)
                a+=1
        if aBol != []:
            with open("NBoletines/boletin"+str(arch)+".txt","w") as file:
                for i in aBol:
                    file.write(i+"\n")
        