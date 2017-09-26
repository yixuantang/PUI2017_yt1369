
# coding: utf-8

# In[1]:

from __future__ import print_function
from pandas import DataFrame
import pandas as pd
import pylab as pl
import os


# In[2]:


print (os.environ['DFDATA'])


# In[3]:

data = pd.read_csv('/projects/open/NYCOpenData/nycopendata/data/h9gi-nx95/1428430582/h9gi-nx95')
print (type(data))


# In[4]:

data.head(3)


# In[5]:

data.drop(data.columns[0:10], axis = 1, inplace = True)
data.drop(data.columns[2:], axis = 1, inplace = True)


# In[6]:

data.head(3)


# In[7]:


data.plot.scatter(x = 'NUMBER OF PERSONS INJURED', y = 'NUMBER OF PERSONS KILLED', title = 'Plot the Columns' )
pl.show()


# In[ ]:



