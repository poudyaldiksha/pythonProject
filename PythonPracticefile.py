import  pandas  as pd
import numpy as np
from numpy.f2py.crackfortran import myeval

x= pd.Series([1,2,3,4,np.nan,np.nan,7,9])

array=np.array(x)
print(np.nanmin(array))
print(np.nanmax(array))

#Check if there is null values
print(x.isnull())
#How many null values
print(np.sum(x.isnull()))

#Checking inverse that is not null

print(x.notnull())

#checking count of nonull values
print(np.sum(x.notnull()))

print("----------Dropping Null Values")
dropped = x.dropna()
print("Original")
print(x)
print("After Drop")
print(dropped)

print("Drop na with inplace")
#Drop na inplace = true changes orginal without returning
#x.dropna(inplace=True)
print("Original")
print(x)


#filing Values
print("====Filling Values")
z =x.fillna(98)
print(z)

print("Fill NA with in place")
x.fillna(88,inplace=True)
print(x)

## IN Dataframe

myDataFrame= pd.DataFrame([[1,np.nan,2],[2,3,5],[np.nan,4,6]])
print(myDataFrame)

print("Drop")
myDataFrame.dropna(inplace=True,axis ='columns')
print(myDataFrame)

myDataFrame[3]=np.nan
print(myDataFrame)

print("-----")
ac= myDataFrame.dropna(axis = 'columns', how = 'all')
print(ac)
print("-----Any")
ad = myDataFrame.dropna(axis = 'columns', how = 'any')
print(ad)
print("-----Thres")
ae = myDataFrame.dropna(axis = 'rows', thresh = 3)
print(ae)
ae = myDataFrame.dropna(axis = 'rows', thresh = 2)
print(ae)