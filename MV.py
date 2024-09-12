import numpy as np
import seaborn as sns
from pandas.core.common import random_state

from PythonPracticefile import array

iris_data = sns.load_dataset ('iris')

X = iris_data.drop(columns = ['species'])
y = iris_data ['species']

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors =3)
model.fit(X,y)

ypred = model.predict(X)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y,ypred)
print(f'The accuracy score is {accuracy*100}')

print("After using holdout")
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(X,y,train_size =0.5,random_state= 120)
#X1 = Xtrain
#X2 = Xtest
#y1= yTrain
#y2= yTest

model.fit(xtrain,ytrain)
predicted = model.predict(xtest)
accuracy = accuracy_score(ytest,predicted)
print(f'The accuracy score is {accuracy*100}')

#Problem
print(f'The total data in dataset {iris_data.size}')
print(f'The data for training {xtrain.size}')
print(f'The percentage of data reduced {(iris_data.size-xtrain.size)/iris_data.size}')

#Cross Validation
from sklearn.model_selection import cross_val_score
cvScore = cross_val_score(estimator=model,X=X,y=y,cv=4)
print(cvScore)
print(np.mean(cvScore*100))
