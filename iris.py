from pyexpat import features
from random import sample

import pandas as pd
iris_df = pd.read_csv('/Users/dikshapoudyal/Downloads/Iris.csv')
from sklearn.naive_bayes import GaussianNB
#1.Choose a class of model by importing the approprate estimator class from Scikitlearn.
#2.Choose model hyper parameters by instantiating this class with discard values.
model = GaussianNB()
#3.Arrange data into a features matrix and target vector following the discussion from before.
from sklearn.naive_bayes import GaussianNB
y= iris_df['Species']
X= iris_df.drop(columns=['Species'])--
#4.Fit the model to your data by calling the fit() method of the model instance.
#If supervised pass data and label model.fit(Feature.Target)
model.fit(X,y)
#5.Apply the model to new data:
#For supervised learning, often we predict labels for unknown data using the predict() method.
#the transform() or predict() method.
newData = pd.read_csv('/Users/dikshapoudyal/Downloads/newData.csv')
predictedData = model.predict(newData)
print(predictedData)

row sample
columns features

irisData ['PCA1'] = X20 [:,0]
         ['pcA2']        :,1

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
sns.set_palette('bright')

irisData = sns.load_dataset('iris')
print(irisData.head())
