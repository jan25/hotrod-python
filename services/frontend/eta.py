import services.customer.client as customer_client
import services.driver.client as driver_client
import services.route.client as route_client
from . import client

def get_best_eta(customer_id):
    customer = customer_client.get_customer(customer_id)

    drivers = driver_client.get_drivers(customer.location)

    best_eta, best_driver = -1, None
    for driver in drivers:
        route = route_client.compute_route(customer.location, driver.location)
        if not best_driver or route.eta < best_eta:
            best_driver = driver.driver_id
            best_eta = route.eta

    return client.Response(driver_id=best_driver, eta=best_eta)