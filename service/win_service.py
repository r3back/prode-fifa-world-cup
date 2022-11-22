import asyncio
from contextlib import suppress

from service.user_service import UserService


class Periodic:
    def __init__(self, func, time):
        self.func = func
        self.time = time
        self.is_started = False
        self._task = None

    async def start(self):
        if not self.is_started:
            self.is_started = True
            # Start task to call func periodically:
            self._task = asyncio.ensure_future(self._run())

    async def stop(self):
        if self.is_started:
            self.is_started = False
            # Stop task and await it stopped:
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task

    async def _run(self):
        while True:
            await asyncio.sleep(self.time)
            self.func()

class WinChecker():

    def check_winners(self):

        for user in UserService.get_instance().get_all_users():
            prodes = user.datos

            for prode in prodes:
                if prode.email_enviado == "false":
                    continue

                local = prode.equipo_local
                visitante = prode.equipo_visitante

                local_goles = prode.equipo_local_goles
                visitante_goles = prode.equipo_visitante_goles



