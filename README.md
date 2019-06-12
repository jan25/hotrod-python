# Jaeger HOTROD app written in Python3

## Run or develop

- Setup virtual env
```
$ virtualenv .venv
$ source .venv/bin/activate
```
- Start up services using docker-compose.yml
```
$ docker-compose up
```
- OR Start up services locally
```
$ sh run.sh frontend
$ sh run.sh customer
$ sh run.sh route
$ sh run.sh driver
```
- Open HotR.O.D. app at [localhost:8080](localhost:8080)
------------------------
### Done
- setup services and connect them

### Todo
- add driver file to kick start all services from one place [Upd: temporarily docker-compose solves this]
- add logging to each service
- instrument services and push traces to jaeger
- Fix unset proxy stuff from docker-compose.yml

>
> **Credits** Blog post on HotR.O.D application https://medium.com/opentracing/take-opentracing-for-a-hotrod-ride-f6e3141f7941
>