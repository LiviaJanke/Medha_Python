#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:46:43 2026

@author: livia
"""

import pandas as pd

import numpy as np

#%%

series_1 = pd.Series([1,2,3,4])

list1 = [5,6,7,8]

series_2 = pd.Series(list1)

#%%

series_3 = pd.Series(list1, index = ['a' , 2 , 'c ', 4])

dict1 = dict(a = 1, b = 2, c = 3, d = 4)

#%%

dict2 = {'a': pd.Series([1,2]),
         'b' : [2, 3]}

df1 = pd.DataFrame(dict2)

# If making a data frame from a dictionary, each key must have more than one value

series_4 = pd.Series(dict1)

dict_4 = dict(a = series_1, b = series_2)

# can only make a Series from dict with one value per key, not a DataFrame

#%%

author = pd.Series(['Jitender', 'Purnima', 'Arpit', 'Jyoti'])
article = pd.Series([210, 211, 114, 178])

#%%

d = {'author': ['Jitender', 'Purnima', 'Arpit', 'Jyoti'], 'article': article}
df = pd.DataFrame(d)
print(df)

#%%

arr1 = np.arange(1, 21 , 1)

arr3 = np.reshape(arr1, ((4 , 5)))

#%%

df5 = pd.DataFrame(arr3)

#%%

arr2 = np.array([[1,2,3], [4,5,6]])

#%%

a = 10
b = 10 * 2 
a = b
a = 10
a %= 2
print(a)

#%%

columns = df1.columns
# To print the first column

print(df1[columns[0]])

# To turn a DataFrame 
arr_from_df = df.values

# To turn an array into a DataFrame:
df_from_arr = pd.DataFrame(arr_from_df)

#%%

df1.describe()

#%%

mm_df = pd.DataFrame([[1,2,3, 'agg', 'agg'], [4, 5, '8', 6, 7]])

print(mm_df.describe())

#%%

df_auto_index = pd.read_csv('automobile_data.csv')

df_automobiles = pd.read_csv('automobile_data.csv', index_col='index')

#%%

# Sort index from smallest to largest
df_auto_sorted = df_automobiles.sort_index()

# Sort columns in reverse alphabetical order
df_auto_sorted = df_automobiles.sort_index(axis = 1, ascending = bool(0))

#%%

result = df_automobiles.sort_values(by='length')

#%%

df_automobiles.loc[1:10,'wheel-base':'num-of-cylinders']
# References the label-based index

#%%

df_automobiles.iloc[2:,2:5]
# IIMPLICIT loc; position-based index, i.e. continuous increasing integer index

#%%

mileage_filter = df_automobiles['average-mileage'] >= 20

old_cars = df_automobiles.loc[df_automobiles['average-mileage'] >= 20]

print(old_cars)

# DataFrame = old_cars
# Column = 'average-mileage'


#%%

data_df = pd.read_csv('data.csv')

Empty_True = pd.isnull(data_df)

Empty_False = pd.notnull(data_df)

#%%

no_na_cols = data_df.dropna(axis = 'columns')

#%%

all_zeros = data_df.fillna('a')



#%%

# keys: name (tom, mike), age (20,25)
# entries 

peoples = dict(name = ['tom', 'mike'], age = [20,25])

#%%

df_people = pd.DataFrame(peoples)

dict_people = {'name': ['mike', 'tom'],'score': [68, 75]}

#%%

df_peep = pd.DataFrame(dict_people)
print(df_people)
print(df_peep)

#%%

pd.merge(df_peep, df_people, on = 'name')

#%%

df1 = pd.DataFrame(np.random.randn(3, 2), columns=['A', 'B'])
print(df1)

df2 = pd.DataFrame(np.random.randn(3, 2), columns=['A', 'B'])
print(df2)

combined_df = pd.concat([df1,df2])

combined_df.reset_index(inplace = True)

#%%

df = pd.read_csv('automobile_data.csv', index_col='index')

#%%

groupedby_body_style = df.groupby('body-style')

#%%

def show_groupby_obj_contents(obj):
    groups = {}
    for name, group in obj:
        print(name)
        print(group)
        df = pd.DataFrame(group)
        groups.update({name : df})
    return groups

#%%

# calling the func:
groupby_styleco = show_groupby_obj_contents(df.groupby('body-style',  'company'))

#%%
multigroup = df.groupby(['body-style', 'num-of-cylinders']).sum()

multigroup.to_csv('multigroup.csv')

multigroup.to_excel('multigroup.xlsx')

#%%

# To save an individual group:
convertibles = contents_groupby_style['convertible']



