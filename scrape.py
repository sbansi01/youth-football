import requests
from bs4 import BeautifulSoup
import csv

# URLs of the Maryland, Michigan, and Ohio State football team's roster website
urls = [
    "https://umterps.com/sports/football/roster",
    "https://mgoblue.com/sports/football/roster",
    "https://ohiostatebuckeyes.com/sports/football/roster"
]

# Create a single CSV file to store all the data
with open("football_roster.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    # Write the CSV headers
    writer.writerow(["School", "Name", "Position", "Class", "Hometown", "High School"])

    # Loop through the URLs
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract the school name from the URL
            school_name = url.split('/')[-4]

            # Find player details in the HTML
            player_details = soup.find_all("div", class_="s-person-details")

            for player in player_details:
                # Extract player information
                name = player.find("div", class_="s-person-details__personal-single-line").find("span").text.strip()
                position = player.find("span", class_="s-person-details__bio-stats-item").text.strip()
                class_year = player.find_all("span", class_="s-person-details__bio-stats-item")[1].text.strip()

                # Find player location details in the HTML:
                location_info = player.find_next("div", class_="s-person-card__content__person-contact-info")
                hometown = location_info.find_all("span", class_="s-person-card__content__person__location-item")[0].text.strip()
                high_school = location_info.find_all("span", class_="s-person-card__content__person__location-item")[1].text.strip()

                # Write the player's information to the CSV file along with the school name
                writer.writerow([school_name, name, position, class_year, hometown, high_school])

        else:
            print(f"Failed to retrieve the web page ({url}). Status code:", response.status_code)