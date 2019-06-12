import requests
import services.config.settings as config
import services.common.serializer as serializer
import services.common.middleware as middleware

class Route:
    def __init__(self, pickup, dropoff, eta):
        self.pickup = pickup
        self.dropoff = dropoff
        self.eta = eta

def compute_route(pickup, dropoff):
    uri = ('http://%s/route?pickup=%s&dropoff=%s' % (config.ROUTE_HOST, pickup, dropoff) )
    
    try:
        # response = requests.get(uri)
        response = middleware.http_get(uri, service_name='route')
        response_json = response.json()
        return serializer.json_to_obj(response_json)
    except Exception:
        return 'ERROR'