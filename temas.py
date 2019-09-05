import requests
import xml.etree.ElementTree as ET

x=400
Temas=[]
for i in range(400,12800):
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
dTemas=open("Temas.txt","w")
sTexto=""
for i in Temas:
    sTexto+=i+", "
dTemas.write(sTexto)


