#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, url_for
from pymongo import MongoClient

# connect to mongo database hosted on AWS
# the script expects the host name to be in  /etc/hosts file

'''
Set up global variables here
'''
mongo_server = "mongo_api"
mongo_port = "27017"
mongo_user = "admin"
mongo_passwd = ":mysecretpassword@"
connect_string = "mongodb://"+ mongo_user 
                             + mongo_passwd 
                             + mongo_server 
                             + ":" 
                             + mongo_port

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Notfound' } ), 404)


def make_public_page(page):
    new_page = {}
    for field in page:
        if field == 'id':
            new_page['uri'] = url_for('get_page', page_id = page['id'], _external = True)
        else:
            new_page[field] = page[field]
    return new_page



@app.route('/api/v1.0/pages/<int:page_id>',methods = ['GET'])
def get_page(page_id):
    '''
    Can connect otherwise exit with message
    '''
    try:
        connection = MongoClient(connect_string)    # equal to > show dbs
    except:
        exit("Error: Unable to connect to the database") # exit with an error
    '''
    connect to database and pull back collections
    '''
    db = connection.test_database # equal to > use test_database                
    pages = db.pages
    page = pages.find_one({"id": int(page_id)})   <------ this pulls back a document
    if page == None:  <---- if a null set comes back then this works great
        abort(404)
    return jsonify( { 'page' : make_public_page(page[0])} ) <- error says its not json

if __name__ == '__main__':
    app.run(debug = True)