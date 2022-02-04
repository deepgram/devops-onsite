import logging

from . import BaseHandler, Handler

logger = logging.getLogger(__name__)

###############################################################################
class StatusHandler(BaseHandler):
    """ A request handler for routes of the form `/status`.
    """

    HANDLER = Handler.STATUS

    ###########################################################################
    def get(self):
        """ Return the system health.
        """
        # TODO: Construct the system status.
        data = {}
        code = 200

        # Construct the response.
        self.set_status(code)
        self.write({'result': 'success', 'data': data})
