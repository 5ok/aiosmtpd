import asyncio
import logging

from aiosmtpd.handlers import Sink
from aiosmtpd.controller import Controller


async def amain(loop):
    cont = Controller(Sink(), hostname='::0', port=8025)
    cont.start()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.create_task(amain(loop=loop))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
