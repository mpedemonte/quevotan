"""
LINKS DE AYUDA PARA CREAR LA API

https://blog.nearsoftjobs.com/crear-un-api-y-una-aplicaci%C3%B3n-web-con-flask-6a76b8bf5383

"""

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)

#@app.route("/", methods=["GET","POST"])
#def index():
#    if (request.method == "POST"):
#        some_json = request.get_json()
#        return jsonify({"you sent": some_json}), 201
#    else:
#        return jsonify({"about":"Hello World!"})
#
#@app.route("/multi/<int:num>", methods=["GET"])
#def get_multiply10(num):
#    return jsonify({"result": num*10})

api = Api(app)

"""
Estamos diciendo que la clase Hello hereda de Resource, 
que es lo utiliza Flask para saber cuál ruta se asocia 
con cada clase, de igual forma el método dentro de la clase 
indica qué tipo de operación se realizará. 
En nuestro caso es solo un get, y aplica de igual forma si 
quisiéramos utilizar otra operación, el método se llamaría 
put, post, etc.
"""
class Hello(Resource):
    def get(self, name):
        return {"Hello":name}



"""
Agregamos el recurso a la API y la asociamos 
con la ruta, con la siguiente línea de código
"""
api.add_resource(Hello,'/hello/<name>')
#####http://localhost:5000/hello/world

if __name__ == '__main__':
    app.run(debug=True)