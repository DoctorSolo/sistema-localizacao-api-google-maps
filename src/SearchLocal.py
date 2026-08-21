import googlemaps
from googlemaps.exceptions import ApiError, TransportError
from config import GEOCODING_API_KEY


class SearchLocal:
    def __init__(self, latitude: float, longitude: float):
        self.gmaps = googlemaps.Client(key=GEOCODING_API_KEY)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        return f'{self.latitude}, {self.longitude}'

    def search_details(self) -> dict:
        """Retorna um dicionário apenas com as informações essenciais."""
        try:
            results = self.gmaps.reverse_geocode((self.latitude, self.longitude))
            if not results:
                return {"error": "Localização não encontrada"}

            first_result = results[0]
            
            # Estrutura limpa para guardar os dados essenciais
            details = {
                "formatted_address": first_result.get('formatted_address', ''),
                "street": "",
                "number": "",
                "neighborhood": "",
                "city": "",
                "state": "",
                "country": "",
                "postal_code": ""
            }

            # Mapeia os componentes do endereço retornados pelo Google
            for component in first_result.get('address_components', []):
                types = component.get('types', [])
                
                if 'route' in types:
                    details['street'] = component['long_name']
                elif 'street_number' in types:
                    details['number'] = component['long_name']
                elif 'sublocality' in types or 'sublocality_level_1' in types:
                    details['neighborhood'] = component['long_name']
                elif 'administrative_area_level_2' in types or 'locality' in types:
                    details['city'] = component['long_name']
                elif 'administrative_area_level_1' in types:
                    details['state'] = component['short_name']
                elif 'country' in types:
                    details['country'] = component['long_name']
                elif 'postal_code' in types:
                    details['postal_code'] = component['long_name']

            return details

        except (ApiError, TransportError, Exception) as e:
            return {"error": f"Falha na requisição: {str(e)}"}

    def search_summary(self) -> str:
        """Retorna apenas uma string resumida no formato: 'Rua, Número - Bairro, Cidade - Estado'"""
        details = self.search_details()
        if "error" in details:
            return "Address not found!"
        
        neighborhood = details.get('neighborhood', '')
        city = details.get('city', '')
        state = details.get('state', '')
        country = details.get('country', '')

        summary = ""
        if neighborhood:
            summary += f" - {neighborhood}"
        if city and state:
            summary += f", {city} - {state}, {country}"
            
        print(summary)
        return summary