import googlemaps
from config import GEOCODING_API_KEY


class SerchLocal:
    def __init__(self, latitude: float, longitude: float):
        self.gmaps = googlemaps.Client(key=GEOCODING_API_KEY)
        
        self.latitude = latitude
        self.longitude = longitude
    
    
    def __str__(self) -> str:
        return f'{self.latitude}, {self.longitude}'
    
    
    def Serch(self):
        try:
            location = self.gmaps.reverse_geocode((self.latitude, self.longitude))
            first_result = location[0]
            
            return first_result.get('formatted_address', 'Address not found!')
        except:
            return 'Address not found!'