import requests
from bs4 import BeautifulSoup
import csv

# URLs of all Power Five football rosters
urls = [
    "https://fightingillini.com/sports/football/roster",
    "https://iuhoosiers.com/sports/football/roster",
    #"https://hawkeyesports.com/sports/football/roster/",
    "https://umterps.com/sports/football/roster",
    "https://mgoblue.com/sports/football/roster",
    "https://msuspartans.com/sports/football/roster",
    "https://gophersports.com/sports/football/roster",
    #"https://huskers.com/sports/football/roster",
    "https://nusports.com/sports/football/roster",
    "https://ohiostatebuckeyes.com/sports/football/roster",
    "https://gopsusports.com/sports/football/roster",
    "https://purduesports.com/sports/football/roster",
    "https://scarletknights.com/sports/football/roster",
    "https://uwbadgers.com/sports/football/roster",
    "https://bceagles.com/sports/football/roster",
    #"https://clemsontigers.com/sports/football/roster/", - missing high school
    "https://goduke.com/sports/football/roster",
    "https://seminoles.com/sports/football/roster/2023-24",
    "https://ramblinwreck.com/sports/m-footbl/roster/",
    "https://gocards.com/sports/football/roster",
    #"https://miamihurricanes.com/sports/football/roster/",
    "https://gopack.com/sports/football/roster",
    "https://goheels.com/sports/football/roster",
    "https://pittsburghpanthers.com/sports/football/roster",
    "https://cuse.com/sports/football/roster",
    #"https://virginiasports.com/sports/football/roster/",
    #"https://hokiesports.com/sports/football/roster",
    "https://godeacs.com/sports/football/roster",
    #"https://baylorbears.com/sports/football/roster",
    #"https://byucougars.com/sports/football/roster/",
    "https://gobearcats.com/sports/football/roster",
    "https://uhcougars.com/sports/football/roster",
    #"https://cyclones.com/sports/football/roster",
    #"https://kuathletics.com/sports/football/roster/",
    "https://www.kstatesports.com/sports/football/roster",
    "https://soonersports.com/sports/football/roster",
    "https://okstate.com/sports/football/roster",
    "https://gofrogs.com/sports/football/roster",
    "https://texassports.com/sports/football/roster",
    "https://texastech.com/sports/football/roster",
    #"https://ucfknights.com/sports/football/roster",
    "https://wvusports.com/sports/football/roster",
    "https://arizonawildcats.com/sports/football/roster",
    "https://thesundevils.com/sports/football/roster",
    "https://calbears.com/sports/football/roster",
    "https://cubuffs.com/sports/football/roster",
    "https://goducks.com/sports/football/roster",
    "https://osubeavers.com/sports/football/roster",
    "https://gostanford.com/sports/football/roster",
    "https://uclabruins.com/sports/football/roster",
    "https://usctrojans.com/sports/football/roster",
    "https://utahutes.com/sports/football/roster",
    "https://gohuskies.com/sports/football/roster",
    "https://wsucougars.com/sports/football/roster",
    "https://rolltide.com/sports/football/roster",
    #"https://arkansasrazorbacks.com/sport/m-footbl/roster/",
    "https://auburntigers.com/sports/football/roster",
    "https://floridagators.com/sports/football/roster",
    "https://georgiadogs.com/sports/football/roster",
    #"https://ukathletics.com/sports/football/roster/",
    "https://lsusports.net/sports/fb/roster/",
    "https://hailstate.com/sports/football/roster",
    "https://mutigers.com/sports/football/roster",
    "https://olemisssports.com/sports/football/roster",
    "https://gamecocksonline.com/sports/football/roster/",
    "https://utsports.com/sports/football/roster",
    "https://12thman.com/sports/football/roster",
    "https://vucommodores.com/sports/football/roster/"
]

# Create a single CSV file to store all the data
with open("football_roster.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    # Write the CSV headers
    writer.writerow(["School", "Name", "Position", "Class", "Hometown", "High School"])

    # Loop through the URLs
    for url in urls:
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors

            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract the school name from the <title> tag within the <head> section
            title_tag = soup.find("title")
            if title_tag:
                school_name = title_tag.text.strip()  # Extract the entire text of the title tag
            else:
                school_name = "Unknown"  # If title tag is not found, use "Unknown"
   
            # First pass: Maryland template
            player_details = soup.find_all("div", class_="s-person-details")

            if player_details:
                for player in player_details:
                    # Extract player information
                    name = player.find("div", class_="s-person-details__personal-single-line").find("span").text.strip()
                    position = player.find("span", class_="s-person-details__bio-stats-item").text.strip()
                    class_year = player.find_all("span", class_="s-person-details__bio-stats-item")[1].text.strip()

                    # Find player location details in the HTML:
                    location_info = player.find_next("div", class_="s-person-card__content__person-contact-info")
                    hometown = location_info.find_all("span", class_="s-person-card__content__person__location-item")[0].text.strip()
                    high_school = location_info.find_all("span", class_="s-person-card__content__person__location-item")[1].text.strip()

                    # Write the players' information to the CSV file:
                    writer.writerow([school_name, name, position, class_year, hometown, high_school])
            
            # Second pass: Alabama template:
            elif soup.find_all(class_='sidearm-roster-player-container'):
                player_containers = soup.find_all(class_="sidearm-roster-player-container")
            
                for player_container in player_containers:
                    position = player_container.find(class_="sidearm-roster-player-position").text.strip()
                    name = player_container.find(class_="sidearm-roster-player-name").text.strip()

                    # Remove extra information from position (height and weight)
                    position = position.split('\n')[0].strip()

                    # Remove extra information from name (jersey number)
                    name = name.split('\n')[-1].strip()

                    class_year = player_container.find(class_="sidearm-roster-player-academic-year").text.strip()
                    hometown = player_container.find(class_="sidearm-roster-player-hometown").text.strip()
                    high_school = player_container.find(class_="sidearm-roster-player-highschool").text.strip()
                
                    # Write the players' information to the CSV file:
                    writer.writerow([school_name, name, position, class_year, hometown, high_school])

            else:
                print(f"No player details found on the page ({url})")

        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            print(f"Failed to retrieve the web page ({url}). Status code:", response.status_code)
        except Exception as err:
            print(f"An error occurred while processing {url}: {err}")

# Read the additional CSV file
additional_csv_file = "other_football_rosters.csv"

# Append additional data to football_roster.csv
with open(additional_csv_file, mode="r", newline="", encoding="utf-8") as additional_csv:
    reader = csv.reader(additional_csv)
    next(reader)  # Skip the header

    with open("football_roster.csv", mode="a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        for row in reader:
            writer.writerow(row)