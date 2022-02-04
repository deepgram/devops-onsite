from enum import Enum, auto
import time

import tornado.web

###############################################################################
class Handler(Enum):
    CODE = auto()
    HEALTH = auto()
    MAIN = auto()
    SLEEP = auto()
    STATUS = auto()
    WORK = auto()

###############################################################################
class BaseHandler(tornado.web.RequestHandler):
    """ Base class to simplify some repetitive structure on our handlers.
    """

    ###########################################################################
    def initialize(self, state):
        """ Initialize the request handler. This is called for every request.
        """
        self.state = state

    ###########################################################################
    def prepare(self):
        """ Called just before the request handler.
        """
        self.timer = time.perf_counter()
        self.state.start(self.HANDLER, self.request)

    ###########################################################################
    def on_finish(self):
        """ Called after a response has been sent to the client, at the end of
            a request.
        """
        elapsed = time.perf_counter() - self.timer
        self.state.finish(
            self.HANDLER,
            self.get_status(),
            self.request,
            elapsed
        )

###############################################################################
# Put these at the bottom to avoid circular imports.

from .code import CodeHandler
from .health import HealthHandler
from .main import MainHandler
from .sleep import SleepHandler
from .status import StatusHandler
from .work import WorkHandler
