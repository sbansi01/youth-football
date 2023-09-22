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
    #"https://gophersports.com/sports/football/roster",
    #"https://huskers.com/sports/football/roster",
    "https://nusports.com/sports/football/roster",
    #"https://ohiostatebuckeyes.com/sports/football/roster",
    #"https://gopsusports.com/sports/football/roster?view=2",
    "https://purduesports.com/sports/football/roster",
    "https://scarletknights.com/sports/football/roster",
    "https://uwbadgers.com/sports/football/roster",
    "https://bceagles.com/sports/football/roster",
    "https://clemsontigers.com/sports/football/roster/",
    "https://goduke.com/sports/football/roster",
    #"https://seminoles.com/sports/football/roster/2023-24",
    #"https://ramblinwreck.com/sports/m-footbl/roster/",
    #"https://gocards.com/sports/football/roster",
    #"https://miamihurricanes.com/sports/football/roster/",
    #"https://gopack.com/sports/football/roster",
    "https://goheels.com/sports/football/roster",
    "https://pittsburghpanthers.com/sports/football/roster",
    "https://cuse.com/sports/football/roster",
    #"https://virginiasports.com/sports/football/roster/",
    #"https://hokiesports.com/sports/football/roster",
    #"https://godeacs.com/sports/football/roster",
    #"https://baylorbears.com/sports/football/roster",
    #"https://byucougars.com/sports/football/roster/",
    "https://gobearcats.com/sports/football/roster",
    #"https://uhcougars.com/sports/football/roster",
    #"https://cyclones.com/sports/football/roster",
    #"https://kuathletics.com/sports/football/roster/",
    #"https://www.kstatesports.com/sports/football/roster",
    "https://soonersports.com/sports/football/roster",
    "https://okstate.com/sports/football/roster",
    #"https://gofrogs.com/sports/football/roster",
    "https://texassports.com/sports/football/roster",
    "https://texastech.com/sports/football/roster",
    #"https://ucfknights.com/sports/football/roster",
    "https://wvusports.com/sports/football/roster",
    #"https://arizonawildcats.com/sports/football/roster",
    "https://thesundevils.com/sports/football/roster",
    "https://calbears.com/sports/football/roster",
    #"https://cubuffs.com/sports/football/roster",
    "https://goducks.com/sports/football/roster",
    "https://osubeavers.com/sports/football/roster",
    "https://gostanford.com/sports/football/roster",
    "https://uclabruins.com/sports/football/roster",
    #"https://usctrojans.com/sports/football/roster",
    #"https://utahutes.com/sports/football/roster",
    "https://gohuskies.com/sports/football/roster",
    #"https://wsucougars.com/sports/football/roster",
    "https://rolltide.com/sports/football/roster",
    #"https://arkansasrazorbacks.com/sport/m-footbl/roster/",
    #"https://auburntigers.com/sports/football/roster",
    #"https://floridagators.com/sports/football/roster",
    "https://georgiadogs.com/sports/football/roster",
    #"https://ukathletics.com/sports/football/roster/",
    #"https://lsusports.net/sports/fb/roster/",
    "https://hailstate.com/sports/football/roster",
    "https://mutigers.com/sports/football/roster",
    "https://olemisssports.com/sports/football/roster",
    #"https://gamecocksonline.com/sports/football/roster/",
    #"https://utsports.com/sports/football/roster",
    "https://12thman.com/sports/football/roster",
    #"https://vucommodores.com/sports/football/roster/"
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
                school_name = title_tag.text.strip()
                if school_name == "Vite App":
                    school_name = "Indiana"
            else:
                school_name = "Unknown" 
   
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

            # Third pass: The Clemson exception:
            elif "clemsontigers.com" in url:
                player_urls = ["https://clemsontigers.com/sports/football/roster/season/2023/antonio-williams/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/barrett-carter/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/andrew-mukuba/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/will-shipley/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/nate-wiggins/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/cade-klubnik/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/noble-johnson/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/xavier-thomas/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/sherrod-covil-jr/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/josh-sapp/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/sheridan-jones/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/tyler-brown-wr/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/phil-mafah/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/justin-mascoll/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/tre-williams/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/adam-randall/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jake-briningstool/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/r-j-mickens/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/troy-stellato/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jeadyn-lukus/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/sage-ennis/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/peter-woods/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/paul-tyson/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/tj-parker/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/tyler-davis/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/brannon-spector/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/trent-pearman/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/shelton-lewis/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/ronan-hanafin/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jahiem-lawson/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/myles-oliver/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/colby-shaw/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/christopher-vizzina/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/wade-woodaz/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/hunter-helms/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/kylon-griffin/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/demonte-capehart/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/keith-adams-jr/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/domonique-thomas/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/avieon-terrell/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jarvis-green/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/kobe-mccloud/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/cole-turner/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/dee-crayton/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/peyton-streko/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/toriano-pride-jr/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/tyler-venables/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/hamp-greene/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jalyn-phillips/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/blackmon-huckabee-jr/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jay-haynes/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/misun-kelley/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/branden-strozier/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/davian-sullivan/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/kylen-webb/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/rob-billings/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/tristen-rigby/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jamal-anderson/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/wise-segars-jr/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/griffin-batt/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/ruke-orhorhoro/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/armon-mason/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/kevin-mcneal/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/austin-randall/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/joseph-flesch/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/quinn-castner/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/khalil-barnes/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jacob-hendricks/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/peter-nearn/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/robert-gunn-iii/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/aidan-swanson/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/bubba-mcatee/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/brodey-conn/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jonathan-weitz/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/caleb-nix/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/david-ojiegbe/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/riggs-faulkenberry/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/will-blackston/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/banks-pope/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/cade-denhoff/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/philip-florenzo/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/vic-burley/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jaden-kinard/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/hogan-morton/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/boston-miller/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/walt-smith/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/collin-sadler/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/fletcher-cothran/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jaden-murray/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/peyton-pitts/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/ryan-linthicum/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/ian-reed/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jeremiah-trotter-jr/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/payton-page/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/harris-sewell/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/will-putnam/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/reed-morrissey/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jackson-hall/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/chandler-mcmaster/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/holden-caspersen/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/evan-mccutchen/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/dietrick-pennington/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/bryce-smith/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/walker-parks/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/chapman-pendergrass/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/nathan-brooks/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/will-boggs/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/sam-judy/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/mason-johnstone/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/tristan-leigh/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/zack-owens/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/bryn-tucker/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/marcus-tate/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/trent-howard/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/john-williams/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/mitchell-mayes/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/blake-miller/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jake-norris/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/beaux-collins/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/olsen-patt-henry/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jackson-crosby/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/hampton-earle/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/markus-dixon/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/charlie-johnson/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/tristan-martinez/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/michael-mankaka/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/clay-swinney/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/zach-jackson/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jack-smith/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/stephiylan-green/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/zaire-patterson/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/levi-matthews/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/caden-story/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/jaheim-scott/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/patrick-swygert/",
                               "https://clemsontigers.com/sports/football/roster/season/2023/a-j-hoffler/"
                ]
                for player_url in player_urls:
                    try:
                        response = requests.get(player_url)
                        response.raise_for_status()

                        soup = BeautifulSoup(response.content, "html.parser")

                        player_name_with_number = soup.find("div", class_="profile__title").find("h1").string.strip()
                        player_name = player_name_with_number.split('\xa0')[1]
                        position = soup.find("div", class_="info__name", string="Position:").find_next("div", class_="info__value").string.strip()
                        class_year = soup.find("div", class_="info__name", string="Class:").find_next("div", class_="info__value").string.strip()
                        hometown = soup.find("div", class_="info__name", string="Hometown:").find_next("div", class_="info__value").string.strip()
                        high_school = soup.find("div", class_="info__name", string="High School:").find_next("div", class_="info__value").string.strip()

                        writer.writerow(["Clemson", player_name, position, class_year, hometown, high_school])
                    
                    except requests.exceptions.HTTPError as errh:
                        print(f"HTTP Error: {errh}")
                        print(f"Failed to retrieve the web page ({url}). Status code:", response.status_code)
                    except Exception as err:
                        print(f"An error occurred while processing {url}: {err}")

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