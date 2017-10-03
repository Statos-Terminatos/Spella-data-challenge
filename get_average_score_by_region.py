import json
from os import path
from misc import ExtractId
import pathname as pn 

review_stat = {}
with open(path.join(pn.DATA_PATH, "all_reviews_sentiments.json")) as f:
    objs = json.loads(f.read())
    f.close()

for obj in objs:
    id_wine = obj.get("wine_id")
    if not review_stat.get(id_wine, False):
        stat_wine = {}
        stat_wine["score"] = obj.get("score")
        stat_wine["nb_reviews"] = 1
        review_stat[id_wine] = stat_wine
    else:
        review_stat[id_wine]["score"] = review_stat[id_wine]["score"] + obj.get("score")
        review_stat[id_wine]["nb_reviews"] = 1 + review_stat[id_wine]["nb_reviews"]

with open(path.join(pn.DATA_PATH, "cellartracker_wine.json")) as f:
    objs = json.loads(f.read())
    f.close()

id_location = {}
locations = set()
for obj in objs:
    wine_id = ExtractId(obj.get("url"))
    id_location[wine_id] = obj.get("category")
    locations.add(obj.get("category"))
    #print(wine_id, ':', obj.get("category"))
file_to_write = open(path.join(pn.DATA_PATH, 'wine_id_location.json'), 'w')
file_to_write.write(json.dumps(id_location))
file_to_write.close()

print(locations)
print(len(locations))

keys = review_stat.keys()
for key in keys:
    review_stat[key]["average_score"] = review_stat[key].get("score")/review_stat[key].get("nb_reviews")
    print(id_location.get(key))
    review_stat[key]["location"] = id_location.get(key)

print(len(id_location.keys()))
print(len(review_stat.keys()))

file_to_write = open(path.join(pn.DATA_PATH, 'id_review_counter.json'), 'w')
file_to_write.write(json.dumps(review_stat))
file_to_write.close()

