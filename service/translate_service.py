class TranslateService:
    to_translate = {
        "Iran": "Iran",
        "England": "Inglaterra",
        "United States": "Estados Unidos",
        "Qatar": "Catar",
        "Ecuador": "Ecuador",
        "Senegal": "Senegal",
        "Nederlands": "Nueva Zelanda",
        "Argentina": "Argentina",
        "Saudi Arabia": "Arabia Saudita",
        "Mexico": "Mexico",
        "Poland": "Polonia",
        "France": "Francia",
        "Australia": "Australia",
        "Denmark": "Dinamarca",
        "Tunisia": "Tunisia",
        "Spain": "España",
        "Costa Rica": "Costa Rica",
        "Germany": "Alemania",
        "Japan": "Japon",
        "Belgium": "Belgica",
        "Canada": "Canada",
        "Morocco": "Morocco",
        "Croatia": "Croacia",
        "Brazil": "Brasil",
        "Serbia": "Serbia",
        "Switzerland": "Suiza",
        "Cameroon": "Camerun",
        "Portugal": "Portugal",
        "Ghana": "Ghana",
        "Uruguay": "Uruguay",
        "South Korea": "Korea del Sur",
        "Wales": "Wales",
    }

    @staticmethod
    def translate_to_spanish(name):
        return TranslateService.to_translate[name]