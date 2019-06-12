import requests
import services.config.settings as config
import services.common.serializer as serializer
import services.common.middleware as middleware

class Customer:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

def get_customer(customer_id):
    uri = 'http://%s/customer?id=%s' % (config.CUSTOMER_HOST, customer_id)
    try:
        # response = requests.get(uri)
        response = middleware.http_get(uri=uri, service_name='customer')
        response_json = response.json()
        return serializer.json_to_obj(response_json)
    except Exception as e:
        print (e)
        return 'ERROR'
    