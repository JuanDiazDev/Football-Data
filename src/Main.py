import Leagues
import Standings


def main():
    country = input("Country: ")
    s = Leagues.Leagues(country)
    res = s.get_leagues()
    all_leagues = []
    for key in res:
        all_leagues.append(key)
    if not all_leagues:
        print("This country has no official football league yet")
    else:
        print(all_leagues)
        league_country = input("League: ")
        league_id = res[league_country]
        positions_country = Standings.Standings(league_id)
        ranking = positions_country.get_standings()
        if ranking:
            for i in ranking:
                print(i)
        else:
            print("The data you requested is currently unavailable")


if __name__ == "__main__":
    main()
