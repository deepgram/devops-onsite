import asyncio
import logging
import random
import time

from . import BaseHandler, Handler

logger = logging.getLogger(__name__)

###############################################################################
class WorkHandler(BaseHandler):
    """ A request handler for routes of the form `/work`. This sleeps for a
        random amount of time (up to 5 seconds) and returns randomly chosen
        status code.
    """

    HANDLER = Handler.WORK

    ###########################################################################
    async def post(self):
        """ Sleeps for a random amount of time and then returns a randomly
            chosen status code.
        """
        sleep = random.randrange(100, 5000)
        code = random.choices([200, 400, 500], weights=[0.95, 0.04, 0.01])[0]

        # Perform the sleep
        before = time.perf_counter()
        await asyncio.sleep(sleep / 1000.)
        after = time.perf_counter()

        # Write the response
        elapsed = after - before
        self.set_status(code)
        self.write({
            'result': 'success',
            'data': {
                'elapsed': elapsed * 1000.,
                'code': code,
            },
        })
