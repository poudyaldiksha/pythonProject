
import numpy as np
#Step 2.Import the dataset from this adddress
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
import pandas as pd
#Step 3.Assign it to a variable called drinks.
drinks = pd.read_csv(url)
print(drinks.head().to_string())#head will retrieve 5 items
#Step 4. Which continent drinks more beer on average?
##Group By
drinksGrouped = drinks.groupby('continent')
result = drinksGrouped['beer_servings'].mean()
sorted = result.sort_values()
print(sorted.index[-1])

#Step 5.For each continent print the statistics for wine consumption.
print(drinksGrouped['wine_servings'].describe())

#Step6: Print the mean alcohol consumption per continent for every column
print(drinksGrouped[['beer_servings','total_litres_of_pure_alcohol','wine_servings','spirit_servings']].mean().to_string())