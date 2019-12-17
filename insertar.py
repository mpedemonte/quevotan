import pymongo
import os.path
import json

def InsertarLegislaturas():

    for i in range(1, 52):
        if os.path.exists("Jsons/Nlegislaturas/Legislatura_"+str(i)+".json") == True:
            with open("Jsons/Nlegislaturas/Legislatura_"+str(i)+".json") as file:
                data = json.load(file)
                x = legislaturas.find({"ID": str(i)}).count()
                if x == 0 :
                    print 0
                    legislaturas.insert(data)

def InsertarSesiones():

    for i in range(1, 3850):
        if os.path.exists("Jsons/Nsesiones/Sesion_"+str(i)+".json") == True:
            with open("Jsons/Nsesiones/Sesion_"+str(i)+".json") as file:
                data = json.load(file)
                x = sesion.find({"ID": str(i)}).count()
                if x == 0 :
                    sesion.insert(data)

def InsertarVotaciones():

    for i in range(1, 23100):
        if os.path.exists("Jsons/Nvotaciones/Votacion_"+str(i)+".json") == True:
            with open("Jsons/Nvotaciones/Votacion_"+str(i)+".json") as file:
                data = json.load(file)
                x = votacion.find({"ID": str(i)}).count()
                if x == 0 :
                    votacion.insert(data)

def InsertarProyecto_ley():

    for i in range(1, 12830):
        if os.path.exists("Jsons/Nproyecto_ley/Proyecto_ley_Boletin"+str(i)+".json") == True:
            with open("Jsons/Nproyecto_ley/Proyecto_ley_Boletin"+str(i)+".json") as file:
                data = json.load(file)
                x = proyecto.find({"ID": str(i)}).count()
                if x == 0 :
                    proyecto.insert(data)
            


coneccion = pymongo.MongoClient("localhost", 27017)

db = coneccion.quevotan
legislaturas = db.Legislaturas
sesion = db.Sesion
votacion = db.Votaciones
proyecto = db.Proyecto_ley

InsertarLegislaturas()
InsertarSesiones()
InsertarVotaciones()
InsertarProyecto_ley()