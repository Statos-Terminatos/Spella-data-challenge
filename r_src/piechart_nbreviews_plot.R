library(rjson)

sentiment<-fromJSON(file="/Users/aliya/Documents/Spella - Data science test/src/all_reviews_sentiments.json")
wa
library(jsonlite)
data <- rjson::fromJSON(file="/Users/aliya/Documents/Spella - Data science test/src/all_reviews_sentiments.json")

sentiment_data<-data.frame(matrix(nrow = length(sentiment), ncol = 4))
colnames(sentiment_data) <- c("wine_id", "user_id", "score", "magnitude")
for (i in 1:length(sentiment)){
  wine_id<-sentiment[[i]]$wine_id    
  user_id<-sentiment[[i]]$user
  score<-sentiment[[i]]$score
  magnitude<-sentiment[[i]]$score
  sentiment_data[i,]<-cbind(wine_id,user_id, score, magnitude)
}

library(cluster)
library(fpc)
library(dplyr)

sentiment_data$score<-as.numeric(sentiment_data$score)
sentiment_data$magnitude<-as.numeric(sentiment_data$magnitude)

sentiment_data<-sentiment_data %>% 
  add_count(wine_id)

  
sentiment_aggregated<-aggregate(sentiment_data[, 3:4], list(sentiment_data$wine_id), mean)
sentiment_aggregated$n<-aggregate(sentiment_data[, 5], list(sentiment_data$wine_id), unique)$n


library(plotly)

p <- sentiment_aggregated %>%
  plot_ly(labels = ~Group.1, values = ~n) %>%
  add_pie() %>%
  layout(title = "Number of Comments per wine",  showlegend = F,
         xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
         yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE))

