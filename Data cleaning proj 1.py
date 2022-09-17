# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 18:41:56 2022

@author: Muqeet
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
# helpful modules
import fuzzywuzzy
from fuzzywuzzy import process
import chardet
proff=pd.read_csv("pakistan_intellectual_capital.csv")


np.random.seed(0)

proff.head()

proff.shape

#get all unique countries 

countries=proff['Country'].unique()
#%%
countries.sort()

#convert to lower case

proff['Country']=proff['Country'].str.lower()

#%%

#remove trailing white spaces 

proff['Country']=proff['Country'].str.strip()
proff['Country']

#%%
#using fuzzywuzzy to see how strings that are closer to others 
#for example So "apple" and "snapple" are two changes away from each other (add "s" and "n") while "in" and "on" and one change away (rplace "i" with "o")
matches=fuzzywuzzy.process.extract("south Korea",countries, limit=10,scorer=fuzzywuzzy.fuzz.token_sort_ratio)

matches


#%%

#writing a function to change all the corelated strings like "south Korea" and "southkorea"

def replac(df, column, string_to_match, min_ratio = 47):
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("All done!")
#%%

replac(df=proff, column='Country', string_to_match='south Korea')

countries=proff['Country'].unique()
countries.sort()
countries

#%%
for gettingcol in proff.columns:
    print(gettingcol)

#%%
for gettingrow in proff.index:
    print(gettingrow)

#%%
name=proff['Teacher Name']
depart=proff['Department']

fig, ax=plt.subplots()
ax.scatter(name,depart, color='green')
fig.show()

#%%
year=proff['Year']

plt.style.use('seaborn')

fig,az=plt.subplots()
az.hist(year)
fig.show()

az.set_xlabel("year")
az.set_ylabel("data")
az.set_title("our graph")

#%%


#%%
#%%
#%%
#%%
