from geopy.geocoders import Nominatim

# Inicializar o objeto geocoder com o provedor geocodefarm
geolocator = Nominatim(user_agent="myGeocoder", geocodefarm_api_key='SUA_CHAVE_DO_IBGE')

# Definir as coordenadas
latitude = -48.38292204
longitude = -27.46079003

# Buscar o endereço
location = geolocator.reverse(f"{latitude}, {longitude}")

# Exibir o endereço
print(location.address)