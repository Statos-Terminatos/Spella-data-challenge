from misc import ExtractId
import json
from os import path
import pathname as pn

review_counter = {}

with open(path.join(pn.DATA_PATH, "cellartracker_reviews.json")) as f:
    objs = json.loads(f.read())

    for obj in objs:
        id_temp = ExtractId(obj.get("url"))
        if not review_counter.get(id_temp, False):
            review_counter[id_temp] = 1
        else:
            review_counter[id_temp] = 1 + review_counter[id_temp]

    file_to_write = open(path.join(pn.DATA_PATH, 'id_review_counter.json'), 'w')
    file_to_write.write(json.dumps(review_counter))
    file_to_write.close()
    f.close()


