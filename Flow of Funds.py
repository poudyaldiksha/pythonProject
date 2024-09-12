# Step 1. Import the necessary libraries
from unittest.mock import inplace

# Step 2. Import the dataset from this address.
url = 'https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv'
import pandas as pd
import numpy as np
myData = pd.read_csv(url)
print(myData.head().to_string())

# Step 3. Assign it to a variable called myData
# Step 4. What is the frequency of the dataset?
#Check if the data column in date timr format

print(myData.dtypes)
myData ['Date'] = pd.to_datetime(myData['Date'])
print(myData.dtypes)


#To find Frequency first sort the values in ascending order

myData.sort_values(['Date'],inplace=True)
print(myData.head(5).to_string())
#find the difference between first and second row after sorting

firstItem = myData['Date'].iloc[0]
secondItem= myData['Date'].iloc[1]
differenceInDate = secondItem - firstItem
print(f'frequency is {differenceInDate.days}')

# Step 5. Set the column Date as the index.
myData.set_index('Date',inplace= True)
print(myData.index)
print(myData.head())

# Step 8. Change the frequency to monthly, sum the values and assign it to monthly.

monthly = myData.resample('ME').sum()
print(monthly.sample(10).to_string())
# Step 9. You will notice that it filled the dataFrame with months that don't have any data with NaN. Let's drop these rows.
# Now change the frequency to year.
yearly = myData.resample('YS').sum()
print(yearly.head(10).to_string())

population = crime['Total'].resample('10YS').max()
print(Total)
print("======")

print("===Most Dangerous Decade====")
most_dan_decade= grouped['Total'].idxmax()
print(grouped.loc[most_dan_decade])