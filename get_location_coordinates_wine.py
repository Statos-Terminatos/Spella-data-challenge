from geo import GetCoordinates
from os import path
import json
import pathname as pn

with open(path.join(pn.DATA_PATH, 'wine_id_location.json')) as f:
    objs = json.loads(f.read())
    f.close()

long_lat = {}
keys = objs.keys()
for key in keys:
    location = objs.get(key)
    print(key, ":", location)

    if location == "":
        long_lat[key] = {'lat':None, 'lng':None}
        print(long_lat[key])
    else:
        locationCoordinates = GetCoordinates(location)
        print(locationCoordinates)
        if locationCoordinates:
            long_lat[key] = locationCoordinates

file_to_write = open(path.join(pn.DATA_PATH, 'wine_location_coordinates.json'), 'w')
file_to_write.write(json.dumps(long_lat))
file_to_write.close()