from geo import GetCoordinates
from os import path
import json
import pathname as pn


with open(path.join(pn.DATA_PATH, 'wine_id_location.json')) as f:
    objs = json.loads(f.read())
    f.close()

locations = list(set(objs.values()))

long_lat = {}
for i in range(1,len(locations)):
    temp_name = locations[i]
    print(temp_name)
    locationCoordinates = GetCoordinates(temp_name)
    long_lat[temp_name] = locationCoordinates    

file_to_write = open(path.join(pn.DATA_PATH, 'unique_location_coordinates.json'), 'w')
file_to_write.write(json.dumps(long_lat))
file_to_write.close()