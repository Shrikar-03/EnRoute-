from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import numpy as np

geolocator = Nominatim(user_agent="MyApp")


def haha(locations):
    cities = {}
    l = []
    for i in range(len(locations)):
        location = geolocator.geocode(locations[i])
        cities[locations[i]] = ((location.latitude, location.longitude))
        l.append({locations[i], location.latitude, location.longitude})

    print('\n\n')
    print(cities)
    print('\n\n')

    distances = np.zeros((len(locations), len(locations)))

    for i, city1 in enumerate(cities):
        for j, city2 in enumerate(cities):
            if i != j:
                coord1 = cities[city1]
                coord2 = cities[city2]
                distance = int(geodesic(coord1, coord2).kilometers)
                distances[i, j] = "{:.3f}".format(distance)[:3]

    return distances

def second_haha(locations):
    l = []
    cities = {}
    for i in range(len(locations)):
        location = geolocator.geocode(locations[i])
        cities[locations[i]] = {"latitude": location.latitude, "longitude": location.longitude}
        l.append(cities[locations[i]])
    return l
