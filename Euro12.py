
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
import pandas as pd
import numpy as np
euros = pd.read_csv(url)
print(euros.head().to_string())#head will retrieve 5 items
#Step 4. Which continent

# Step 3. Assign it to a variable called euro12.
# Step 4. Select only the Goal column.

goalColumn = euros['Goals']
print(goalColumn)

# Step 5. How many teams participated in the Euro2012?
numberOfTeams = euros['Team'].nunique()
print(f'Number of teams is {numberOfTeams}')

# Step 6. What is the number of columns in the dataset?
print(f'Number of columns {euros.shape[1]}')
# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

columnsToExtract = ['Team','Yellow Cards','Red Cards']
discipline = euros[columnsToExtract]
print(discipline.head())

# Step 8. Sort the teams by Red Cards, then to Yellow Cards

print('======Red Card and Yellow Card sorting======')
sorted =discipline.sort_values(['Red Cards', 'Yellow Cards'],ascending=False)
print(sorted)
# Step 9. Calculate the mean Yellow Cards given per Team

print('======Mean Yellow Card ======')

print(discipline.dtypes)
print('Over all Yellow Card')
print(np.mean(discipline['Yellow Cards']))
# Step 10. Filter teams that scored more than 6 goals

print('Filtered Team with Goals...')
filteredTeam = euros[euros['Goals']>6]
print(filteredTeam)

# Step 11. Select the teams that start with G

filteredTeam = euros[euros['Team'].str.startswith('G')]
print(filteredTeam)

# Step 12. Select the first 7 columns

print('First seven columns======')
print(euros.iloc[:,:7].to_string())
# Step 13. Select all columns except the last 3.

print(euros.iloc[:,:-3].to_string())
# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
selectedTeamAllColumns = euros[euros['Team'].isin(['England','Italy','Russia'])]
print(selectedTeamAllColumns['Shots on target'])