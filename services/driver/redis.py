import random
from .client import Driver

def find_drivers_ids(pickup, n=10):
    driver_ids = []
    for _ in range(n):
        random_5digs = custom_rand_int() % 100000
        driver_ids.append("T7%05dC" % random_5digs)
    return driver_ids

def get_driver(driver_id):
    location = "%d,%d" % (custom_rand_int() % 1000, custom_rand_int() % 1000)
    return Driver(driver_id=driver_id, location=location)

def custom_rand_int():
    return random.randint(9999, 10000000)