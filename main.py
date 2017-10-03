import json
import apiclient

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from os import path
from misc import Extract_ID


DATA_PATH = "/Users/aliya/Documents/Spella - Data science test/data/"

# [START def_analyze]
def analyze(text):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    return score, magnitude
# [END def_analyze]

with open(path.join(DATA_PATH, "cellartracker_reviews.json")) as f:
    objs = json.loads(f.read())
    for obj in objs:
        user = obj.get("user")
        
        sentiment = analyze(obj.get("text"))
        
