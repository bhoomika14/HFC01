#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")
import time
import pandas as pd
import validators
from urllib.parse import urlparse



# Sample data with date format 'Mon Day, Year'
data = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\#projects\Hackathon\cleaned_dataset2.csv")
print(data.head())


# In[2]:


# Convert data to DataFrame
df = pd.DataFrame(data)


# In[3]:


#Data types
print(df.dtypes)


# In[4]:


# Assuming 'df' is the DataFrame containing the dataset
#descriptive statistics for numerical columns
df.describe(include='all')


# In[5]:


### Data Cleaning
# Check for missing values
print(df.isnull().sum())


# In[6]:


df.dropna(inplace=True)
print(df.head())


# In[7]:


# Replace '(Healthcare, )' with 'Healthcare'
df['hacking_sub_type'] = df['hacking_sub_type'].str.replace('(Healthcare, )', 'Healthcare')

# Strip leading and trailing whitespace
df['hacking_sub_type'] = df['hacking_sub_type'].str.strip()


# In[8]:


### Data Validation
# Check for duplicates
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




