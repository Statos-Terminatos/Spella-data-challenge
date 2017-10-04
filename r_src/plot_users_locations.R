library(rworldmap)

user_loc<- fromJSON("user_location_coordinates.json", flatten=T)

newmap <- getMap(resolution = "low")
plot(newmap)
points(user_loc$coordinates.lng, user_loc$coordinates.lat, col = "red", cex = .3)


#wine_loc<- fromJSON("wine_id_location.json", flatten=T)
#plot(newmap)
#points(wine_loc$coordinates.lng, user_loc$coordinates.lat, col = "blue", cex = .3)

library(ggmap)
map <- get_map(location = 'world', zoom =1)

mapPoints <- ggmap(map) + 
  geom_point(aes(x = coordinates.lng, y = coordinates.lat),  data = user_loc, alpha = .5)

mapWorld <- borders("world", colour="gray50", fill="gray50") # create a layer of borders
mp <- ggplot() +   mapWorld + geom_point(aes(x = coordinates.lng, y = coordinates.lat),  data = user_loc, alpha = .5)
