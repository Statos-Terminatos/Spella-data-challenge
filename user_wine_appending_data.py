from os import path
import json
import pathname as pn 
import pandas as pd 
from misc import ExtractId
from misc import FindYear


with open(path.join(pn.DATA_PATH, 'cellartracker_user_wine.json')) as f:
    user_wine_data = json.loads(f.read())
    f.close()

with open(path.join(pn.DATA_PATH, 'user_data_complete.json')) as f:
    user_data = json.loads(f.read())
    f.close()

with open(path.join(pn.DATA_PATH, 'cellartracker_wine.json')) as f:
    wine_data = json.loads(f.read())
    f.close()

with open(path.join(pn.DATA_PATH, 'unique_location_coordinates.json')) as f:
    locations = json.loads(f.read())
    f.close()

keyWineConst = "http://www.cellartracker.com/wine.asp?iWine="

WineFlatStructure = {
    "user_id": "",
    "username" : "",
    "user_location": "",
    "user_location_lng": "",
    "user_location_lat": "",
    "wine_id": "",
    "wine_location": "",
    "wine_location_lng": "",
    "wine_location_lat": "",
    "wine_name": "",
    "wine_year": "",
    "friends":"",
    "purchased": "",
    "dream_wine": "",
}


# Transform the lists to dicts for a better lookup and search performance
def TransformStructure(attrIndexer, array):
    new_objects = {}
    for obj in array:
        attr_value = obj.get(attrIndexer)
        new_objects[attr_value] = obj
   
    return new_objects


# transform the structures
user_data = TransformStructure("user", user_data)
wine_data = TransformStructure("url", wine_data)

def GetObjectFromArrayWithAttribute(attr_name, attr_value, array):
    for obj in array:
        if obj.get(attr_name) == attr_value:
            return obj
        else:
            return None


all_data = []
for user_wine in user_wine_data:
    tmp = {}
    url = user_wine.get("wine_url")
    user_id = user_wine.get("user")

    # Get the user object
    user = user_data.get(user_id) #GetObjectFromArrayWithAttribute("user", user_id, user_data)
    if not user:
        print("Skipped user with id {}, it does not exist...".format(user_id))
        continue
    tmp["user_id"] = user_id
    tmp["username"] = user["username"]
    tmp["user_location"] = user["locale"]
    userCoor = user["coordinates"]

    if not userCoor:
        userCoor = dict(lng=None, lat=None)

    tmp["user_location_lng"] = userCoor["lng"]
    tmp["user_location_lat"] = userCoor["lat"]
    tmp["friends"] = user["friends"]
    tmp["dream_wine"] = user["dream_wine"]
    tmp["purchased"] = user["purchased"]
    tmp["fans"] = user["fans"]

    # Get the wine object
    wine = wine_data.get(url) #GetObjectFromArrayWithAttribute("url", url, wine_data)
    wine_id = ExtractId(url)
    print(wine)
    tmp["wine_id"] = wine_id
    tmp["wine_name"] = wine.get("name")
    tmp["wine_year"] = FindYear(tmp["wine_name"])
    locationName = wine.get("category")
    locationCoor = locations.get(locationName)
    if not locationCoor:
        locationCoor = dict(lng=None, lat=None)

    tmp["wine_location"] = locationName
    tmp["wine_location_lng"] = locationCoor["lng"]
    tmp["wine_location_lat"] = locationCoor["lat"]

    print("I am processing the wine_id/user_id: {}/{}".format(wine_id, user_id))    
    all_data.append(tmp)

f = open(path.join(pn.DATA_PATH, 'all_flat.json'), 'w')
f.write(json.dumps(all_data))
f.close()
