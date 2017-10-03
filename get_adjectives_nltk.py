import json 
from os import path
import nltk 
import pathname as pn 

with open(path.join(pn.SRC_PATH, "all_reviews_sentiments.json")) as f:
    objs = json.loads(f.read())
    all_wines_adj = []
    for obj in objs:
        new_data = {}
        new_data["wine_id"] =obj.get("wine_id")
        comment = obj.get("text")
        tokens= nltk.word_tokenize(comment)
        tagged= nltk.pos_tag(tokens)
        adjectives = []
        for item in tagged:
            if item[1] == 'JJ':
                adjectives.append(item[0])  
        new_data["adj"] = adjectives   
        print("I am processing {}, {}".format(new_data["wine_id"], 3))
        all_wines_adj.append(new_data)

    file_to_write = open(path.join(pn.DATA_PATH,'wine_adjectives.json'), 'w')
    file_to_write.write(json.dumps(all_wines_adj))
    file_to_write.close()
    
