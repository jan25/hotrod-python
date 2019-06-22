# Jaeger HotROD written in Python

HotROD is a set of 4 simple services- frontend, customer, driver, route. It can find and assign the nearest driver to a chosen customer on the frontend page.

The original HotROD app was written in Go by Jaeger team. This rewrite in python using Flask is part of my learning tracing and how it works in the services world.

I used jaeger-client to instrument the services by writing a common middleware. Alternate(maybe better) solution would be use framework specific tracing clients so we wouldn't have to write the middleware layer. At the time of creating this project the opentracing-flask had compatibility issues with its latest release, which is why the services are instrumented manually using middleware.

## Run
- Start up services using docker-compose.yml
```
$ docker-compose up
```
- HotR.O.D. app is available at [localhost:8080](localhost:8080)
- Jaeger UI is available at [localhost:16686](localhost:16686)
------------------------
### Todo
- [x] setup services and connect them
- [x] add driver file to kick start all services from one place [Upd: temporarily docker-compose solves this]
- [ ] add logging to each service
- [ ] improve metadata in traces
- [x] instrument services and push traces to jaeger
- [ ] Fix unset proxy stuff from docker-compose.yml

>
> **Credits** Blog post on HotR.O.D application https://medium.com/opentracing/take-opentracing-for-a-hotrod-ride-f6e3141f7941
>