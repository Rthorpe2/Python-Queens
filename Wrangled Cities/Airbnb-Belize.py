#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.cluster import KMeans
import seaborn as sns


# In[2]:


listings = pd.read_csv("C:/Users/ekaar/Downloads/listings (1).csv")


# In[3]:


listings.head()


# In[4]:


listings2 = listings[['neighbourhood','room_type', 'price', 'minimum_nights', 'number_of_reviews', 'number_of_reviews','availability_365']]


# In[5]:


listings2.head()


# In[8]:


def neighbourhood (series): 
    if series == "Belize Islands":
        return 0
    if series == "Stann Creek Mainland": 
        return 1


# In[9]:


listings2.head()


# In[ ]:




