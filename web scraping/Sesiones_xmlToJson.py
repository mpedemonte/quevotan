import xml.etree.ElementTree as ET
import json
import requests

conta=[]
conta2 =[]
for a in range (1,3842):
    conta.append(a)
arbol = ET.parse("Legislaturas/legislaturas.xml")
raiz = arbol.getroot()    
for i in raiz:
    for j in i:
        x=[]
        x=j.tag.split("}")
        if x[1] == "ID":
            arbol = ET.parse("Sesiones/Sesion_Legislatura_"+j.text.encode("UTF-8")+".xml")
            raiz = arbol.getroot()
            for k in raiz:
                palabra={}
                for l in k:
                    y=[]
                    y=l.tag.split("}")
                    palabra[y[1]] = l.text.encode("UTF-8")
                    if y[1] == "ID":
                        c=l.text
                        if int(c) in conta:
                            conta2.append(int(c))
                palabra["ID_Legislatura"] = j.text.encode("UTF-8")
            
                with open('Sesiones/Sesion_'+c+'.json', 'w') as file:
                    json.dump(palabra, file)            

for i in conta2:
    URL="http://opendata.congreso.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+str(i)
    response = requests.get(URL)
    nombre = "Boletines/boletin_sesion_"+str(i)+".xml"
    if len(response.content)>38:
        with open(nombre,"w") as file:
            file.write(response.content)
