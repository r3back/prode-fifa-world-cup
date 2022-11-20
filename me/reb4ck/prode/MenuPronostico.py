from me.reb4ck.prode.config.DecorationConfigLoader import DecorationConfigLoader
from me.reb4ck.prode.service.ProdeAPIService import ProdeAPIService
from me.reb4ck.prode.user.UserProde import UserProde


class MenuPronostico:
    @staticmethod
    def crear_pronostico():
        partidos = ProdeAPIService().obtener_partidos()

        resultados = []

        for partido in partidos:
            if partido.ya_fue_jugado:
                continue

            for i in range(1, 11):
                print("")




            print("Partido a jugarse el dia: " + partido.fecha)
            print(partido.equipo_local + " Contra " + partido.equipo_visitante)
            print("")
            goles_local = int(input("⚽ Ingresa la cantidad de goles que hara " + partido.equipo_local + ": "))

            goles_visitante = int(input("⚽ Ingresa la cantidad de goles que hara " + partido.equipo_visitante + ": "))

            quien_ganara = None

            if goles_local == goles_visitante:
                print("Has pronosticado un empate entre: ")
                print("")
                print("[1] " + partido.equipo_local)
                print("[2] " + partido.equipo_visitante)
                print("")

                ganador = input("Ingresa el equipo que crees que ganara: ")

                if ganador == "1":
                    quien_ganara = partido.equipo_local
                else:
                    quien_ganara = partido.equipo_visitante
            else:
                if goles_local > goles_visitante:
                    quien_ganara = partido.equipo_local
                else:
                    quien_ganara = partido.equipo_visitante
            resultados.append(
                UserProde(partido.equipo_local, goles_local, partido.equipo_visitante, goles_visitante, quien_ganara))
