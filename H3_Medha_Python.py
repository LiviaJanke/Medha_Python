#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:48:06 2026

@author: livia

Pandas for Datasets

"""

#  importing libraries

import pandas as pd
import numpy as np

# pwd = print working directory
# shows you the folder you are currently in
# Save your python file and your data files in the same folder to make access easier

#%%

# In-place functions 

list1 = [1,2,3,4,5]
print('Example list (list1):', list1)

print('Example of an "in place" function:')
print('list1.pop(2)')

print(".pop() removes the item at the given index from list1, "
      "changing the contents of the list1 variable in the process")

print(list1.pop(2))

print('Running the line above prints the removed value 3 (which is the third item in the list so is at index 2), '
'because the removed value is the only output of the function')

print("The function does not output a changed form of the variable (list1), "
      "instead changing the data stored in the original variable directly")

print('Assigning the output of the function to a new variable (pop_output)'
      ' will not prevent the original variable (list1) from being modified')


list1 = [1,2,3,4,5]
print('Original list (list1):', list1)

pop_output = list1.pop(2)
print('Contents of the variable "list1" after running the line above:', list1)

print('contents of the variable "pop_output":',pop_output)

#%%
# Non in-place functions

print('a NON in-place function outputs the changed form of the original variable, e.g.')


arr1 = np.ones((3,5))
print('Original array', arr1)

print('Ouput of np.delete() function:', np.delete(arr1, 1))

print('while the data contained by the original variable is unchanged:', arr1)

print('if the output of the function is not assigned to a new variable, it will not be stored anywhere; '
      'it is printed to the terminal but not accessible within the code')

arr1 = np.ones((3,5))
new_arr1 = np.delete(arr1, 1)
print(' After running the line above, the variable new_arr1 now contains the output of the np.delete() function.')
print('new_arr1:', new_arr1)


#%%


"""
Example: Load the automobile dataset and print the first 5 rows
Hint:
• Download the data file automobile_data.csv from https://yinglonghe.github.io/files/teaching/surrey-eng2124/automobile_data.csv
• Use Pandas read_csv() to load the automobile dataset.
• Use Pandas head() to return the first n rows.

Hints:
• Write your code between two comment lines: ### Start/End your code here ###.
• Expected output is shown at the end of each question (directly below the code cell).
"""
df = pd.read_csv('automobile_data.csv')

print('print  first 5 rows:')
print(df.head())

print('Print last 5 rows:')
print(df.tail())


# Using the given non-continuous index values as the index column:
    
df1 = pd.read_csv('automobile_data.csv', index_col='index')
print(df1.head())

# Print column names

print(df.columns)

#%%


"""
Q1: Drop the rows where at least one element is missing
Hint:
• Use Pandas dropna().
"""

df_some_stuff_missin = pd.read_csv('automobile_data_empty_cells.csv')
print(df_some_stuff_missin.tail())


df_less_stuff_missing = df_some_stuff_missin.dropna()
print(df_less_stuff_missing.tail())

#%%
"""
Q2: Print all details of Toyota cars
Hint:
• Use Pandas selection method.
"""

companies = df['company']

toyotas = df.loc[df['company']=='toyota']

print(toyotas)


#%%

"""
Q3: Find the most expensive car’s company name
• Print most expensive car’s company name and price.
"""

most_expensive_row = df.loc[df['price']==df['price'].max()]

most_expensive_row = most_expensive_row.reset_index(drop=True)

print('company:', most_expensive_row['company'][0])

print('price:', most_expensive_row['price'][0])


#%%

"""
Q4: Count total cars per company
Hint:
• Use Pandas value_counts().
"""

df_counts = df['company'].value_counts()
print(df_counts)

#%%

"""
Q5: Find each company’s Highest price car
"""

grouped_df_object = df.groupby('company')

df_max_prices = grouped_df_object['price'].max()

#Or can do in one line:
    
df_max_prices = df.groupby('company')['price'].max()

print(df_max_prices)

#%%

# Looking at Groupby further 
# More examples:

groupedby_body_style = df.groupby('body-style')

print('head')
print(groupedby_body_style.head())

print('groups')
print(groupedby_body_style.groups)

print('indices')
print(groupedby_body_style.indices)

# GroupBy docs: 
# https://pandas.pydata.org/docs/reference/groupby.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

# User Guide: https://pandas.pydata.org/docs/dev/user_guide/groupby.html#transformation

# API docs: https://pandas.pydata.org/docs/reference/groupby.html

# Guide to software library APIs: https://libereurope.github.io/ds-topic-guides/api.html

#%%

# Descriptor string does not show the actual contents of the object
# But .head() or .tail() let you see something? Unsure how that output is related to the object
# lazy devs.............

# Using a for loop to view contents of groupby object:

for name, group in groupedby_body_style:
    print(name)
    print(group)
    print()

#%%
# As a function:

def show_groupby_obj_contents(obj):
    for name, group in obj:
        print(name)
        print(group)
        print()
#    return

# calling the func:
show_groupby_obj_contents(groupedby_body_style)

#%%

# new func to save output in visible manner:
    
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
contents_groupby_style = show_groupby_obj_contents(groupedby_body_style)

# All seems to work fine

# To save an individual group:
    
convertibles = contents_groupby_style['convertible']

#%%

"""
Q6: Find the average mileage of each car making company
"""



"""
Q7: Sort all cars by Price column in descending order
Hint:
• Use Pandas sort_values().
• Print the first 5 rows of the sorted Dataframe.
"""


"""
Q8: Concatenate two Dataframes and reset the index of the combined
Dataframe
Hint:
• Use Pandas concat() and its ignore_index option.
"""



"""
Q9: Merge two data frames using the following condition
• Create two DataFrames using the following two Dictionarys.
• Merge two DataFrames on the Company column.
"""

























