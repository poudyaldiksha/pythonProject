import numpy as np
import  pandas as pd

dataFrame = pd.read_csv('BuildingPermits,txt',low_memory=False)
#Check data Columns
print(dataFrame.columns)
#Check first 5 values
print(dataFrame.head(8).to_string())
#check last 5 values
print(dataFrame.tail(5).to_string())
#Rnaodm 5 values
print(dataFrame.sample(5).to_string())
#DataTypes Information ( Column name, no of non null values , dataype)
#DataTypes Information ( Column name, no of non null values , dataype)
print(dataFrame.info())
print("Missing Data Per Column")
missingDataPerColumn = np.sum(dataFrame.isnull())
print(missingDataPerColumn)
print("Total Missing Data")
totalMissingData = np.sum(missingDataPerColumn)
print("On the basis of columns")
requiredColumns = missingDataPerColumn[['Street Number Suffix','Zipcode']]
print(requiredColumns)
numberOfRows = dataFrame.shape[0]
print(numberOfRows)
print(f'Percentage of Street {(requiredColumns["Street Number Suffix"]/numberOfRows)*100}')

print(f'Percentage of Street {(requiredColumns["Zipcode"]/numberOfRows)*100}')

