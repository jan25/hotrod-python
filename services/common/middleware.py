import opentracing
from opentracing import tags
from opentracing.propagation import Format
import services.config.settings as config
from jaeger_client import Config
import requests
import logging


log_level = logging.DEBUG
logging.getLogger('').handlers = []
logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

def before_request(request):
    tracer = opentracing.global_tracer()
    span = _before_request(request, tracer)
    tracer.scope_manager.activate(span, True)


def _before_request(request, tracer):
    span_context = tracer.extract(
        format=Format.HTTP_HEADERS,
        carrier=request.headers,
    )
    span = None
    # If span_context: # FINDWHY this didn't work
    if span_context and span_context.has_trace:
        span = tracer.start_span(
            operation_name=request.path,
            child_of=span_context)
    else:
        span = tracer.start_span(
            operation_name=request.path
        )
    span.set_tag('http.url', request.full_path)

    return span


def after_request(response):
    tracer = opentracing.global_tracer()    
    span = tracer.active_span
    if span:
        tracer.scope_manager.active.close()
    # FINDWHY below thing didn't close span
    # scope = tracer.scope_manager.active
    # if scope.span:
        # scope.close()
        # scope.span.finish()

    return response


def http_get(uri, service_name='default-service'):
    # create and serialize a child span and use it as context manager
    current_span = opentracing.global_tracer().active_span
    span, headers = before_http_request(request_uri=uri,
                                        current_span=current_span,
                                        service_name=service_name)

    headers = headers or {}
    with span:
        return requests.get(uri, headers=headers)
    return requests.get(uri)


def before_http_request(request_uri, current_span, service_name):
    outbound_span = opentracing.global_tracer().start_span(
        operation_name=request_uri,
        child_of=current_span
    )

    outbound_span.set_tag('http.url', request_uri)
    if service_name:
        outbound_span.set_tag(tags.PEER_SERVICE, service_name)

    http_header_carrier = {}
    opentracing.global_tracer().inject(
        span_context=outbound_span,
        format=Format.HTTP_HEADERS,
        carrier=http_header_carrier)

    headers = {}
    for key, value in http_header_carrier.items():
        headers[key] = value

    return outbound_span, headers

def init_tracer(service_name):
    JAEGER_HOST = config.JAEGER_HOST

    jaeger_config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                'logging': True,
                                'reporter_flush_interval': 1,
                                'local_agent': {
                                    'reporting_host': JAEGER_HOST
                                    # 'reporting_host': 'localhost'
                                }
                            },
                            service_name=service_name)
    jaeger_config.initialize_tracer()