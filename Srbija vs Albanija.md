```python
import pandas as pd

df = pd.read_csv(r'C:\Users\bonum\Downloads\world_pop.csv')

countries = ['Serbia', 'Albania']

filtered_data = df.loc[df['country'].isin(countries)]

selected_columns = filtered_data.columns[2:]  # Прескакање прве две колоне (Unnamed: 0 и country)

result = filtered_data.loc[:, selected_columns]

print(result)
```

         year_1960  year_1961  year_1962  year_1963  year_1964  year_1965  \
    1    1608800.0  1659800.0  1711319.0  1762621.0  1814135.0  1864791.0   
    167  6608000.0  6655000.0  6696000.0  6732000.0  6765000.0  6794000.0   
    
         year_1966  year_1967  year_1968  year_1969  ...  year_2011  year_2012  \
    1    1914573.0  1965598.0  2022272.0  2081695.0  ...    2905195  2900401.0   
    167  6841000.0  6880000.0  6915000.0  6945000.0  ...    7234099  7199077.0   
    
         year_2013  year_2014  year_2015  year_2016  year_2017  year_2018  \
    1    2895092.0  2889104.0  2880703.0  2876101.0  2873457.0  2866376.0   
    167  7164132.0  7130576.0  7095383.0  7058322.0  7020858.0  6982604.0   
    
         year_2019  year_2020  
    1    2854191.0  2837743.0  
    167  6945235.0  6908224.0  
    
    [2 rows x 61 columns]
    


```python

```
