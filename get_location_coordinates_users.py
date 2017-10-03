from geo import GetCoordinates
from os import path
import json
import pathname as pn 


with open(path.join(pn.DATA_PATH, 'cellartracker_user.json')) as f:
    objs = json.loads(f.read())
    f.close()

long_lat_user = []
for obj in objs:
    new_data = {}
    new_data["user"] = obj.get("user")
    location = obj.get("locale")
    print(new_data["user"], ":", location)
    if location is None:
        new_data["coordinates"] = {'lat':None, 'lng':None}
        print(new_data["coordinates"])
    else: 
        new_data["coordinates"] = GetCoordinates(location)
        print(new_data["coordinates"])
    long_lat_user.append(new_data)

file_to_write = open(path.join(pn.DATA_PATH, 'user_location_coordinates.json'), 'w')
file_to_write.write(json.dumps(long_lat_user))
file_to_write.close()