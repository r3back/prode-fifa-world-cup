import json
import os
import pathlib


class MatchesConfigLoader:
    @staticmethod
    def get_matches_config():
        path = str(pathlib.Path(__file__).parent.resolve()) + '/../../../../resources/partidos'

        os.chdir(path)

        file = open('partidos.json', encoding="utf8")

        config = json.load(file)

        file.close()

        return config