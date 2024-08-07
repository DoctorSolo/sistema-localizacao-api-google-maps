import googlemaps   # Biblioteca para a API do google maps
import webbrowser   # Esta biblioteca é usada para abrir a web

class Local:
    # Instancia nescessaria para acessar o projeto do Google Clound
    gmaps = googlemaps.Client(key='')
    
    
    def __init__(self, latitude:float, longitude:float):    # O construtor recebe os paremetros x(latitude) e y(longetude),
            self.latitude   = latitude                      # Os parametros já são definidos para converter qualquer
            self.longitude  = longitude                     # tipo para (float) para evitar erro
    
    
    def __str__(self) -> str:
         return f'{self.latitude}, {self.longitude}'
    
    
    # Esta função sera usada para retornar a localização do banco de dados
    def pesquisa(self):
        
        try:    # Caso a localização exista ele retorna todos os dados do local
            location = self.gmaps.reverse_geocode((self.latitude, self.longitude))
            primeiro_resultado = location[0]
            # Extrai informações essenciais
            address = primeiro_resultado.get('formatted_address', 'Endereço não encontrado')
            loc = primeiro_resultado.get('geometry', {}).get('location', {})
            return {
                "Endereço": address,
                "localização": loc
            }
        
        except:
            return 'A localização não existe'


    # Esta funcao é nescessaria para abrir a localização na web
    def mapa(self):
        url = f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
        webbrowser.open(url)