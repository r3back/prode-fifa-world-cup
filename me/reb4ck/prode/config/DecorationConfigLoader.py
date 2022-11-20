import json
import os
import pathlib


class DecorationConfigLoader:
    @staticmethod
    def get_ascii_config(nombre):
        path = str(pathlib.Path(__file__).parent.resolve()) + '/../../../../resources/ascii'

        os.chdir(path)

        with open(nombre + ".txt") as file:
            lines = [line.rstrip() for line in file]

        return lines
