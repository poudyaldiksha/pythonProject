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
xtrain, xtest, ytrain, ytest = train_test_split(X,y,train_size =0.5,random_state= 120)
#X1 = Xtrain
#X2 = Xtest
#y1= yTrain
#y2= yTest
print("X1")
print(x1)
print("X2")
print(x2)
