import asyncio
import json
import os
from threading import Thread

import requests

from game.team import Team
from loader.matches_loader import MatchesConfigLoader
from game.match import Match


class ExternalProdeAPI:
    teams_map = {}
    __instance = None
    api_uri = ""

    @staticmethod
    def get_instance():
        if ExternalProdeAPI.__instance is None:
            ExternalProdeAPI.__instance = ExternalProdeAPI()
        return ExternalProdeAPI.__instance

    @staticmethod
    def get_team_name_by_id(id):
        team = ExternalProdeAPI.get_instance().teams_map.get(int(id))
        return team.get_name()

    @staticmethod
    def get_team_flag_by_id(id):
        team = ExternalProdeAPI.get_instance().teams_map.get(int(id))
        return team.get_flag()

    @staticmethod
    def get_team(token, id):
        equipo = None

        if token is None:
            return equipo

        request = requests.get('http://api.cup2022.ir/api/v1/team/{}'.format(id), headers={
            'Authorization': 'Bearer {}'.format(token),
        })

        request_json = json.loads(request.text)

        return request_json

    @staticmethod
    def get_token():
        try:
            myobj = {
                "email": "andresiphone132021@gmail.com",
                "password": "arboleda"
            }

            login = requests.post('http://api.cup2022.ir/api/v1/user/login', json=myobj)

            return json.loads(login.text)["data"]["token"]
        except:
            print("Se Produjo un error tratando de obtener el token!")
        return None

    @staticmethod
    def download():
        import pathlib

        path = str(pathlib.Path(__file__).parent.resolve()) + '/../resources'

        os.chdir(path)

        if not os.path.exists(path + "/partidos"):
            os.mkdir("partidos")

        os.chdir(path + "/partidos")

        token = ExternalProdeAPI.get_token()

        ExternalProdeAPI.download_matches_task(token)

        asyncio.run(ExternalProdeAPI.download_team_files(token))

    @staticmethod
    def download_matches_task(token):
        thread = Thread(target=ExternalProdeAPI.create_runnable(token))
        thread.start()

    @staticmethod
    def create_runnable(token):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(ExternalProdeAPI.download_matches(token))

    # Download all matches
    @staticmethod
    async def download_matches(token):

        import pathlib

        path = str(pathlib.Path(__file__).parent.resolve()) + '/../resources'

        os.chdir(path)

        if not os.path.exists(path + "/partidos"):
            os.mkdir("partidos")

        os.chdir(path + "/partidos")

        # Current File
        file_name = 'partidos.json'

        # If file of matches doesn't exist it download a new one trough api
        if os.path.exists(file_name):
            file = open(file_name, encoding="utf8")
            config = json.load(file)
            file.close()

            request = requests.get('http://api.cup2022.ir/api/v1/match', headers={
                'Authorization': 'Bearer {}'.format(token),
            })

            request_json = json.loads(request.text)

            # If are not equals it replace contents
            if request_json != config:
                json_object = json.dumps(request_json)
                with open(file_name, "w") as outfile:
                    outfile.write(json_object)

    # Creates a file per each team
    @staticmethod
    async def download_team_files(token):
        for number in range(1, 33):
            asyncio.create_task(ExternalProdeAPI.create_team_file(token, number))

        await asyncio.gather(*asyncio.all_tasks() - {asyncio.current_task()})

    @staticmethod
    async def create_team_file(token, id):
        file_name = '{}.json'.format(str(id))

        if os.path.exists(file_name):
            file = open(file_name, encoding="utf8")

            config = json.load(file)

            file.close()

            ExternalProdeAPI.add_to_dictionary(id, config)
        else:
            dictionary = ExternalProdeAPI.get_team(token, id)

            ExternalProdeAPI.add_to_dictionary(id, dictionary)

            json_object = json.dumps(dictionary)

            with open(file_name, "w") as outfile:
                outfile.write(json_object)

    @staticmethod
    def add_to_dictionary(id, json):
        if len(json["data"]) >= 1:
            name = json["data"][0]["name_en"]
            flag = json["data"][0]["flag"]
            ExternalProdeAPI.get_instance().teams_map[id] = Team(name, flag)
            if id == 31:
                print("Partidos cargados con exito!")

    @staticmethod
    def get_matches():
        matches = []

        request = MatchesConfigLoader.get_matches_config()

        for partido in request["data"]:
            # try:
            equipo_local_id = partido["home_team_id"]
            equipo_visitante_id = partido["away_team_id"]
            ya_fue_jugado = ExternalProdeAPI.has_been_played(partido["finished"])
            fecha = partido["local_date"]

            equipo_local = ExternalProdeAPI.get_instance().get_team_name_by_id(equipo_local_id)
            equipo_visitante = ExternalProdeAPI.get_instance().get_team_name_by_id(equipo_visitante_id)

            bandera_local = ExternalProdeAPI.get_instance().get_team_flag_by_id(equipo_local_id)
            bandera_visitante = ExternalProdeAPI.get_instance().get_team_flag_by_id(equipo_visitante_id)

            matches.append(
                Match(equipo_local, equipo_visitante, bandera_local, bandera_visitante, ya_fue_jugado, fecha))
        # except:
        #   print("Exception " + str(partido))
        #    continue

        return matches

    @staticmethod
    def has_been_played(status):
        if status == "FALSE":
            return False
        else:
            return True
