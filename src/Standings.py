import requests


class Standings:

    def __init__(self, id):
        self.id = id

    url = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/"

    headers = {
        'x-rapidapi-key': "YOUR_API_KEY",
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

    def get_standings(self):
        standings_url = Standings.url + f"{self.id}"
        response = requests.request("GET", standings_url, headers=Standings.headers)
        response_json = response.json()
        standings = []
        try:
            for i in response_json["api"]["standings"][0]:
                team_name = i["teamName"]
                position = i["rank"]
                points = i["points"]
                standings.append(str(position) + " | " + team_name + "  " + str(points)
                             + " points")
        except IndexError:
            return []
        return standings
