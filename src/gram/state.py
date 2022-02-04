import logging

from .handlers import Handler

logger = logging.getLogger(__name__)

###############################################################################
class State:
    """ The `State` class is intended to encapsulate global, shared application
        state.
    """

    ###########################################################################
    def __init__(self):
        """ Constructs a new `State` object.
        """
        self._state = {}

    ###########################################################################
    def start(self, handler, req):
        """ Called whenever a new request is getting handled.

            `handler` is a `Handler` enum which indicates which handler has
            been instantiated.

            `req` is a [tornado.httputil.HTTPServerRequest]
            (https://www.tornadoweb.org/en/stable/httputil.html#tornado.httputil.HTTPServerRequest)
            which contains information about the incoming request.
        """
        logger.info(f'START: {handler} {req.path} {req.method} {req.remote_ip}')

    ###########################################################################
    def finish(self, handler, code, req, elapsed):
        """ Called when a response has been returned to a client.

            `handler` is a `Handler` enum which indicates which handler has
            generated the response.

            `code` is the HTTP status code that was returned.

            `req` is a [tornado.httputil.HTTPServerRequest]
            (https://www.tornadoweb.org/en/stable/httputil.html#tornado.httputil.HTTPServerRequest)
            which contains information about the incoming request.

            `elapsed` is the time that the request took.
        """
        logger.info(f'FINISH: {handler} {code} {req.path} {req.method} {req.remote_ip} {elapsed}')
