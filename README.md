File reviews contains information on the review of the wine from a client. 
It is an array of objects with the following attributes: 
  "url" 
  "user"
  "username"
  "date"
  "text"
  "rating"

File user_wine contains information on the id of client and what bottle of wine they have in the cave.
But the quantity is not available. We know that he has at least one bottle. It is an array of objects with the following attributes: 
  "user"
  "wine_url"

File user contains an array of objects with the following attributes: 
  "url": "http:\/\/www.cellartracker.com\/user.asp?iUserOverride=1",
  "user": "1",
  "username": "Eric",
  "info": "Locale: Seattle, Washington, USA",
  "fans": null,
  "purchased": null,
  "friends": null,
  "locale": "Seattle, Washington, USA",
  "dream_wine"

File Wine contains an array of objects with the following attributes: 
  "category" (Name of the region): "Napa Valley",
  "category2": null,
  "category3": null,
  "category4": null,
  "category5": null,
  "path": null,
  "path2": null,
  "path3": null,
  "path4": null,
  "path5": null,
  "url": "http:\/\/www.cellartracker.com\/wine.asp?iWine=1",
  "reviews": null,
  "blend": "",
  "name": "1997 Abreu Cabernet Sauvignon Madrona Ranch",
  "ct": null

authorization: 
export GOOGLE_APPLICATION_CREDENTIALS=/Users/aliya/Documents/Spella\ -\ Data\ science\ test/src/credentials.json

CREATED OUTPUT FILES: 
  File all_reviews_sentiments contains an array of objects with the following attributes: 
    "wine_id"
    "url"
    "user"
    "username"
    "date"
    "text"
    "rating"
    "score"
    "magnitude"
    "phrases"  is an array of objects that contains the attributes: 
        text": 
            "content"
            "begin_offset"
            "sentiment"
            "score"
            "magnitude"

Tutorial for word cloud generation: 
https://www.r-bloggers.com/text-mining-and-word-cloud-fundamentals-in-r-5-simple-steps-you-should-know/

