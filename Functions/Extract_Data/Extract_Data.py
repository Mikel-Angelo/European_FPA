#!/usr/bin/env python
# coding: utf-8

# ---
# # Libraries

# In[1]:


import pandas as pd
import requests 


# ---
# # Functions

# In[ ]:


def Extract_Data(url):
    '''
    This Function Return dataframe with European coutries of ΦΠΑ
    ------------------------------
    Parameter(url): Url from website where to Extract
    ------------------------------
    '''
    
    data = requests.get(url)
    
    name_of_site = data.url
    
    html_page = data.content
    dataframe = pd.read_html(html_page)
    dataframe = dataframe[0]

    dataframe.drop([dataframe.columns[1], dataframe.columns[2], dataframe.columns[3]], axis=1, inplace=True)

    for _ in range(len(dataframe.columns)):
        dataframe.rename(columns={dataframe.columns[_] : dataframe.iloc[0,_]}, inplace=True)
    
    return dataframe, name_of_site


# ---

# In[ ]:




