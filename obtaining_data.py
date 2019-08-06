import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import correlation_functions as cf

#importing csv files containing movies and ratings with pandas as dataframes
Movies_Id= pd.read_csv("MovieLens/movies.csv")
User_Ratings= pd.read_csv("MovieLens/ratings.csv")
#pivoting the ratings frame in order to be able to group values and work with the data at hand
URatings_PD=pd.pivot_table(User_Ratings, values='rating', index='userId', columns='movieId', fill_value=0)
#Transposing the frame in order to properly convert it to dictionarie
a=URatings_PD.transpose()
#Creating new dictionaries (movie ids, user-movie and movie-user)
Dict_MID=Movies_Id.to_dict()
Dict_byUser=a.to_dict()
Dict_byMovies=URatings_PD.to_dict()

#creating function in case the user wants to see which users have similar taste
def Create_User_Recom(username):
    print("The Data Set has",len(Movies_Id), "movies and", len(User_Ratings), "reviews")
    print("This could take a few seconds...")
    #Searching for similar users by calling the function topMatches
    c=cf.topMatches(Dict_byUser,username)
    #printing default 5 similar usears
    print("\nSimilar Users to User", username, "\n")
    for i in range(len(c)):
        corr,usuario=c[i]
        print("User",usuario)

#creating function in case the user wants movie recommendations
def Create_Movie_Recom(username):
    print("The Data Set has",len(Movies_Id), "movies and", len(User_Ratings), "reviews")
    print("This could take a few seconds...")
    #Searching for recomended movies by calling the function getrecommendations
    k=cf.getRecommendations(Dict_byUser,username)
    #printing default 10 movie recommendations for the user
    print("\n10 Movie Recommendations For User", username,"\n")
    for i in range(10):
        corr,peli=k[i]
        #printing movie titles instead of the id
        for j in Dict_MID['movieId']:
            if Dict_MID['movieId'][j]==peli:
                print(Dict_MID['title'][j])
