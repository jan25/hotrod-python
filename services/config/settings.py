import os

USE_DOCKER_COMPOSE = 'USE_DOCKER_COMPOSE' in os.environ

JAEGER_HOST = 'jaeger-all-in-one' if USE_DOCKER_COMPOSE else 'localhost'

FRONTEND_PORT = 80 if USE_DOCKER_COMPOSE else 8080
FRONTEND_HOST = 'frontend' if USE_DOCKER_COMPOSE else 'localhost:8080'

# RouteWorkerPoolSize is the size of the worker pool used to query `route` service.
# Can be overwritten from command line.
# RouteWorkerPoolSize = 3
route_worker_pool_size = 3

# 'customer' service

CUSTOMER_PORT = 80 if USE_DOCKER_COMPOSE else 8081
CUSTOMER_HOST = 'customer' if USE_DOCKER_COMPOSE else 'localhost:8081'

# MySQLGetDelay is how long retrieving a customer record takes.
# Using large value mostly because I cannot click the button fast enough to cause a queue.
# MySQLGetDelay = 300 * time.Millisecond
mysql_get_delay = 300

# MySQLGetDelayStdDev is standard deviation
# MySQLGetDelayStdDev = MySQLGetDelay / 10
mysql_get_delay_std_dev = mysql_get_delay // 10

# MySQLMutexDisabled controls whether there is a mutex guarding db query execution.
# When not disabled it simulates a misconfigured connection pool of size 1.
# MySQLMutexDisabled = false
mysql_mutex_disabled = False

# 'driver' service

DRIVER_PORT = 80 if USE_DOCKER_COMPOSE else 8082
DRIVER_HOST = 'driver' if USE_DOCKER_COMPOSE else 'localhost:8082'

# RedisFindDelay is how long finding closest drivers takes.
# RedisFindDelay = 20 * time.Millisecond
redis_find_delay = 20

# RedisFindDelayStdDev is standard deviation.
# RedisFindDelayStdDev = RedisFindDelay / 4
redis_find_delay_std_dev = redis_find_delay // 4

# RedisGetDelay is how long retrieving a driver record takes.
# RedisGetDelay = 10 * time.Millisecond
redis_get_delay = 10

# RedisGetDelayStdDev is standard deviation
# RedisGetDelayStdDev = RedisGetDelay / 4
redis_get_delay_std_dev = redis_get_delay // 4

# 'route' service

ROUTE_PORT = 80 if USE_DOCKER_COMPOSE else 8083
ROUTE_HOST = 'route' if USE_DOCKER_COMPOSE else 'localhost:8083'

# RouteCalcDelay is how long a route calculation takes
# RouteCalcDelay = 50 * time.Millisecond
route_calc_delay = 50

# RouteCalcDelayStdDev is standard deviation
# RouteCalcDelayStdDev = RouteCalcDelay / 4
route_calc_delay_std_dev = route_calc_delay // 4