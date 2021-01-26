import requests
from bs4 import BeautifulSoup
import teams

url = 'https://www.skysports.com/premier-league-table'

r = requests.get(url)
# print(r.status_code)

bs = BeautifulSoup(r.text, 'html.parser')
# print(bs).encode("utf-8") # use for printing bs

league_table = bs.find('table', class_ = 'standing-table__table callfn')
# print(league_table)

for team in league_table.find_all('tbody'):
    table = []
    rows = team.find_all('tr')
    header = teams.TeamHeader() #display table header
    for row in rows:
        team = row.find('td', class_ = 'standing-table__cell standing-table__cell--name').text.strip()
        position = row.find_all('td', class_ = 'standing-table__cell')[0].text
        points = row.find_all('td', class_ = 'standing-table__cell')[9].text

        position_int = int(position) - 1 # to be used as index
        team_info = teams.TeamInfo(position, team, points)
        new_team = team_info.add_to_table()
        table.append(new_team)

for table in table:
    print(table)



