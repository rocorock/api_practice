# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response, request

import sqlite3
import logging

api = Flask(__name__)

@api.route('/search', methods=['GET'])
def get_address_by_zipcode():
    try:
        filepath = "../../Database/Address.sqlite"
        conn = sqlite3.connect(filepath)
        cur = conn.cursor() 
        zipcode = request.args.get('zipcode')
        cur.execute("SELECT * FROM Address WHERE zipcode = ?;", (zipcode,))
        add = cur.fetchall()
        if not add:
            raise ValueError("valueError")          
        result = {
            "result":True,
            "data":add
            }
    except sqlite3.Error as e:
        abort(500)
    except ValueError as e:
        logging.error("Error = %s", e)
        abort(400)   
    return make_response(jsonify(result))

@api.route('/search/all', methods=['GET'])
def get_all_address():
    try:
        filepath = "../../Database/Address.sqlite"
        conn = sqlite3.connect(filepath)
        cur = conn.cursor() 
        cur.execute("SELECT * FROM Address;")
        add = cur.fetchall()
        logging.error("add[0] = %s", add)
        result = {
            "result":True,
            "data":add
            }
       
    except sqlite3.Error as e:
        abort(500)
    except ValueError as e:
        logging.error("Error = %s", e)
        abort(400)   
    return make_response(jsonify(result))

@api.route('/address', methods=['POST'])
def add_address():
    try:        
        filepath = "../../Database/Address.sqlite"
        conn = sqlite3.connect(filepath)
        cur = conn.cursor() 
        id = request.args.get('id')
        zipcode = request.args.get('zipcode')
        prefecture = request.args.get('prefecture')
        sql = "insert into Address (id, zipcode, prefecture) values (?,?,?)"
        address = (int(id), zipcode, prefecture)
        cur.execute(sql, address)
        conn.commit()        
        cur.execute("SELECT * FROM Address WHERE zipcode = ?;", (zipcode,))
        add = cur.fetchall()
        result = {
            "result":True,
            "data":add
            }
    except sqlite3.Error as e:
        abort(500)
    return make_response(jsonify(result))

@api.route('/address', methods=['DELETE'])
def delete_address():
    try:
        filepath = "../../Database/Address.sqlite"
        conn = sqlite3.connect(filepath)
        cur = conn.cursor() 
        sql = "delete from Address where zipcode = ?;"
        zipcode = request.args.get('zipcode')
        cur.execute(sql, (zipcode,))
        conn.commit() 
    except sqlite3.Error as e:
        abort(500)
    return jsonify(None), 204



@api.errorhandler(400)
def not_found(error):
    logging.error("error")
    return make_response(jsonify({'error' : "BadRequest"}), 400)
    
@api.errorhandler(500)
def not_found(error):
    logging.error("error")
    return make_response(jsonify({'error' : 'DBError'}), 500)
  

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
