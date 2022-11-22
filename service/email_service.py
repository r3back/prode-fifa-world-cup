import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0e1d729fd97945ec883d51cd83b81ffb.mailgun.org/messages",
        auth=("api", "b4d13194f7f0fe39d0c054318c01aee0-69210cfc-e65bc47f"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox0e1d729fd97945ec883d51cd83b81ffb.mailgun.org>",
              "to": "Andres ponce <andresponce1334@gmail.com>",
              "subject": "Hello Andres ponce",
              "text": "Congratulations Andres ponce, you just sent an email with Mailgun!  You are truly awesome!"})


#send_simple_message()
import asyncio

@asyncio.coroutine
def periodic():
    while True:
        print('periodic')
        yield from asyncio.sleep(1)

def stop():
    task.cancel()

loop = asyncio.get_event_loop()
loop.call_later(5, stop)
task = loop.create_task(periodic())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass