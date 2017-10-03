from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json
 
def AnalyzeSentiment(text):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()
 
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
 
    try:
        annotations = client.analyze_sentiment(document=document)
        phrases = []
        for _, sentence in enumerate(annotations.sentences):
            phrases.append({
                "text": {
                    "content": sentence.text.content,
                    "begin_offset": sentence.text.begin_offset
                },
                "sentiment": {
                    "score": sentence.sentiment.score,
                    "magnitude": sentence.sentiment.magnitude
                }
            })
 
            score = annotations.document_sentiment.score
            magnitude = annotations.document_sentiment.magnitude
            langue = annotations.language
        return score, magnitude, phrases, langue
    except:
        return 0,0,None,None
