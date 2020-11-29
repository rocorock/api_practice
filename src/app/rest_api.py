# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response, request
import sqlite3
import logging

api = Flask(__name__)

@api.route('/search', methods=['GET'])

def get_adress_by_zipcode():
    try:
        filepath = "/home/ec2-user/Database/Address.sqlite"
        conn = sqlite3.connect(filepath)
        cur = conn.cursor()
        zipcode = request.args.get('zipcode')
        logging.error("zipcode = %s", zipcode)
        cur.execute("SELECT * FROM Address WHERE zipcode = ?;", (zipcode,))
        add = cur.fetchall()
        if not add:
            raise ValueError("valueError")          
        result = {
            "result":True,
            "data":{
                "id": add[0],
              #  "zipcode" add[1],
               # "zipcode": add[2]
                }
            }
        logging.error("ListError = %s", add) 
    except sqlite3.Error as e:
        abort(500)
    except ValueError as e:
        logging.error("Error = %s", e)
        abort(400)
    
    return make_response(jsonify(result))


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
