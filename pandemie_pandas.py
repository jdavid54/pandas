#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[101]:

#df_w = pd.read_csv('Cases_country27.csv')
df_w = pd.read_csv('https://opendata.arcgis.com/datasets/bbb2e4f589ba40d692fab712ae37b9ac_2.csv')
df_w

df_US = pd.read_csv('COVID19_Cases_US.csv')
print(df_US)


# In[84]:


print(df_w.loc[0])


# In[85]:


fr = df_w[df_w['Country_Region']=='France']
print(fr)


# In[86]:


names = df_w['Country_Region']
print(names)


# In[87]:


df_w.info()


# In[88]:


update = list(df_w[df_w['Country_Region']=='France']['Last_Update'])[0]
print(update)


# In[89]:


day = update.split('T')[0]
print(day)


# In[90]:


time = update.split('T')[1].split('.')[0]
print(time)


# In[91]:


x = df_w['X']
y = df_w['Y']


# In[92]:


import matplotlib.pyplot as plt
plt.plot(x,y,'r.')
plt.show()

# In[93]:


df_w.plot.scatter(x='X',y='Y')
plt.show()

# In[94]:


deads = df_w['Deaths'].sum()
print(deads)


# In[95]:


confirmed = df_w['Confirmed'].sum()
print(confirmed)
#deads/confirmed


# In[96]:


print('{:1.2f}%'.format(deads/confirmed*100))


# In[97]:


df_w['Deaths'].plot()
plt.show()

# In[98]:


df_w['Confirmed'].plot()
plt.show()
# In[103]:

columns=['Country_Region','Confirmed','Deaths','Recovered']
max = df_w.loc[df_w['Deaths']>1000, columns]
print(max)

# In[ ]:
x=list(max['Country_Region'])
y=list(max['Confirmed'])
z=list(max['Deaths'])
w=list(max['Recovered'])

plt.bar(x,y,label='Confirmed')
plt.legend()
plt.show()

plt.bar(x,z, label='Deaths')
plt.legend()
plt.show()

plt.bar(x,z, label='Recovered')
plt.legend()
plt.show()