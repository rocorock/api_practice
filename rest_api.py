# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response, request
import sqlite3
import logging

api = Flask(__name__)

@api.route('/address', methods=['GET'])

def get_address():
    try:
        filepath = "restdata.sqlite"
        conn = sqlite3.connect(filepath)
        cur = conn.cursor()
        postnum = request.args.get('postnum')
        logging.error("postnum = %s", postnum)
        cur.execute("SELECT * FROM address WHERE postnum = ?;", (postnum,))
        add = cur.fetchall() 
    except sqlite3.Error as e:
        abort(404)

    result = {
            "result":True,
            "data":{
                "id": add[0],
              #  "postnum" add[1],
               # "address": add[2]
                }
            }
    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    logging.error("error")
    return make_response(jsonify({'error' : 'Not'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
