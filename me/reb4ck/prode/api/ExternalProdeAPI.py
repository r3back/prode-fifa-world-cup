import asyncio
import glob
import json
import os

import requests


class ExternalProdeAPI():
    __diccionario_nombres = {}
    __instance = None

    @staticmethod
    def get_nombre(id):
        return ExternalProdeAPI.get_instance().__diccionario_nombres.get(int(id))

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

        path = str(pathlib.Path(__file__).parent.resolve()) + '/../../../../resources'

        os.chdir(path)

        if not os.path.exists(path + "/equipos"):
            os.mkdir("equipos")

        os.chdir(path + "/equipos")

        token = ExternalProdeAPI.obtener_token()

        asyncio.run(ExternalProdeAPI.create_all_files(token))

        # files = glob.glob(path + "/teams/*.json")
        # for f in files:
        #    os.remove(f)

    @staticmethod
    async def create_all_files(token):
        for number in range(0, 32):
            #print("Entro " + str(number))
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

            #print(config["data"])
            #print("Termina simple " + str(number))
        else:
            #print("Nashe")

            dictionary = ExternalProdeAPI.obtener_equipo(token, number)

            ExternalProdeAPI.add_to_dictionary(number, dictionary)

            json_object = json.dumps(dictionary)

            with open(file_name, "w") as outfile:
                outfile.write(json_object)
                #print("Termina " + str(number))

    @staticmethod
    def add_to_dictionary(number, json):
        if len(json["data"]) >= 1:
            ExternalProdeAPI.get_instance().__diccionario_nombres[number] = json["data"][0]["name_en"]


ExternalProdeAPI.get_instance()
ExternalProdeAPI.get_instance()
ExternalProdeAPI.get_instance()
#ExternalProdeAPI.descargar()
