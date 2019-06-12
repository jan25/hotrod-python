from flask import Flask, request, jsonify
from uwsgidecorators import postfork

import services.common.middleware as middleware
import services.config.settings as config
import services.common.serializer as serializer
from . import db

app = Flask(__name__)

@postfork
def postfork():
    print (middleware.init_tracer('customer'))

@app.before_request
def before_request():
    return middleware.before_request(request)

@app.after_request
def after_request(response):
    return middleware.after_request(response)

@app.route('/customer')
def get_customer():
    customer_id = request.args.get('id')
    customer_obj = db.get_customer_by_id(customer_id)
    return jsonify(serializer.obj_to_json(customer_obj))

def start_server(debug):
    app.run(host='0.0.0.0', port=config.CUSTOMER_PORT, debug=debug)

if __name__ == '__main__': start_server(True)