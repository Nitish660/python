#!/usr/bin/env python
# coding: utf-8

# In[1]:


# let us import the Pandas Library
import pandas as pd


# In[2]:


#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df


# In[3]:


#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x


# In[4]:


type(x)


# In[5]:


#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
z


# In[ ]:




