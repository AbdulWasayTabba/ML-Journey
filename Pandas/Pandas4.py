# More Important Functions


# value_counts
# sort_values
# rank
# sort index
# set index
# rename index -> rename
# reset index
# unique & nunique
# isnull/notnull/hasnans
# dropna
# fillna
# drop_duplicates
# drop
# apply
# isin
# corr
# nlargest -> nsmallest
# insert
# copy

import numpy as np
import pandas as pd

# value_counts(series and dataframe)

# a = pd.Series([1,1,1,2,2,3])
# print(a.value_counts())


marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])
# print(marks)
# print(marks.value_counts())\


ipl = pd.read_csv('Pandas/ipl-matches.csv')

# find which player has won most potm -> in finals and qualifiers

# print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

# Toss  descision plot

# import matplotlib.pyplot as plt

# ipl['TossDecision'].value_counts().plot(kind='pie')
# plt.show()


# har team ne kitne matches khele hai

# print((ipl['Team1'].value_counts()+ipl['Team2'].value_counts()).sort_values(ascending=False))



# sort_values(series and dataframe) -> ascending -> na_position -> inplace -> multiple cols

# x = pd.Series([12,14,1,56,89])
# print(x)
# print(x.sort_values(ascending=False))

# data frame pe sort values

movie = pd.read_csv('Pandas/movies.csv')

# pehle single columns per on movie name

# print(movie.sort_values('title_x'))

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)
# ab students me missing values hai
# toh ispe sort kar ke kya hoye ga

# print(students.sort_values('name'))
# by default missing will go to bottom
# to change it wer can do this

# print(students.sort_values('name',na_position='first',ascending=False))

# inplace will sotre the result permanently

# print(students.sort_values('name',na_position='first',ascending=False,inplace = True))

# ab multiple column ke basis pe

# print(movie.sort_values(['year_of_release','title_x']))
# isme pehel year ke hisab se sort hoye ga
# then uske andar alphabetically hoye ga

# agar year ko ascending wise 
# and title ko descing wise then

# print(movie.sort_values(['year_of_release','title_x'],ascending=[True,False]))


batsman = pd.read_csv('Pandas/batsman_runs_ipl.csv')
# print(batsman)

# rank(series)

# ab mujhe sare batsman ka rank nikalna hai
# on the basis of runs made

# batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)
# print(batsman.sort_values('batting_rank'))


# sort_index(series and data frame)

marks1 = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series = pd.Series(marks1)
# print(marks_series.sort_index(ascending=False))


# dataframe ko sort kare ge

# print(movie.sort_index(ascending=False))


# set_index(dataframe) -> inplace

# print(batsman)

# if i want to make my batsman name as index
# because it i unique

# print(batsman.set_index('batter'))
# to make it permanent
# print(batsman.set_index('batter',inplace=True))


# reset_index(series + dataframe)-> drop parameter

# this is opposite of set index
# it make it go back to normal 

# to make it permanent we use inplace

# batsman.reset_index()
# print(batsman)

# how to replace existing index wothut lossing batsman

# batsman.set_index('batting_rank')
# this will losse the batter column
# so first we reset

# batsman.reset_index().set_index('batting_rank')


# series to dataframe using reset-index


# print(marks_series)
# print(marks_series.reset_index())
# print(type(marks_series.reset_index()))
# this converts it to a dataframe


# rename(datafram)-> index

# print(movie.set_index('title_x',inplace=True))
# print(movie.rename(columns={'imdb_id':'imdb','poster_path':'link'},inplace=True))

# to rename index

# print(movie.rename(index={'Uri: The Surgical Strike':'Uri'}))


# unique(series)

# temp = pd.Series([1,1,2,2,3,3,4,4,np.nan,5,5,np.nan])
# print(temp.unique())
# this will take out all the uniqiue values

# ipl me total seasons kitne hoye hai
# print(ipl['Season'].unique().size)


# nunique(series + dataframe)-> does not count nan -> drop na parameter

# print(ipl['Season'].nunique())


# isnull(series + dataframe)

# print(students['name'].isnull())
# get a bolean series

# dataframe
# print(students.isnull())

# not null(series + dataframe)
# opposite of isnull

# print(students['name'][students['name'].notnull()])

# dataframe
# print(students.notnull())

# hasnans(series)
# poore column me koi bhi missing hai ya nahi

# print(students['name'].hasnans)


# dropna(series + dataframe) -> how parameter -> works like or
# removes all the missing values

# series
# students['name'].dropna()

# dataframe

# print(students.dropna())
# kise bhi row me agar aik bhi missing
# value hai woh poore row koh hata de ga

# is se bohot sara data hat jata hai
# so we can chnage that 
# because in drop na there is a default
# parameter
# dropna('how'=any)

# print(students.dropna(how='all'))
# this means that if all the values in the 
# row are null only then it will remove that
# row 

# you can also specify column 
# wise e.g if there is nan at name only then remove

# print(students.dropna(subset=['name']))

# ab un rows jahan par name me missing ya phir college me

# print(students.dropna(subset=['name','college']))
# isse or lag raha name or college me

# fillna(series + dataframe)
# print(students['name'].fillna('unknown'))
# fill missing values in name with unknown
# print(students['name'].fillna('unknown').hasnans)
# false

# dataframe

# print(students.fillna(0))
# you can do this but this isnt a 
# good idea 
# you shuld fill column by column

# print(students['package'].fillna(students['package'].mean()))
# we are filling the missing values in package
# with there mean

# print(students['name'].fillna(method = 'ffill'))
# ffill = forward fill
# print(students['name'].fillna(method = 'bfill'))
#bfill = backward fill


# drop_duplicates(series + dataframe) -> works like and -> duplicated()

# print(marks)
# print(marks.duplicated().sum())
# this will tell how many duplicates there are

# drop_duplicates hels you remove the duplicates

# temp = pd.Series([1,1,1,2,3,3,4,4])
# print(temp.drop_duplicates())

# print(marks)
# print(marks.drop_duplicates())
# this will remove the dulpicated row
# there is a parameter
# keep which will decide to keep
# the first parameter or the last one
# print(marks.drop_duplicates(keep='last'))


# find the last match played by virat kohli in Delhi

# ipl['all_players'] = ipl['Team1Players']+ipl['Team2Players']
# print(ipl.head())
# def did_kholi_play(player_list):
#     return 'V Kohli' in player_list
# ipl['did_kohli_play'] = ipl['all_players'].apply(did_kholi_play)
# print(ipl)
# print(ipl[(ipl['City'] == 'Delhi')&(ipl['did_kohli_play'] == True)].drop_duplicates(subset=['City','did_kohli_play'],keep='first'))



# drop(series + dataframe)

# temp = pd.Series([10,2,3,16,45,78,10])
# print(temp.drop(index =[0,6]))

# print(students)

# print(students.drop(columns=['branch','cgpa']))


# print(students.drop(columns=['branch','cgpa'],inplace=True))
# print(students.drop(index=[0,8]))

# print(students.set_index(['name']).drop(index=['nitish','aditya']))


# apply(series + dataframe)

# temp = pd.Series([10,20,30,40,50])

# har value ka sigmid calculate karna hai
# def sigmoid(value):
#     return 1/1+np.exp(-value)
# print(temp.apply(sigmoid))

# data frame

# dataframe me rows ko bhej sakhte hai


points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)

# you have to make a new colum  called eucleadian distance
# by using 1st point and 2nd point

def euclidean(row):
    pt_A = row['1st point']
    pt_B = row['2nd point']

    return ((pt_A[0]-pt_B[0])**2 + (pt_A[1]-pt_B[1])**2)**0.5

points_df['distance']=points_df.apply(euclidean,axis = 1)
print(points_df)
# axis = 1 mean rows


