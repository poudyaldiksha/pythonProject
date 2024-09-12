from unittest.mock import inplace

# Step 1. Import the necessary libraries

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
import pandas as pd
import numpy as np
apple= pd.read_csv(url)
print(apple)#head will retrieve 5 items

# Step 5. Transform the Date column as a datetime type
print(apple.dtypes)
apple['Date'] = pd.to_datetime(apple['Date'])
print(apple.dtypes)

# Step 6. Set the date as the index
apple.set_index(apple['Date'],inplace = True)
print(apple.index)
# Step 4. Check out the type of the columns
print(f"Duplicate Dates :{apple['Date'].duplicated().sum()}")

# # Step 7. Are there any duplicate dates?

# # Step 8. Make the first entry the oldest date.
# Step 4. Check out the type of the columns
apple.sort_index(ascending =False, inplace = True)
print(apple.head().to_string())

# # Step 9. Get the last business day of each month

print("Business Days of Each Month")
lastBusinessDays= apple.resample('BME').mean()
print(lastBusinessDays)
# # Step 10. What is the difference in days between the first day and the oldest

firstData= apple.index.min()
lastData= apple.index.max()
difference = lastData- firstData
print(difference.days)

# # Step 11. How many months in the data we have?
months= apple.resample('ME').mean()
print(months)

