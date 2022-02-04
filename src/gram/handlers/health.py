import logging

from . import BaseHandler, Handler

logger = logging.getLogger(__name__)

###############################################################################
class HealthHandler(BaseHandler):
    """ A request handler for routes of the form `/health`.
    """

    HANDLER = Handler.HEALTH

    ###########################################################################
    def get(self):
        """ Return the system health.
        """
        # TODO: Determine the system health
        msg = 'healthy'
        code = 200

        # Construct the response.
        self.set_status(code)
        self.write({'result': 'success', 'data': {'health': msg}})
