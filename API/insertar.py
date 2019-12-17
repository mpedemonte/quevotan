import pymongo
import os.path
import json

def InsertarLegislaturas():
    TotalLegislaturasInsertadas=0
    for i in range(1, 52):
        if os.path.exists("Jsons/Nlegislaturas/Legislatura_"+str(i)+".json") == True:
            with open("Jsons/Nlegislaturas/Legislatura_"+str(i)+".json") as file:
                print ("archivo "+"Legislatura_"+str(i)+".json")
                data = json.load(file)
                x = legislaturas.find({"ID": str(i)}).count()
                if x == 0 :
                    legislaturas.insert(data)
                    TotalLegislaturasInsertadas+=1
                    #print ("INSERTADO")
    output = {'TotalLegislaturasInsertadas' : TotalLegislaturasInsertadas}
    return {'result' : output}

def InsertarSesiones():
    TotalSesionesInsertadas=0
    for i in range(1, 3850):
        if os.path.exists("Jsons/Nsesiones/Sesion_"+str(i)+".json") == True:
            with open("Jsons/Nsesiones/Sesion_"+str(i)+".json") as file:
                print ("archivo "+"Sesion_"+str(i)+".json")
                data = json.load(file)
                x = sesion.find({"ID": str(i)}).count()
                if x == 0 :
                    sesion.insert(data)
                    TotalSesionesInsertadas+=1
                    #print ("INSERTADO")
    output = {'TotalSesionesInsertadas' : TotalSesionesInsertadas}
    return {'result' : output}

def InsertarVotaciones():
    TotalVotacionesInsertadas=0
    for i in range(1, 23100):
        if os.path.exists("Jsons/Nvotaciones/Votacion_"+str(i)+".json") == True:
            with open("Jsons/Nvotaciones/Votacion_"+str(i)+".json") as file:
                print ("archivo "+"Votacion_"+str(i)+".json")
                data = json.load(file)
                x = votacion.find({"ID": str(i)}).count()
                if x == 0 :
                    votacion.insert(data)
                    TotalVotacionesInsertadas+=1
                    #print ("INSERTADO")
    output = {'TotalVotacionesInsertadas' : TotalVotacionesInsertadas}
    return {'result' : output}

def InsertarProyecto_ley():
    TotalProyectosInsertados=0
    for i in range(1, 12830):
        if os.path.exists("Jsons/Nproyecto_ley/Proyecto_ley_Boletin"+str(i)+".json") == True:
            with open("Jsons/Nproyecto_ley/Proyecto_ley_Boletin"+str(i)+".json") as file:
                print ("archivo "+"Proyecto_ley_Boletin"+str(i)+".json")
                data = json.load(file)
                x = proyecto.find({"ID": str(i)}).count()
                if x == 0 :
                    proyecto.insert(data)
                    TotalProyectosInsertados+=1
                    #print ("INSERTADO")
    output = {'TotalProyectosInsertados' : TotalProyectosInsertados}
    return {'result' : output}
            


coneccion = pymongo.MongoClient("localhost", 27017)

db = coneccion.quevotan
legislaturas = db.Legislaturas
sesion = db.Sesion
votacion = db.Votaciones
proyecto = db.Proyecto_ley


######## LA API ESTA LLAMANDO A LAS FUNCIONES
#InsertarLegislaturas()
#InsertarSesiones()
#InsertarVotaciones()
#InsertarProyecto_ley()
