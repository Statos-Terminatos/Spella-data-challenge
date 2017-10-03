import googlemaps
import json


def GetCoordinates(location):
    gmaps = googlemaps.Client(key='AIzaSyCh8yvlYldMn1lRAgICOfs5gJus9b3-Yiw')
    geocode_result = gmaps.geocode(location)
    if (geocode_result):
        return geocode_result[0]['geometry']['location']
    else:
        return None

