import os
from flask import Flask, send_from_directory, request, jsonify
from uwsgidecorators import postfork

import services.common.middleware as middleware
import services.common.serializer as serializer
import services.config.settings as config
from . import eta

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'web_assets')

app = Flask(__name__)

@postfork
def postfork():
    middleware.init_tracer('frontend')

@app.before_request
def before_request():
    return middleware.before_request(request)

@app.after_request
def after_request(response):
    return middleware.after_request(response)

@app.route("/")
def index():
    return send_from_directory(static_file_dir, 'index.html')

@app.route('/dispatch')
def dispatch():
    return jsonify(handle_dispatch(request))

def handle_dispatch(request):
    customer_id = request.args.get('customer')
    return serializer.obj_to_json(eta.get_best_eta(customer_id))

def start_server(debug):
    app.run(host='0.0.0.0', port=config.FRONTEND_PORT, debug=debug)

if __name__ == "__main__": start_server(debug=True)