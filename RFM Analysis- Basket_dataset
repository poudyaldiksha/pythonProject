#Distribution analysis / Value Counts and Graphs
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Loading the dataset
data = pd.read_csv("/Users/dikshapoudyal/Downloads/basket_dataset.csv")

#Generating Quick Insights
#Columns
print(data.columns)

#Checking Null Values
print(data.isna().sum())

#Checking more info
print(data.info())

#Stastical Exploration
#Since data only contain one numerical value member_number and such value
#Cannot give proper insights it is no much imp
print(data.describe(include = 'all').to_string())

#Distribution Analysis
item_counts = data ['itemDescription'].value_counts().sort_values(ascending=False)
print(item_counts.head().to_string())

#Top 5 item
print("Top 5 Selling items\n")
print(item_counts.head(5).to_string())

#Least 5 Selling items
print("Top 5 Selling Items\n")
print(item_counts.head(5).to_string())

#Checking Data Types of all columns to check if any transformation is required
print(data.dtypes)

data['Date'] = pd.to_datetime(data['Date'],dayfirst = True)
print(data.info())
print(data.head().to_string())

#Removing Duplicates
duplicates = data.duplicated()
print(duplicates)
print("Number of Duplicates")
print(duplicates.sum())

print("Number of Duplicates- Another way")
duplicates = data.duplicated()
print(duplicates.sum())
#Since in this data there are not much information, for example there is no quantity and #timestamp
print("After Removing Duplicates")
print(duplicates.sum())
# Since in this data there are not much information, for example there is no quantity and #time stamp for date so we donot know exactly if two transaction are from same time
#Or different time , hence we are considering it as duplicates
print("After Removing Duplication")
data.drop_duplicates(inplace=True)
print(data.duplicated().sum())

#Visualization
plt.figure(figsize=(10,6))
sns.countplot(x= 'itemDescription',data = data, order= data['itemDescription'].value_counts().index)
plt.title('Item Description Count lot')
plt.show()

#Plotting Value Counts Item Desccription
data['itemDescription'].value_counts().sort_values(ascending=False).head(5).plot(kind='pie')
plt.title('Top 5 item Sold')
plt.xlabel('Item')
plt.ylabel('')
plt.tight_layout()
plt.show()

#Plotting Value Counts Item Descriptiom
data['itemDescription'].value_counts().sort_values(ascending=False).tail(5).plot(kind='pie')
plt.title('Least 5 item Sold')
plt.xlabel('Item')
plt.ylabel('')
plt.tight_layout()
plt.show()

























