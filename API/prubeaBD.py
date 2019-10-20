import pymongo
from pymongo import MongoClient

cliente = MongoClient()

cliente = MongoClient('mongodb://localhost:27017/')

coleccion = cliente.db.col

######Insertar un documento
resultado = coleccion.insert_one({'x':1})
resultado.inserted_id

#######Insertar varios documentos
resultado = coleccion.insert_many([{'x': 2}, {'x': 3}])
resultao.inserted_ids

######Reemplazar un solo documento que coincida
######replace_one(filter, replacement, upsert=False)
######para insertar un nuevo documento si no existe 
# un documento coincidente, use upsert=True
resultado = coleccion.replace_one({'x': 1}, {'y': 1})
resultado.matched_count #recuento
resultado.modified_count #recuento modificado


#####Modificar un solo documento que coincida
# update_one(filter, update, upsert=False)
resultado = coleccion.update_one({'x': 1}, {'x': 3})
# Modificar uno o mas documentos que coincidan
# update_many(filter, update, upsert=False)
resultado = coleccion.update_many({'x': 1}, {'x': 3})


####LEER
#find(filter=None, projection=None, skip=0, limit=0, no_cursor_timeout=False)
resultado = coleccion.find({'x': 1})
#find_one(filter=None)
resultado = coleccion.find_one()


#ELIMINAR
#elimina documento que coincide
#delete_one(filter)
resultao = col.delete_one({'x': 1})
resultao.deleted_count#recuento
#Elimina uno o varios documentos que coincidan
#delete_many(filter)
resultado = coleccion.delete_many({'x': 1})
resultado.deleted_count#recuento

#BUSCA UN DOCUMENTO Y .....
#find_one_and_delete()
#find_one_and_update()
#find_one_and_replace()