#!/usr/bin/env python
# coding: utf-8

# ---
# # Libraries

# In[3]:


import pandas as pd


# ---
# # Functions

# In[2]:


def Convert_ObjectOrFloat_ToInt(dataframe, column_name):
    '''
    This Function Return a dataframe and convert object or float column to Int
    ------------------------------
    Parameter(dataframe): Dataframe
    Parameter(column_name): Column name (string)
    ------------------------------
    '''
    
    if dataframe[column_name].dtype == 'O' or dataframe[column_name].dtype == 'float64':
            dataframe[column_name] = dataframe[column_name].astype(int)
    
    return dataframe


# ---

# In[ ]:




