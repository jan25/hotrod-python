import requests
import services.config.settings as config
import services.common.serializer as serializer
import services.common.middleware as middleware

class Driver:
    def __init__(self, driver_id, location):
        self.driver_id = driver_id
        self.location = location

def get_drivers(pickup):
    uri = 'http://%s/find_nearest?pickup=%s' % (config.DRIVER_HOST, pickup)
    # response = requests.get(uri)
    response = middleware.http_get(uri, service_name='driver')
    try:
        drivers = response.json()
        for i in range(len(drivers)):
            drivers[i] = serializer.json_to_obj(drivers[i])
        return drivers
    except Exception as e:
        print (e)
        return 'ERROR'