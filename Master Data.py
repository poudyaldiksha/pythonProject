import pandas as pd
import re
import numpy as np
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users= pd.read_csv(url,sep ='|')
print(users.head(10))


occupation = users['occupation']
print('Different Occupation', occupation.nunique())

valuesOfOccupation = occupation.value_counts()
print(valuesOfOccupation)

print("Summarize")

print(users.describe())

print(users.describe(include = 'all'))

print(occupation.describe())

print(np.mean(users['age']))

valueCountOfage= users['age'].value_counts()
print(valueCountOfage.tail(10))