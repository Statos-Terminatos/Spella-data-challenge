#install.packages("tm")  # for text mining
#install.packages("SnowballC") # for text stemming
#install.packages("wordcloud") # word-cloud generator 
#install.packages("RColorBrewer") # color palettes

library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

wine_adj <- fromJSON("wine_adjectives.json", flatten=T)

# dumping adjectives
wine_id<-unique(wine_adj$wine_id)


text1<-paste(unlist(wine_adj$adj), sep="", collapse=" ")
docs <- Corpus(VectorSource(text1))
inspect(docs)
toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))
docs <- tm_map(docs, toSpace, "/")
docs <- tm_map(docs, toSpace, "@")
docs <- tm_map(docs, toSpace, "\\|")
docs <- tm_map(docs, toSpace, "<U+2019>")
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, stemDocument)

dtm <- TermDocumentMatrix(docs)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 300)

set.seed(1234)
wordcloud(words = d$word, freq = d$freq, min.freq = 1,
          max.words=500, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(12, "Dark2"))




