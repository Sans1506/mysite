from flask import Flask, make_response, jsonify, request
from flask_pymongo import PyMongo, MongoClient
import json
from bson.json_util import dumps
from flask_oauthlib.provider import OAuth2Provider
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/Coworking"
oauth = OAuth2Provider(app)
mongo = PyMongo(app)

@app.route('/add',methods=['POST'])
def add_user():
    _json = request.json
    _id_user = _json['id_user']
    _status = _json['status']
    _token = _json['token']
    _tempat = _json['tempat']
    _capacity = _json['capacity']
    _invoice = _json['invoice']
    _is_aktif = _json['is_aktif']

    if _id_user and _status and _token and _tempat and _capacity and _invoice and _is_aktif and request.method == 'POST':

        _id = mongo.db.Order.insert({'id_user':_id_user,'status':_status,'token':_token,'tempat':_tempat,'capacity':_capacity,'invoice':_invoice,'is_aktif':_is_aktif})
        resp = jsonify("User added successfully")

        resp.status_code = 200

        return resp

    else:
        return not_found()

@app.route('/Order')
def Order():
    Order = mongo.db.Order.find()
    resp = dumps(Order)
    return resp

@app.route('/Order/<id>')
def user(id):
    user = mongo.db.Order.find_one({'_id':ObjectId(id)})
    resp = dumps(user)
    return resp

@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.Order.delete_one({'_id': ObjectId(id)})
    resp = jsonify("User delete successfully")

    resp.status_code = 200

    return resp

@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _id_user = _json['id_user']
    _status = _json['status']
    _token = _json['token']
    _tempat = _json['tempat']
    _capacity = _json['capacity']
    _invoice = _json['invoice']
    _is_aktif = _json['is_aktif']

    if _id_user and _status and _token and _tempat and _capacity and _invoice and _is_aktif and _id and request.method == 'PUT':

        mongo.db.Order.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'id_user': _id_user,'status': _status,'token': _token,'tempat': _tempat,'capacity': _capacity,'invoice': _invoice,'is_aktiif': _is_aktif}})

        resp = jsonify("User update successfully")

        resp.status_code = 200

        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message':'Not Found' +' '+ request.url 
    }    
    resp = jsonify(message)

    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run(debug=True)
