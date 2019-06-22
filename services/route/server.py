from flask import Flask, request, jsonify
from uwsgidecorators import postfork
import random
import math

import services.config.settings as config
import services.common.serializer as serializer
import services.common.middleware as middleware
from . import client

app = Flask(__name__)

@postfork
def postfork():
    middleware.init_tracer('route')

@app.before_request
def before_request():
    return middleware.before_request(request)

@app.after_request
def after_request(response):
    return middleware.after_request(response)

@app.route('/route')
def route():
    return jsonify(handle_route(request))

def handle_route(request):
    pickup = request.args.get('pickup')
    dropoff = request.args.get('dropoff')
    return serializer.obj_to_json(compute_route(pickup, dropoff))

def compute_route(pickup, dropoff):
    eta = random.randint(2, 15)
    return client.Route(pickup=pickup, dropoff=dropoff, eta=eta)

def start_server(debug):
    app.run(host='0.0.0.0', port=config.ROUTE_PORT, debug=debug)

if __name__ == '__main__': start_server(debug=True)