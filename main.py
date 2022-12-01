import asyncio
from threading import Thread

from api.prode_api import ExternalProdeAPI
from frame.main_frame import Main
from service.win_service import Periodic


async def main():
    p = Periodic(lambda: print('test'), 3)

    try:
        await p.start()
        while True:
            await asyncio.sleep(1)
    finally:
        await p.stop()
    '''try:
        print('Start')
        await p.start()
        await asyncio.sleep(3.1)

        print('Stop')
        await p.stop()
        await asyncio.sleep(3.1)

        print('Start 2')
        await p.start()
        await asyncio.sleep(3.1)
    finally:
        await p.stop()'''


def create_runnable():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())


def start_checking():
    thread = Thread(target=create_runnable)
    thread.start()


if __name__ == "__main__":
    ExternalProdeAPI.download()
    #start_checking()
    Main()

