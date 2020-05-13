
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')

dataset = pd.read_csv('C:\Users\Sreekar\Desktop\Linear_Regreesion_Salary_Data.csv')
print(dataset.describe())


# In[7]:


x = dataset['Salary'].values
y = dataset['YearsExperience'].values


# In[10]:


# Finding mean
mean_x = np.mean(x)
mean_y = np.mean(y)
#print(mean_x,mean_y)

n = len(x)

# Finding m(slope)
numer = 0
denom = 0
for i in range(n):
    numer += (x[i] - mean_x) * (y[i]- mean_y)
    denom += (x[i] - mean_x) ** 2 
m = numer/denom
c = mean_y - (m * mean_x)

print(m,c)


# In[19]:


# y predict

nm = 0
dm = 0

for i in range(n):
    y_pred = c + (m * x[i])
    #print(y_pred)
    nm += (y_pred - mean_y) ** 2
    dm += (y[i] - mean_y) ** 2
r2 = (nm/dm)
print(r2)
    

