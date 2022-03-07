import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Obtain Data: 
df = pd.read_csv('https://raw.githubusercontent.com/datasets/gdp/0be54c18d900edc37123f25b4eff014731c9e459/data/gdp.csv')

print(df)

# Slicing for Country Name, Year, and Value Columns 
df = df.rename(columns={'Country Name': 'country',
                        'Year' : 'year',
                        'Value': 'gdp'})

# Assignment
us = df[df.country == 'United States']
eu = df[df.country == 'European Union']
cn = df[df.country == 'China']

# Plot
plt.style.use('seaborn')
plt.title("Simon Chu's GDP Plot")
plt.xlabel('Year')
plt.ylabel('GDP')
plt.xlim(1960, 2020)
plt.plot(us.year, us.gdp / 1E9, '-', label = 'United States')
plt.plot(eu.year, eu.gdp / 1E9, '--', label = 'European Union')
plt.plot(cn.year, cn.gdp / 1E9, '-.', label = 'China')
plt.legend()
plt.show()
