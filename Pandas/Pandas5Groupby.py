
from email import errors
from itertools import count
import re
from tokenize import Ignore
import pandas as pd
import numpy as np

movies = pd.read_csv('Pandas\\imdb-top-1000.csv')
# print(movies)

# group by
# kisse column ke basis pe ap group form
# karte ho

# print(movies.shape)

# if i want to seperate all the genres

genres =movies.groupby('Genre')
# it will divide all the 
# stuff in genres into diffrent columns


# Applying builtin aggregation fuctions on groupby objects
# print(genres.sum())
# when doing this it will 
# be a dataframe
# the index will be genres now
# all the numerical columns
# will be summed
# in there groups
# jese drama wale genre me jo bhi imdb
# rating thee woh sum ho jaye ge



# print(movies.sort_values('IMDB_Rating',ascending=False))


# find the top 3 genres by total earning

# print(movies.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(3))
# or 
# print(movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3))
# both will get the same result 
# second one is faster


# Find the genre with highest avg imdb rating

# print(movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1))


# find director with most popularity

# print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1))



# find number of movies done by each actor

# print(movies.groupby('Star1')['Series_Title'].count())







# GroupBy Attributes and Methods
# find total number of groups -> len
# find items in each group -> size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique


# print(len(movies.groupby('Genre')))
# or
# print(movies['Genre'].nunique())


# har group ke andar kitne rows gaye hai

# print(movies.groupby('Genre').size())
# or
# print(movies['Genre'].value_counts())


# har group ka first and last item

# genres = movies.groupby('Genre')
# print(genres.first())#first movies
# print(genres.last())#last movies

# agar har group ke 7th movie dekhne

# print(genres.nth(6))


# getgroup()

# agar dekhna keh horor me kon kon se movies hai
# print(genres)
# genres = movies.groupby('Genre')
# print(genres.get_group('Horror'))
# or
# print(movies[movies['Genre'] == 'Fantasy'])

# print(genres.groups)
# yeh sare ke sare index postions
# batadeta


# print(genres.describe())
# har group keh har numerical column ke
# opper sare calculation karta min max
# mean std 25% 50% 75% etc 

# print(genres.sample())
# this will get me one random movie
# from each genre


# print(genres.nunique())


# agg method
# passing dict
# print(genres.agg(
#     {
#         'Runtime':'mean',
#         'IMDB_Rating':'mean',
#         'No_of_Votes':'sum',
#         'Gross':'sum',
#         'Metascore':'min'
#     }
# ))
# agar ap chaho toh ap aik
# sath multiple aggregate funtion laga sakhte ho


# print(genres.head())
# ab agar har colum ke opper
# min max aur avg
# passing list
# numeric_cols = movies.select_dtypes(include='number')
# print(numeric_cols.groupby(movies['Genre']).agg(['min','max','mean']))


# if we want to merge these two ways 

# Adding both the syntax
# print(genres.agg(
#     {
#         'Runtime':['min','mean'],
#         'IMDB_Rating':'mean',
#         'No_of_Votes':['sum','max'],
#         'Gross':'sum',
#         'Metascore':'min'
#     }
# )
# )



# looping on groups

# find the highest rated movie of each genre
# rows = []
# for group, data in genres:
#     rows.append(data[data['IMDB_Rating'] == data['IMDB_Rating'].max()])
# df = pd.concat(rows, ignore_index=True)
# print(df)



# generes will give group object snd data
# two things



# split (apply) combine
# apply -> builtin function

# genres.apply(min)


# Find number of movie starting with A FOR EACH GROUP

# def foo(group):
#     return group['Series_Title'].str.startswith('A').sum()
    
# print(genres.apply(foo))



# find ranking of each movie in the gorup according to IMDB score

# def rank_movie(group):
#     group['genre_rank'] = group['IMDB_Rating'].rank(ascending = False)
#     return group
# print(genres.apply(rank_movie))



# find normalized IMDB rating group wise

# def normal(group):
#     group['norm_rating']= (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
#     return group

# print(genres.apply(normal))



# groupby on multiple cols

duo = movies.groupby(['Director','Star1'])
# print(duo.size())

# getgroup

# print(duo.get_group(('Aamir Khan','Amole Gupte')))


# find the most earnign actor -> director combo

# print(duo['Gross'].sum().sort_values(ascending = False).head(1))



# find the best(in-terms of metascore(avg)) actor->genre combo

# print(movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1))


# agg on multiple groupby

# print(duo.agg({
#     'IMDB_Rating': ['min','max','mean'],
#     'Gross': ['min','max','mean']
# }))


ipl = pd.read_csv('Pandas\\deliveries.csv')
# print(ipl.head())

# find the top 10 batsman in terms of runs

# batsman = ipl.groupby('batsman')
# print(batsman['batsman_runs'].sum().sort_values(ascending=False).head(10))


# find the batsman with max no of sixes

# six = ipl[ipl['batsman_runs'] == 6]
# print(six.groupby('batsman')['batsman'].value_counts().sort_values(ascending=False).head(1))



# find batsman with most number of 4s and 5s in the last 5 overs

# lastovers = ipl[ipl['over']>15] 
# boundry = lastovers[(lastovers['batsman_runs'] == 4) | (lastovers['batsman_runs'] == 6)]
# print(boundry.groupby('batsman')['batsman'].value_counts().sort_values(ascending=False).head(1))


# find Kholi's record against all teams
# temp_df = ipl[ipl['batsman'] == 'V Kohli']

# temp_df.groupby('bowling_team')['batsman_runs'].sum().reset_index()




# temp_df = ipl[ipl['batsman'] == 'V Kohli']
# temp  = temp_df.groupby('bowling_team')
# result = temp.agg(
#     fours = ('batsman_runs', lambda x: (x == 4).sum()),
#     sixes = ('batsman_runs', lambda x: (x == 6).sum())
# )
# print(result.head())

# print(temp_df.groupby('bowling_team')['batsman_runs'].sum().reset_index())



# Create a function that can return the highest score of any batsman

# def maxscore(batsman_name,group):
#     temp = group[group['batsman'] == batsman_name]
#     temp1 = temp.groupby('match_id')['batsman_runs'].sum().max()
#     return temp1
# print(maxscore('CH Gayle',ipl))