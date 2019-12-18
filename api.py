from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quevotan'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/quevotan'

mongo = PyMongo(app)
#########################################################################
#                                                                       #
#                                GET                                    #
#                                                                       #
#########################################################################
@app.route('/legislaturas', methods=['GET'])
def get_all_legislaturas():
  Legislaturas = mongo.db.Legislaturas
  output = []
  for s in Legislaturas.find():
    output.append({'ID' : s['ID'],'Tipo' : s['Tipo'], 'FechaInicio' : s['FechaInicio'], 'Numero' : s['Numero'], 'Sesiones' : s['Sesiones'], 'FechaTermino' : s['FechaTermino']})
  return jsonify({'result' : output})

@app.route('/legislaturas/<id>', methods=['GET'])
def get_one_legislatura(id):
  Legislaturas = mongo.db.Legislaturas
  s = Legislaturas.find_one({'ID' : id})
  if s:
    output = {'ID' : s['ID'],'Tipo' : s['Tipo'], 'FechaInicio' : s['FechaInicio'], 'Numero' : s['Numero'], 'Sesiones' : s['Sesiones'], 'FechaTermino' : s['FechaTermino']}
  else:
    output = "No se ha encontrado legislatura"
  return jsonify({'result' : output})
########################################################################
@app.route('/proyecto_ley', methods=['GET'])
def get_all_proyectos():
  proyectos = mongo.db.Proyecto_ley
  output = []
  for s in proyectos.find():
      output.append({'ID' : s['ID'], 'tramitacion' : s['proyectos']['proyecto']['tramitacion'],'oficios' : s['proyectos']['proyecto']['oficios'],'indicaciones' : s['proyectos']['proyecto']['indicaciones'],'observaciones' : s['proyectos']['proyecto']['observaciones'],'urgencias' : s['proyectos']['proyecto']['urgencias'],'votaciones' : s['proyectos']['proyecto']['votaciones'],'comparados' : s['proyectos']['proyecto']['comparados'],'descripcion' : s['proyectos']['proyecto']['descripcion'],'materias' : s['proyectos']['proyecto']['materias'],'autores' : s['proyectos']['proyecto']['autores'],'informes' : s['proyectos']['proyecto']['informes']})
  return jsonify({'result' : output})

@app.route('/proyecto_ley/<id>', methods=['GET'])
def get_one_proyecto(id):
  proyectos = mongo.db.Proyecto_ley
  s = proyectos.find_one({'ID' : id})
  if s:
    output = {'ID' : s['ID'], 'tramitacion' : s['proyectos']['proyecto']['tramitacion'],'oficios' : s['proyectos']['proyecto']['oficios'],'indicaciones' : s['proyectos']['proyecto']['indicaciones'],'observaciones' : s['proyectos']['proyecto']['observaciones'],'urgencias' : s['proyectos']['proyecto']['urgencias'],'votaciones' : s['proyectos']['proyecto']['votaciones'],'comparados' : s['proyectos']['proyecto']['comparados'],'descripcion' : s['proyectos']['proyecto']['descripcion'],'materias' : s['proyectos']['proyecto']['materias'],'autores' : s['proyectos']['proyecto']['autores'],'informes' : s['proyectos']['proyecto']['informes']}
  else:
    output = "No se ha encontrado proyecto de ley"
  return jsonify({'result' : output})
########################################################################

@app.route('/sesion', methods=['GET'])
def get_all_sesion():
  sesiones = mongo.db.Sesion
  output = []
  for s in sesiones.find():
    output.append({'ID' : s['ID'], 'Tipo' : s['Tipo'], 'Fecha' : s['Fecha'], 'ID_Legislatura' : s['ID_Legislatura'], 'Numero' : s['Numero'], 'FechaTermino' : s['FechaTermino'], 'Estado' : s['Estado']})
  return jsonify({'result' : output})

@app.route('/sesion/<id>', methods=['GET'])
def get_one_sesion(id):
  sesion = mongo.db.Sesion
  s = sesion.find_one({'ID' : id})
  if s:
    output = {'ID' : s['ID'], 'Tipo' : s['Tipo'], 'Fecha' : s['Fecha'], 'ID_Legislatura' : s['ID_Legislatura'], 'Numero' : s['Numero'], 'FechaTermino' : s['FechaTermino'], 'Estado' : s['Estado']}
  else:
    output = "No se ha encontrado la sesion"
  return jsonify({'result' : output})
########################################################################
@app.route('/votaciones', methods=['GET'])
def get_all_votaciones():
  votaciones = mongo.db.Votaciones
  output = []
  for s in votaciones.find():
    output.append({'ID' : s['ID'], 'TotalAbstenciones' : s['TotalAbstenciones'], 'Resultado' : s['Resultado'], 'Quorum' : s['Quorum'], 'Tipo' : s['Tipo'], 'Informe' : s['Informe'], 'Fecha' : s['Fecha'], 'TotalAfirmativos' : s['TotalAfirmativos'], 'TotalNegativos' : s['TotalNegativos'], 'Temas' : s['Temas'], 'Articulo' : s['Articulo'], 'Boletin' : s['Boletin'], 'Sesion' : s['Sesion'], 'Tramite' : s['Tramite'], 'TotalDispensados' : s['TotalDispensados']})
  return jsonify({'result' : output})

@app.route('/votaciones/<boletin>', methods=['GET'])
def get_one_votacion(boletin):
  votacion = mongo.db.Votaciones
  s = votacion.find_one({'Boletin' : boletin})
  if s:
    output = {'ID' : s['ID'], 'TotalAbstenciones' : s['TotalAbstenciones'], 'Resultado' : s['Resultado'], 'Quorum' : s['Quorum'], 'Tipo' : s['Tipo'], 'Informe' : s['Informe'], 'Fecha' : s['Fecha'], 'TotalAfirmativos' : s['TotalAfirmativos'], 'TotalNegativos' : s['TotalNegativos'], 'Temas' : s['Temas'], 'Articulo' : s['Articulo'], 'Boletin' : s['Boletin'], 'Sesion' : s['Sesion'], 'Tramite' : s['Tramite'], 'TotalDispensados' : s['TotalDispensados']}
  else:
    output = "No se ha encontrado la votacion"
  return jsonify({'result' : output})


#########################################################################
#                                                                       #
#                                POST                                   #
#                                                                       #
#########################################################################
@app.route('/legislaturas', methods=['POST'])
def add_legislatura():
  Legislaturas = mongo.db.Legislaturas 
  ID = request.json['ID']
  Tipo = request.json['Tipo']
  FechaInicio = request.json['FechaInicio'] 
  Numero = request.json['Numero'] 
  Sesiones = request.json['Sesiones']
  FechaTermino = request.json['FechaTermino']
  legislatura = Legislaturas.insert({'ID' : ID,'Tipo' : Tipo, 'FechaInicio' : FechaInicio, 'Numero' : Numero, 'Sesiones' : Sesiones, 'FechaTermino' : FechaTermino})
  new_legislatura = Legislaturas.find_one({'ID': ID })
  output = {'Sesiones' : new_legislatura['Sesiones'], 'FechaTermino' : new_legislatura['FechaTermino'], 'ID' : new_legislatura['ID'], 'Tipo' : new_legislatura['Tipo'], 'FechaInicio' : new_legislatura['FechaInicio'], 'Numero' : new_legislatura['Numero']}
  return jsonify({'result' : output})

@app.route('/proyecto_ley', methods=['POST'])
def add_proyecto_ley():
  proyectos = mongo.db.Proyecto_ley 
  ID = request.json['ID']
  proyec = request.json['proyectos']
  proyecto = proyectos.insert({'ID':ID, 'proyectos':proyec})
  new_proyecto = proyectos.find_one({'ID': ID })
  output = {'ID' : new_proyecto['ID'], 'tramitacion' : new_proyecto['proyectos']['proyecto']['tramitacion'],'oficios' : new_proyecto['proyectos']['proyecto']['oficios'],'indicaciones' : new_proyecto['proyectos']['proyecto']['indicaciones'],'observaciones' : new_proyecto['proyectos']['proyecto']['observaciones'],'urgencias' : new_proyecto['proyectos']['proyecto']['urgencias'],'votaciones' : new_proyecto['proyectos']['proyecto']['votaciones'],'comparados' : new_proyecto['proyectos']['proyecto']['comparados'],'descripcion' : new_proyecto['proyectos']['proyecto']['descripcion'],'materias' : new_proyecto['proyectos']['proyecto']['materias'],'autores' : new_proyecto['proyectos']['proyecto']['autores'],'informes' : new_proyecto['proyectos']['proyecto']['informes']}

  return jsonify({'result' : output})

@app.route('/sesion', methods=['POST'])
def add_sesiones():
  sesiones = mongo.db.Sesion
  ID = request.json['ID']
  Tipo = request.json['Tipo']
  Fecha = request.json['Fecha']
  ID_Legislatura = request.json['ID_Legislatura']
  Numero = request.json['Numero']
  FechaTermino = request.json['FechaTermino']
  Estado = request.json['Estado']
  sesion = sesiones.insert({'ID' : ID, 'Tipo' : Tipo, 'Fecha' : Fecha, 'ID_Legislatura' : ID_Legislatura, 'Numero' : Numero, 'FechaTermino' : FechaTermino, 'Estado' : Estado})
  s = sesiones.find_one({'ID': ID })
  output = {'ID' : s['ID'], 'Tipo' : s['Tipo'], 'Fecha' : s['Fecha'], 'ID_Legislatura' : s['ID_Legislatura'], 'Numero' : s['Numero'], 'FechaTermino' : s['FechaTermino'], 'Estado' : s['Estado']}
  return jsonify({'result' : output})

@app.route('/votaciones', methods=['POST'])
def add_votacion():
  votaciones = mongo.db.Votaciones
  ID = request.json['ID']
  TotalAbstenciones = request.json['TotalAbstenciones']
  Resultado = request.json['Resultado']
  Quorum = request.json['Quorum']
  Tipo = request.json['Tipo']
  Informe = request.json['Informe']
  Fecha = request.json['Fecha']
  TotalAfirmativos = request.json['TotalAfirmativos']
  TotalNegativos = request.json['TotalNegativos']
  Temas = request.json['Temas']
  Articulo = request.json['Articulo']
  Boletin = request.json['Boletin']
  Sesion = request.json['Sesion']
  Tramite = request.json['Tramite']
  TotalDispensados = request.json['TotalDispensados']
  votacion = votaciones.insert({'ID' : ID, 'TotalAbstenciones' : TotalAbstenciones, 'Resultado' : Resultado, 'Quorum' : Quorum, 'Tipo' : Tipo, 'Informe' : Informe, 'Fecha' : Fecha, 'TotalAfirmativos' : TotalAfirmativos, 'TotalNegativos' : TotalNegativos, 'Temas' : Temas, 'Articulo' : Articulo, 'Boletin' : Boletin, 'Sesion' : Sesion, 'Tramite' : Tramite, 'TotalDispensados' : TotalDispensados})
  s = votaciones.find_one({'Boletin': Boletin })
  output = {'ID' : s['ID'], 'TotalAbstenciones' : s['TotalAbstenciones'], 'Resultado' : s['Resultado'], 'Quorum' : s['Quorum'], 'Tipo' : s['Tipo'], 'Informe' : s['Informe'], 'Fecha' : s['Fecha'], 'TotalAfirmativos' : s['TotalAfirmativos'], 'TotalNegativos' : s['TotalNegativos'], 'Temas' : s['Temas'], 'Articulo' : s['Articulo'], 'Boletin' : s['Boletin'], 'Sesion' : s['Sesion'], 'Tramite' : s['Tramite'], 'TotalDispensados' : s['TotalDispensados']}
  return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)









#@app.route('/votaciones/<id>', methods=['GET'])
#def get_one_votacion(id):
#  votacion = mongo.db.Votaciones
 # s = votacion.find_one({'ID' : id})
  #if s:
   # output = {'ID' : s['ID'], 'TotalAbstenciones' : s['TotalAbstenciones'], 'Resultado' : s['Resultado'], 'Quorum' : s['Quorum'], 'Tipo' : s['Tipo'], 'Informe' : s['Informe'], 'Fecha' : s['Fecha'], 'TotalAfirmativos' : s['TotalAfirmativos'], 'TotalNegativos' : s['TotalNegativos'], 'Temas' : s['Temas'], 'Articulo' : s['Articulo'], 'Boletin' : s['Boletin'], 'Sesion' : s['Sesion'], 'Tramite' : s['Tramite'], 'TotalDispensados' : s['TotalDispensados']}
  #else:
  #  output = "No se ha encontrado la votacion"
  #return jsonify({'result' : output})