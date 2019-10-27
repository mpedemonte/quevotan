import xml.etree.ElementTree as ET
import json


arbol = ET.parse("Legislaturas/legislaturas.xml")
raiz = arbol.getroot()
for i in raiz:
    legislaturas={}
    for j in i:
        x=[]
        x=j.tag.split("}")
        legislaturas[x[1]] = j.text.encode("UTF-8")
        if x[1] == "ID":
            lsesion=[]
            c=j.text
            arbol2 = ET.parse("Sesiones/Sesion_Legislatura_"+j.text.encode("UTF-8")+".xml")
            raiz2 = arbol2.getroot()
            for k in raiz2:
                sesiones={}
                
                for l in k:
                    y=[]
                    y=l.tag.split("}")
                    sesiones[y[1]] = l.text.encode("UTF-8")
                    if y[1] == "ID":
                        n=l.text
                        lsesion.append(n)
                sesiones["ID_Legislatura"] = j.text.encode("UTF-8")        
                with open('Sesiones/Sesion_'+n+'.json', 'w') as file:
                    json.dump(sesiones, file)
        print lsesion
        legislaturas["Sesiones"] = lsesion 


    with open('Legislaturas/Legislatura_'+c+'.json', 'w') as file:
        json.dump(legislaturas, file)      
    