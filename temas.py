import requests
import xml.etree.ElementTree as ET

x=8609
Temas=[]
for i in range(10):
    URL="https://www.senado.cl/wspublico/tramitacion.php?boletin="+str(x)
    response = requests.get(URL)
    nombre="Tramitaciones/tramitacion_"+str(x)+".xml"
    with open(nombre,"w") as file:
        file.write(response.content)
    tree = ET.parse(nombre)
    root = tree.getroot()
    if (len(root)>=1):
        largo=len(root[0][10])
        for i in range (largo):
            Temas.append(root[0][10][i][0].text.encode("UTF-8"))
    print x
    x+=1
print Temas


