from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="bansil-test")
location = geolocator.geocode("Abbeville, SC", "Aberdeen, NJ")
print(location)