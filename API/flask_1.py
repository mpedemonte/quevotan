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

class Hello(Resource):
    def get(self, name):
        return {"Hello":name}


api.add_resource(Hello,'/hello/<name>')

if __name__ == '__main__':
    app.run(debug=True)