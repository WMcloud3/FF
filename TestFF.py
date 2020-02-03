import numpy as np
import pandas as pd

filename = 'scripting exercise.csv'
df = pd.read_csv(filename)
print(df)

print(df[['Name','FavoriteFridge1']])

print(df[df['Name'] == 'Jill'])

print(df[df['Name'] == 'Candice'])

print(df[df['Name'] == 'Alycia'])


# write to csv file
#df.to_csv('FILE B')