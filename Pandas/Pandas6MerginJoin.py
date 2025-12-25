import math
from operator import mul
import re
from tempfile import tempdir
from matplotlib.pyplot import bar
import pandas as pd
import numpy as np

# Merging 
# Joining
# Concatenating

students = pd.read_csv('Pandas\\students.csv')
courses = pd.read_csv('Pandas\\courses.csv')
nov = pd.read_csv('Pandas\\reg-month1.csv')
dec = pd.read_csv('Pandas\\reg-month2.csv')
matches = pd.read_csv('Pandas\\matches.csv')
delv = pd.read_csv('Pandas\\deliveries.csv')

# print(courses)
# print(students)
# print(nov)
# print(dec)
# print(matches)
# print(delv)




# Funtion 1
# concat


# pd.concat = this helps stacking two dataframe
# on top of each other

# print(pd.concat([nov,dec]))

# the problem with this is 
# that it is retaining index 
# so you do ignore idex 

regs = pd.concat([nov,dec],ignore_index=True)
# print(regs)


# multi = pd.concat([nov,dec],keys=['november','december'])
# this is a multiindex data frame

# we write this code to create diffrentiation 
# when the index doesent indicate another dataset

# print(multi)
# if i only want nov or dec

# print(multi.loc['november'])
# print(multi.loc['december'])

# if i want a particular row in vov
# print(multi.loc[('december',4)])

# right now we stacked the df verically 
# we can also stack them horizontally

# print(pd.concat([nov,dec],axis=1))


# Merge

# join = joins on the basis of a common column
# print(students)
# print(regs)

# inner join

# print(students.merge(regs,how='inner',on='student_id'))
# how asks for what kind on join
# on asks for on what column are you joining



# left join

# courses.merge(regs,how='left',on='course_id')


# right join
# temp_df = pd.DataFrame({
#     'student_id':[26,27,28],
#     'name':['Nitish','Ankit','Rahul'],
#     'partner':[28,26,17]
# })

# students = pd.concat([students,temp_df],ignore_index=True)

# print(students.tail())

# students.merge(regs,how='right',on='student_id')

# outer join (sare values irrespective of the fact they
#  exist in each other)

# print(students.merge(regs,how='outer',on='student_id').tail(10))



# print(students)
# print(regs)
# print(courses)

# 1. find total revenue generated

# print(courses.merge(regs,how='inner',on='course_id')['price'].sum())


# 2. find month by month revenue

# temp_df = pd.concat([nov,dec],keys=['nov','dec']).reset_index()
# print(temp_df.merge(courses,on='course_id').groupby('level_0')['price'].sum())


# 3. Print the registration table
# cols -> name -> course -> price

# print(students.merge(regs,on="student_id").merge(courses,on='course_id')[['name','course_name','price']])



# 4. Plot bar chart for revenue/course
import matplotlib.pyplot as plt
# regs.merge(courses,on='course_id').groupby('course_name')['price'].sum().plot(kind='bar')
# plt.show()



# 5. find students who enrolled in both the months

# common = np.intersect1d(nov['student_id'],dec['student_id'])
# print(common)
# print(students[students['student_id'].isin(common)])


# 6. find course that got no enrollment
# courses['course_id']
# regs['course_id']

# print(courses[~(courses['course_id'].isin(regs['course_id']))])
# or
# course_id_list = np.setdiff1d(courses['course_id'],regs['course_id'])
# print(courses[courses['course_id'].isin(course_id_list)])


# 7. find students who did not enroll into any courses

# print(students[~(students['student_id'].isin(regs['student_id']))])


# 8. Print student name -> partner name for all enrolled students
# self join

# students['partner_name']

# print(students.merge(students,how='inner',left_on='partner',right_on='student_id')[['name_x','name_y']])



# 9. find top 3 students who did most number enrollments

# print(regs.merge(students,on='student_id').groupby(['student_id','name'])['name'].count().sort_values(ascending=False).head(3))



# 10. find top 3 students who spent most amount of money on courses

# print(regs.merge(students,on='student_id').merge(courses,on='course_id').groupby(['student_id','name'])['price'].sum().sort_values(ascending=False).head(3))


# Alternate syntax for merge

# pd.merge(students,regs,how='inner',on='student_id')



# IPL Problems

# print(matches)
# print(delv)
# find top 3 studiums with highest sixes/match ratio

# totalsixes = delv.merge(matches,left_on='match_id',right_on='id').query('batsman_runs == 6').groupby(['venue']).size()
# totalmatches = matches['venue'].value_counts()
# ratio = (totalsixes/totalmatches).dropna().sort_values(ascending=False)
# print(ratio.head(3))

# or

# temp_df = delv.merge(matches,left_on='match_id',right_on='id')
# six_df = temp_df[temp_df['batsman_runs'] == 6]
# # stadium -> sixes
# num_sixes = six_df.groupby('venue')['venue'].count()
# num_matches = matches['venue'].value_counts()
# (num_sixes/num_matches).sort_values(ascending=False).head(10)



# find orange cap holder of all the seasons

# temp_df = delv.merge(matches,left_on='match_id',right_on='id').groupby(['season','batsman'])['batsman_runs'].sum()
# temp_df=temp_df.reset_index()
# print(temp_df.sort_values('batsman_runs',ascending=False).drop_duplicates('season',keep='first').sort_values('season'))



