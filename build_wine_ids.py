from misc import ExtractId
import json
from os import path
from misc import FindYear
import pathname as pn

with open(path.join(pn.DATA_PATH, "cellartracker_wine.json")) as f:
    objs = json.loads(f.read())
    all_wines = []
    for obj in objs:
        new_data = {}
        new_data["wine_id"] = ExtractId(obj.get("url"))
        new_data["name"] = obj.get("name")
        new_data["wine_year"] = FindYear(obj.get("name"))
        new_data["region"] = obj.get("category")
        new_data["blend"] = obj.get("blend")
        all_wines.append(new_data)

    file_to_write = open('wine_id.json', 'w')
    file_to_write.write(json.dumps(all_wines))
    file_to_write.close()

