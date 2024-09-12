import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Loading the dataset
titanicData = pd.read_csv('titanic.csv')

#Data Analyzation and Visualization
#Column Information, Data Type Information and A Sample of Data
print('Column Information')
print(titanicData.columns)
#We will use survived as target to predict if the passengers survived

#Using dtype information we find out which data are numeric for Sklearn we need to have all numeric data
#We might want to change categorical data to numeric as well
print('Data type Information')
print(titanicData.dtypes)

print('Checking a sample')
print(titanicData.sample(5).to_string())

#Data cleaning
#Remove null values
print(titanicData.shape[0])
print(titanicData.isnull().sum())
# Cannot Remove unnecessary rows because the total rows in 891 and in worst case null rows is 866
#Remove Cabin Column
titanicData.drop(columns =['Cabin','Age'],inplace=True)
print(titanicData.isnull().sum())
#Remove null values
#Dropping all NA values which in this case is embarked with 2 values
titanicData.dropna(inplace =True)
print(titanicData.isnull().sum())
#Remove unnecessary columns
#Check if passenger class is int or we can be used as categorical

#Quick Visualization
#main goal how different categorics variables affect the survived columns
#Count plot y axis has frequency so we give x axis only
sns.countplot(x='Survived',data= titanicData)
plt.title("Count Plot Of Survived")
plt.xlabel('Survived')
plt.ylabel('Count')
plt.legend(loc ='best')
plt.show()

#Remove unnecessary columns
#Check if passenger class is int or can be used as categorical

#Survived in reference to gender
sns.countplot(x='Survived',data= titanicData, hue ='Sex')
plt.title("Count Plot Of Survived Aganist Sex")
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

#Survived in reference to passenger class
sns.countplot(x='Survived',data= titanicData, hue ='Pclass')
plt.title("Count Plot Of Survived Aganist Pclass")
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

#Remove unnecessary columns
#Check if passenger class is int or can be used as categorical

print("Checking if the int value can be used as categorical")
#Even though pclass is on int datatype there are only three data so
#we use this  as categorical
print(titanicData['Pclass'].unique())
print(titanicData ['Sex'].unique())
print(titanicData ['Embarked'].unique())

#Changing to categorical variables
#we us pd.dummies to change categorical
sex = pd.get_dummies(titanicData['Sex'], drop_first = True)
print(sex)
#1 bhane male ho natra female

embarked = pd.get_dummies(titanicData['Embarked'], drop_first = True)
print(embarked)

pclass = pd.get_dummies(titanicData['Pclass'], drop_first = True)
print(pclass)

#join to original data frame
titanicdata = pd.concat