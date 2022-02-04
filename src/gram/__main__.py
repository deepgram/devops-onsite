import argparse
import logging
import sys

import tornado.ioloop
import tornado.web

from . import handlers
from .state import State

logger = logging.getLogger(__name__)

###############################################################################
def parse_args():
    """ Parses command line arguments.
    """
    parser = argparse.ArgumentParser(description='Dummy devops app')
    parser.add_argument('-v', '--verbose', default=0, action='count', help='Increase verbosity.')
    parser.add_argument('-p', '--port', default=8080, type=int, help='Port to listen on.')
    parser.add_argument('-b', '--bind', default='0.0.0.0', help='IP address to bind to.')
    return parser.parse_args()

###############################################################################
def configure_logging(verbosity):
    """ Configures logging.
    """
    logging.basicConfig(
        level={
            0 : logging.INFO,
            1 : logging.DEBUG,
        }.get(verbosity, logging.DEBUG),
        format='[%(levelname)s %(asctime)s %(name)s:%(lineno)s] %(message)s'
    )
    logging.captureWarnings(True)

###############################################################################
def main():
    """ Entrypoint which runs the server.
    """
    args = parse_args()
    configure_logging(args.verbose)

    # Construct global state.
    state = State()

    logger.info("Starting the server.")

    # Construct the web application
    app = tornado.web.Application([
        (r"/", handlers.MainHandler, {'state': state}),
        (r"/code/([0-9]+)", handlers.CodeHandler, {'state': state}),
        (r"/sleep/([0-9]+)", handlers.SleepHandler, {'state': state}),
        (r"/work", handlers.WorkHandler, {'state': state}),
        (r"/status", handlers.StatusHandler, {'state': state}),
        (r"/health", handlers.HealthHandler, {'state': state}),
    ])
    app.listen(args.port, args.bind)
    tornado.ioloop.IOLoop.current().start()

###############################################################################
if __name__ == '__main__':
    sys.exit(main() or 0)
