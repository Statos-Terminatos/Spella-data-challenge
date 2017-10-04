#--------------------------------------------
#          Aliya Ussinova                   #
#   Analysis of Geographical trends         # 
#--------------------------------------------

# Load the libraries
library(dplyr) # the transformation of data
library(maps) # map polygon of world
library(ggplot2) # plot
library(wesanderson) # color palette
library(RColorBrewer) # color palette
library(ggplot2)
library(ggmap)
library(maps)
library(mapdata)
library(sp)
library(geosphere)
library(stringr)
# Main dataset 
user_wine <- fromJSON("all_flat.json", flatten=T)

# Subset the dataset on the location of users only for merge 
loc_user<- unique(data.frame(cbind(user_wine$user_location, user_wine$user_location_lng,
                                   user_wine$user_location_lat), stringsAsFactors = F))
colnames(loc_user)<-c("user_location","user_location_lng", "user_location_lat" )
loc_user$user_location_lng<-as.numeric(loc_user$user_location_lng)
loc_user$user_location_lat<-as.numeric(loc_user$user_location_lat)

# Subset the dataset on the location of wines only for merge 
loc_wine<- unique(data.frame(cbind(user_wine$wine_location, user_wine$wine_location_lng,
                                   user_wine$wine_location_lat)))
colnames(loc_wine)<-c("wine_location","wine_location_lng", "wine_location_lat" )

mapWorld<-map_data("world", boundary = TRUE, xlim=c(-300, 300)) %>% 
          filter(region != "Antarctica")

# Graph on the location of wineyards from the dataset
mp <- ggplot() + geom_polygon(aes(long, lat, group = paste(region, group)),
                              col="black",fill='white', data = mapWorld) +
                 geom_count(aes(x = as.numeric(as.character(wine_location_lng)), 
                           y = as.numeric(as.character(wine_location_lat)), color = ..n..),
                           data = loc_wine, alpha = .5)+
                 #coord_fixed() +
                 theme(axis.line=element_blank(),axis.text.x =element_blank(),
                                axis.text.y=element_blank(),axis.ticks=element_blank(),
                                axis.title.y=element_blank(),axis.title.x=element_blank(),
                                panel.background=element_blank(),panel.border=element_blank(), 
                                panel.grid.major=element_blank(),
                                panel.grid.minor=element_blank(),plot.background=element_blank()) + 
                 scale_colour_gradientn(colours= c("#A1D99B","#74C476","#41AB5D","#238B45","#005A32")) +
                 ggtitle("Régions viticoles dans le monde") + 
                 theme(plot.title = element_text(face="bold", hjust = 0.5)) +
                 theme(legend.direction = "horizontal", 
                      legend.position = "bottom",
                      legend.box = "horizontal") +scale_size(guide=FALSE) +
                 theme(legend.text=element_text(size=8))



# calculating the distance to determine the local
for (i in 1:nrow(user_wine)) {
  user_wine$distance[i]<-distm(c(user_wine$user_location_lng[i], user_wine$user_location_lat[i]),
           c(user_wine$wine_location_lng[i], user_wine$wine_location_lat[i]), 
           fun = distHaversine)/1000 # to convert to km
  print(i)
}

#:length(unique(user_wine$user_location))
for (i in 1:length(unique(user_wine$user_location))) {
    loc<-unique(user_wine$user_location)[i]
    temp_data<-user_wine[user_wine$user_location == loc & !is.na(user_wine$user_location),] 
    #ratio_local<- local_wines_count/nrow(user_wine)
    #themostfreqdest<-temp_data %>%
    #    group_by(wine_location) %>%
    #    summarise(freq = n())
    temp_data<-merge(x = temp_data, y = themostfreqdest, by = "wine_location", all.x = TRUE)
    destination_df<-temp_data[order(temp_data$freq, decreasing=T)[1:5],]
    destination_df<-temp_data[order(temp_data$freq, decreasing=T)[1:5],]
    main_wine_destinations<-
    temp_data_unique<-temp_data[!duplicated(temp_data[,c('user_id')]),]
    nb_users <- length(unique(temp_data$user_id))
    
    title = paste("Wine preferences of of users from", loc, sep = " ")
    #subtitle = paste("Ratio of local wines:",ratio_local, sep = " " )
    
    p<- ggplot() + geom_polygon(aes(long, lat, group = paste(region, group)),
                            col="black",fill='white', data = mapWorld) +
      geom_count(aes(x = as.numeric(as.character(wine_location_lng)), 
                 y = as.numeric(as.character(wine_location_lat)), color = ..n..),
             data = temp_data, alpha = .5) +
      geom_point(aes(x = as.numeric(as.character(user_location_lng)), 
                 y = as.numeric(as.character(user_location_lat))),color = "yellow", 
             data = temp_data_unique, alpha = .5, size = 2 )  +
      coord_fixed() +
      theme(axis.line=element_blank(),axis.text.x =element_blank(),
            axis.text.y=element_blank(),axis.ticks=element_blank(),
            axis.title.y=element_blank(),axis.title.x=element_blank(),
            panel.background=element_blank(),panel.border=element_blank(),panel.grid.major=element_blank(),
            panel.grid.minor=element_blank(),plot.background=element_blank()) + 
      scale_colour_gradientn(colours= c("#A1D99B","#74C476","#41AB5D","#238B45","#005A32"), name = "Number of users") +
      ggtitle(title) + 
      #labs(subtitle=subtitle)+
      theme(plot.title = element_text(size=12, face="bold", hjust = 0.5)) +
      theme(legend.direction = "horizontal", 
            legend.position = "bottom",
            legend.box = "horizontal") + scale_size(guide=FALSE) 
      #theme(plot.subtitle=element_text(size=10, hjust=0.5, face="italic", color="black"))
name<-str_replace_all(name, "[[:punct:]]", " ")

filename =  paste("users", name, ".pdf", sep = "")
#filename = paste("/Users/aliya/Documents/Spella - Data science test/output/","users", name, ".pdf", sep = "")
ggsave(filename = filename, device = "pdf", p , width = 8.5, height = 7, units = c("in"), scale = 1)
#unlink(filename)
}  
