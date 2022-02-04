import asyncio
import logging
import time

from . import BaseHandler, Handler

logger = logging.getLogger(__name__)

###############################################################################
class SleepHandler(BaseHandler):
    """ A request handler for routes of the form `/sleep/{sleep}`.
    """

    HANDLER = Handler.SLEEP

    ###########################################################################
    async def get(self, sleep):
        """ Sleeps for `sleep` milliseconds, then returns a 200 response.
        """
        # Extract the sleep duration
        sleep = int(sleep)

        # Perform the sleep
        before = time.perf_counter()
        await asyncio.sleep(sleep / 1000.)
        after = time.perf_counter()

        # Write the response
        elapsed = after - before
        self.write({'result': 'success', 'data': {'elapsed': elapsed * 1000.}})
