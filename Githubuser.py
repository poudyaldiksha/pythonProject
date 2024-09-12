import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo= pd.read_csv(url,sep ='\t')#this is for tab separator
print(chipo.head())#head will retrieve 5 items


print("=====First5====")
print(chipo.head(5).to_string())#head will retrieve 5 items

print("=====Rows====") #task 5
numberOfRows = chipo.shape[0]
print(numberOfRows)

print("=====Column====") #task 6
numberOfRows = chipo.shape[1]
print(numberOfRows)

print("Grouping By!!") #Task 9
print(chipo.head(10).to_string)
itemGroup = chipo.groupby('item_name')
groupSum= itemGroup.sum()
mostOrderedList = groupSum.sort_values (['quantity'], ascending = False)
print(mostOrderedList.head().to_string())
print(mostOrderedList.iloc[0])

#Task10.For the most-ordered item, how many items were ordered?
print('Most Ordered Item Quantity')
print(mostOrderedList.iloc[0]['quantity'])

#Task11.What was the most ordered item in the choice_description column?
#Same process only change groupby column to choice description

#Task12.How many items were ordered in Total?
TotalItemOrdered = chipo['quantity'].sum()
print(chipo.dtypes)

#Task13 : Turn the item price into a float
print(chipo.dtypes)
print(chipo['item_price'].sample(10))
#chipo['item_price'] = pd.to_numeric(chipo['item_price'])
#print(chipo.dtypes)

#Task14 : Dataframe ma we used map in dataframe and apply in series but works the same
chipo['item_price'] = chipo['item_price'].apply(lambda x:x[1:])
print('After Map')
print(chipo['item_price'])
#Changing to numeric
chipo['item_price'] = pd.to_numeric(chipo['item_price'])
print(chipo.dtypes)

print(chipo.head(10).to_string())
#Task 15.How many different orders were made in the period?
orderMade= chipo['order_id'].value_counts()
totalOrder = orderMade.sum()
print(totalOrder)

#Task 16.What is the average revenue amount per order?
chipo['revenue'] = chipo['quantity']*chipo['item_price']
print(chipo.head().to_string())
groupedOrder = chipo.groupby(['order_id']).sum()
meanGroupOrder = np.mean(groupedOrder['revenue'])
print(meanGroupOrder)#Task 16.What is the average revenue amount per order?
chipo['revenue'] = chipo['quantity']*chipo['item_price']
print(chipo.head().to_string())
groupedOrder = chipo.groupby(['order_id']).sum()
meanGroupOrder = np.mean(groupedOrder['revenue'])
print(meanGroupOrder)

#Task 18 How many different Items are sold?
differentItem = chipo['item_name'].value_counts().sum()
print(differentItem)

#Task 19: How much was the revenue for the period in the dataset?
totalRevenue = (chipo['quantity']*chipo['item_price']).sum()
print(totalRevenue)

#Task20: How many item orders were made in the period?
orderMade= chipo['order_id'].value_counts()
totalOrder = orderMade.sum()
print(totalOrder)




