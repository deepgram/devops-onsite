import logging

from . import BaseHandler, Handler

logger = logging.getLogger(__name__)

###############################################################################
class MainHandler(BaseHandler):
    """ A request handler for routes of the form `/`.
    """

    HANDLER = Handler.MAIN

    ###########################################################################
    def get(self):
        """ Simply return a canned 200 response.
        """
        self.write({'result': 'success', 'data': {'message': 'Hello, world!'}})
