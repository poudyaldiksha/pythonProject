import pandas as pd
import re
import numpy as np


dataFrame= pd.read_csv('/Users/dikshapoudyal/Downloads/BookData.csv')
print("Shape")
print(dataFrame.shape)

print("Column Info")
print(dataFrame.columns)

ColumnsToDrop = ['Edition Statement', 'Contributors','Corporate Author', 'Corporate Contributors','Shelfmarks','Former owner', 'Engraver','Issuance type']
print("After Dropping")
dataFrame.drop(columns= ColumnsToDrop,inplace =True)
print(dataFrame.sample().to_string())

#change index to identifier
print(dataFrame['Identifier'].is_unique)
#Check if identifier has duplicate

#Check if identifier has duplicate
print("Checking Duplicate")
dataFrame.set_index('Identifier', inplace=True)


print(dataFrame.head(10).to_string())

print(dataFrame.loc[206])

#Checking the datatype of data
print('Checking data type')
print(dataFrame.dtypes)

#Checking a sample elmenent
print('Checking a sample element')
print(dataFrame.loc[206])
print('Checking a Date of Publication')
print(dataFrame['Date of Publication'].sample(20))

##Using regex to extract date only
print('Checking satisfied Date')
regex = re.compile(r'^(\d{4})')
satisfiedDate = dataFrame['Date of Publication'].str.extract(regex,expand= False)
print(satisfiedDate)

#Replace the data column with this new column
print('Replace the data column with this new column')
dataFrame['Date of Publication'] = pd.to_numeric(satisfiedDate)
print(dataFrame.dtypes)
print(dataFrame.sample(10).to_string())

print('Checking Another column place of publication')
publication = dataFrame['Place of Publication']
print(publication.head(15)) #different anamolies

print(dataFrame.loc[4157862])
print(dataFrame.loc[4159587])

print('Checking london')
london = publication.str.contains('London')
print(london.head(15)) #boolean masking

london = publication.str.contains('London')
oxford = publication.str.contains('Oxford')

print('Numpy Conditional')
##conditional Statement of Numpy
#np.where(cond,statement if true,statement if false)
dataFrame['Place of Publication']= np.where(london,'london', np.where(oxford,'Oxford',publication.str.replace('-','')))
print(dataFrame['Place of Publication'].head(20))

print('sample')
print(dataFrame['Place of Publication'].sample(20))

