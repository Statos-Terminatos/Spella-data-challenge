import nltk 

text =  "I like beautiful, smart and big dogs. My cat is red. How do I carry this thick book?"
tokens= nltk.word_tokenize(text)
tagged= nltk.pos_tag(tokens)
#print(tagged)

a = list()
for item in tagged:
#   print(item, "     part of speech:",  item[1])
    if item[1] == 'JJ':
        a.append(item[0])

print(a)
