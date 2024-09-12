import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
sns.set_palette('bright')
traininData = pd.read_csv('training.csv')
print(traininData.head(10).to_string())

#Checking if the data is clean
#Check for null values
print(traininData.isnull().sum())
#Data contains no null values so we don't need to do anything
#Seperate data into feature and target set

x =np.array(traininData['height(cm)'])
y= np.array(traininData['weight(kg)'])

#Rough Visualization
sns.scatterplot(x=x, y=y)
plt.show()


#for scikit learn our data would be two dimensional
X2D = x[:,np.newaxis]
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(X2D,y)

#Model Analysis and interpretation
print(f'The slope is {model.coef_}')
print(f'The intercept is {model.intercept_}')
print(f"Starting from {model.intercept_} each 1 cm increase in height results in increase in weight by {model.coef_[0]}")


