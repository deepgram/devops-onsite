import logging

from . import BaseHandler, Handler

logger = logging.getLogger(__name__)

###############################################################################
class CodeHandler(BaseHandler):
    """ A request handler for routes of the form `/code/{code}`.
    """

    HANDLER = Handler.CODE

    ###########################################################################
    def get(self, code):
        """ This GET handler simply returns an HTTP response with the status
            code set to `code`.

            Valid `code` values are 200-599, inclusive. A 400-response is
            generated for other status codes, which are either invalid or to
            which a body cannot be attached.
        """
        code = int(code)
        if code < 200 or code >= 600:
            self.set_status(400)
            self.write({'result': 'failed', 'reason': 'invalid code'})
        else:
            self.set_status(code)
            self.write({'result': 'success', 'data': {'code': code}})
