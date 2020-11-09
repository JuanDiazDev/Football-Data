import requests


class Leagues:
    def __init__(self, league):
        self.league = league

    url = "https://api-football-v1.p.rapidapi.com/v2/leagues/country/"

    headers = {
        'x-rapidapi-key': "YOUR_API_KEY",
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

    def get_leagues(self):
        league_url = Leagues.url + f"{self.league}/2020"
        response = requests.request("GET", league_url, headers=Leagues.headers)
        response_json = response.json()
        leagues = {}
        for i in response_json["api"]["leagues"]:
            if i["type"] == "League":
                leagues[i["name"]] = i["league_id"]
        return leagues

    def get_cups(self):
        league_url = Leagues.url + f"{self.league}/2020"
        response = requests.request("GET", league_url, headers=Leagues.headers)
        response_json = response.json()
        cups = {}
        for i in response_json["api"]["leagues"]:
            if i["type"] == "Cup":
                cups[i["name"]] = i["league_id"]
        return cups

