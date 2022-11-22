import asyncio
import json
import os

import requests

from game.team import Team
from loader.matches_loader import MatchesConfigLoader
from game.match import Match


class ExternalProdeAPI:
    teams_map = {}
    __instance = None

    @staticmethod
    def get_name_by_id(id):
        team = ExternalProdeAPI.get_instance().teams_map.get(int(id))
        return team.get_name()

    @staticmethod
    def get_flag_by_id(id):
        team = ExternalProdeAPI.get_instance().teams_map.get(int(id))
        return team.get_flag()


    @staticmethod
    def get_instance():
        if ExternalProdeAPI.__instance is None:
            ExternalProdeAPI.__instance = ExternalProdeAPI()
        return ExternalProdeAPI.__instance

    @staticmethod
    def obtener_equipo(token, id):

        equipo = None

        if token is None:
            return equipo

        request = requests.get('http://api.cup2022.ir/api/v1/team/{}'.format(id), headers={
            'Authorization': 'Bearer {}'.format(token),
        })

        request_json = json.loads(request.text)

        return request_json

    @staticmethod
    def obtener_equipo_por_id(token, id):

        equipo = None

        if token is None:
            return equipo

        request = requests.get('http://api.cup2022.ir/api/v1/team/{}'.format(id), headers={
            'Authorization': 'Bearer {}'.format(token),
        })

        request_json = json.loads(request.text)

        return request_json["data"][0]["name_en"]

    @staticmethod
    def obtener_token():
        token = None
        try:
            myobj = {
                "email": "andresiphone132021@gmail.com",
                "password": "arboleda"
            }

            login = requests.post('http://api.cup2022.ir/api/v1/user/login', json=myobj)

            y = json.loads(login.text)

            token = y["data"]["token"]

        except:
            print("Se Produjo un error tratando de obtener el token!")
        return token

    @staticmethod
    def descargar():

        import pathlib

        path = str(pathlib.Path(__file__).parent.resolve()) + '/../resources'

        os.chdir(path)

        if not os.path.exists(path + "/equipos"):
            os.mkdir("equipos")

        os.chdir(path + "/equipos")

        token = ExternalProdeAPI.obtener_token()

        asyncio.run(ExternalProdeAPI.create_all_files(token))

    @staticmethod
    async def create_all_files(token):
        for number in range(1, 32):
            asyncio.create_task(ExternalProdeAPI.create_file(token, number))

        await asyncio.gather(*asyncio.all_tasks() - {asyncio.current_task()})

    @staticmethod
    async def create_file(token, number):
        file_name = '{}.json'.format(str(number))

        if os.path.exists(file_name):
            file = open(file_name, encoding="utf8")
            config = json.load(file)
            file.close()

            ExternalProdeAPI.add_to_dictionary(number, config)

        else:
            dictionary = ExternalProdeAPI.obtener_equipo(token, number)

            ExternalProdeAPI.add_to_dictionary(number, dictionary)

            json_object = json.dumps(dictionary)

            with open(file_name, "w") as outfile:
                outfile.write(json_object)

    @staticmethod
    def add_to_dictionary(number, json):
        if len(json["data"]) >= 1:
            name = json["data"][0]["name_en"]
            flag = json["data"][0]["flag"]
            if number == 31:
                print("Partidos cargados con exito!")
            ExternalProdeAPI.get_instance().teams_map[number] = Team(name, flag)

    @staticmethod
    def obtener_partidos():
        partidos = []

        request = MatchesConfigLoader.get_matches_config()

        for partido in request["data"]:
            try:
                equipo_local_id = partido["home_team_id"]
                equipo_visitante_id = partido["away_team_id"]
                ya_fue_jugado = ExternalProdeAPI.ya_fue_jugado(partido["finished"])
                fecha = partido["local_date"]

                equipo_local = ExternalProdeAPI.get_instance().get_name_by_id(equipo_local_id)
                equipo_visitante = ExternalProdeAPI.get_instance().get_name_by_id(equipo_visitante_id)

                partidos.append(Match(equipo_local, equipo_visitante, ya_fue_jugado, fecha))
            except:
                continue

        return partidos

    @staticmethod
    def ya_fue_jugado(status):
        if status == "FALSE":
            return False
        else:
            return True
