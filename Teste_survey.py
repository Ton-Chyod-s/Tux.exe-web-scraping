import googlemaps 

gmaps = googlemaps.Client(key='AIzaSyA2cS5CMyuGcE6PFmMTvUWf8S8AwcVdFBM')
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((-27.75722428, -48.51074237))


for i in reverse_geocode_result[1]:
    print(i)
        