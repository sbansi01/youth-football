import requests
from bs4 import BeautifulSoup
import csv

# Clemson
clemson_url = "https://clemsontigers.com/sports/football/roster/"
clemson_players = []

try:
    response = requests.get(clemson_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    # Assuming players have class 'person__name'
    player_divs = soup.find_all("div", class_="person__name")

    for player_div in player_divs:
        player_name = player_div.text.strip()
        player_url = "https://clemsontigers.com" + player_div.find("a")["href"]

        # Check if the player is not a coach
        if "/coaches/" not in player_url:
            clemson_players.append([player_name, player_url])

except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
    print(f"Failed to retrieve the web page ({clemson_url}). Status code:", response.status_code)
except Exception as err:
    print(f"An error occurred while processing {clemson_url}: {err}")

# Write the player information to a CSV file
with open("clemson_players.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "URL"])
    writer.writerows(clemson_players)