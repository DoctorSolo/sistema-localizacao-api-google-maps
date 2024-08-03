from geopy.geocoders import Nominatim
import googlemaps


gmaps = googlemaps.Client(key='')

# Use aqui para pegar a cordenada
local = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
first_result = local[0]

location = first_result['geometry']['location']
latitude = location['lat']
longitude = location['lng']

print(latitude, longitude)