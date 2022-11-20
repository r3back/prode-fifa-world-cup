from me.reb4ck.prode.api.ExternalProdeAPI import ExternalProdeAPI
from me.reb4ck.prode.config.MatchesConfigLoader import MatchesConfigLoader
from me.reb4ck.prode.match.Match import Match


class ProdeAPIService:
    @staticmethod
    def obtener_partidos():
        partidos = []

        request = MatchesConfigLoader.get_matches_config()

        for partido in request["data"]:
            equipo_local_id = partido["home_team_id"]
            equipo_visitante_id = partido["away_team_id"]
            ya_fue_jugado = ProdeAPIService.ya_fue_jugado(partido["finished"])
            fecha = partido["local_date"]

            equipo_local = ExternalProdeAPI.get_instance().get_nombre(equipo_local_id)
            equipo_visitante = ExternalProdeAPI.get_instance().get_nombre(equipo_visitante_id)

            partidos.append(Match(equipo_local, equipo_visitante, ya_fue_jugado, fecha))

        return partidos

    @staticmethod
    def ya_fue_jugado(status):
        if status == "FALSE":
            return False
        else:
            return True
