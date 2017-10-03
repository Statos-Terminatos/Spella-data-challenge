import googlemaps
import json
import os


def GetCoordinates(location):
    key = os.environ.get('DEV_KEY_MAPS')
    if not key:
        return None
    gmaps = googlemaps.Client(key=key)
    geocode_result = gmaps.geocode(location)
    if (geocode_result):
        return geocode_result[0]['geometry']['location']
    else:
        return None
