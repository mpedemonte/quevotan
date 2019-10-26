import xml.etree.ElementTree as ET
import json


arbol = ET.parse("Legislaturas/legislaturas.xml")
raiz = arbol.getroot()
for i in raiz:
    palabra={}
    for j in i:
        x=[]
        x=j.tag.split("}")
        palabra[x[1]] = j.text.encode("UTF-8")
        if x[1] == "ID":
            c=j.text
    with open('Legislaturas/Legislatura_'+c+'.json', 'w') as file:
        json.dump(palabra, file)      
    