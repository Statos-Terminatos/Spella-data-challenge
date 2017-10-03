from os import path
import json
import pathname as pn 
import pandas as pd 

with open(path.join(pn.DATA_PATH, 'cellartracker_user.json')) as f:
    user_objs = json.loads(f.read())
    f.close()

with open(path.join(pn.DATA_PATH, 'user_location_coordinates.json')) as f:
    loc_objs = json.loads(f.read())
    f.close()

print(loc_objs[0].values)

obj = user_objs[0]
new_obj = loc_objs[0]
user_id = obj.get("user")
if user_id == new_obj.get("user"):
    coordinates = new_obj.get("coordinates")

user_loc = []
for obj in user_objs:
    user_id = obj.get("user")
    for item in loc_objs: 
        if user_id == item.get("user"):
            coordinates = item.get("coordinates")
            obj["coordinates"] = coordinates 
    print(obj)
    user_loc.append(obj)

    file_to_write = open('trial.json', 'w')
    file_to_write.write(json.dumps(user_loc))
    file_to_write.close()