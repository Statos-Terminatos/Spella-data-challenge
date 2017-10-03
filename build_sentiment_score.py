import json
from os import path
from misc import ExtractId
from google_language_processing import AnalyzeSentiment
import sys
import pathname as pn


DONE_IDS = set()

# Load last json work build_sentiment_score
with open(path.join(pn.DATA_PATH, 'all_reviews_sentiments.json')) as f:
    objs = json.loads(f.read())
    for obj in objs:
        print(obj)
        DONE_IDS.add(obj.get('wine_id'))
    f.close()

with open(path.join(pn.DATA_PATH, "cellartracker_reviews.json")) as f:
    objs = json.loads(f.read())
    all_reviews_sentiments = []
    for obj in objs:
        new_data = {}
        new_data["wine_id"] = ExtractId(obj.get("url"))
        new_data["url"] = obj.get("url")
        new_data["user"] = obj.get("user")
        new_data["username"] = obj.get("username")
        new_data["date"] = obj.get("date")
        new_data["text"] = obj.get("text")
        new_data["rating"] = obj.get("rating")
        score, magnitude, phrases, ln = AnalyzeSentiment(obj.get("text"))
        new_data["score"] = score
        new_data["magnitude"] = magnitude
        new_data["phrases"] = phrases
        new_data["language"] = ln
        all_reviews_sentiments.append(new_data)
        print("I am processing {} and it got the score of {}".format(new_data["wine_id"], str(score*magnitude)))
        
    file_to_write = open('all_reviews_sentiments.json', 'w')
    file_to_write.write(json.dumps(all_reviews_sentiments))
    file_to_write.close()
