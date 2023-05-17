#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv(r'C:\Users\bonum\Downloads\world_pop.csv')

countries = ['Serbia', 'Albania']

filtered_data = df.loc[df['country'].isin(countries)]

selected_columns = filtered_data.columns[2:]  # Прескакање прве две колоне (Unnamed: 0 и country)

result = filtered_data.loc[:, selected_columns]

print(result)


# In[ ]:




