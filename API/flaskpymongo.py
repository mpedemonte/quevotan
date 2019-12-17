# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'quevotan'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/quevotan'

mongo = PyMongo(app)
########################################################################
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
    output.append({'ID' : s['ID'], 'TotalAbstenciones' : s['TotalAbstenciones'], 'Resultado' : s['Resultado'], 'Quorum' : s['Quorum'], 'Tipo' : s['Tipo'], 'Informe' : s['Informe'], 'Fecha' : s['Fecha'], 'TotalAfirmativos' : s['TotalAfirmativos'], 'TotalNegativos' : s['TotalNegativos'], 'Articulo' : s['Articulo'], 'Boletin' : s['Boletin'], 'Sesion' : s['Sesion'], 'Tramite' : s['Tramite'], 'TotalDispensados' : s['TotalDispensados']})
  return jsonify({'result' : output})

@app.route('/votaciones/<id>', methods=['GET'])
def get_one_votacion(id):
  votacion = mongo.db.Votaciones
  s = votacion.find_one({'ID' : id})
  if s:
    output = {'ID' : s['ID'], 'TotalAbstenciones' : s['TotalAbstenciones'], 'Resultado' : s['Resultado'], 'Quorum' : s['Quorum'], 'Tipo' : s['Tipo'], 'Informe' : s['Informe'], 'Fecha' : s['Fecha'], 'TotalAfirmativos' : s['TotalAfirmativos'], 'TotalNegativos' : s['TotalNegativos'], 'Articulo' : s['Articulo'], 'Boletin' : s['Boletin'], 'Sesion' : s['Sesion'], 'Tramite' : s['Tramite'], 'TotalDispensados' : s['TotalDispensados']}
  else:
    output = "No se ha encontrado la votacion"
  return jsonify({'result' : output})
########################################################################





"""

@app.route('/update', methods=['POST'])
def update():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

"""

if __name__ == '__main__':
    app.run(debug=True)