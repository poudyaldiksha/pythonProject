from symbol import parameters

import numpy as np
import seaborn as sns
from PIL.GimpGradientFile import linear

dataSet = sns.load_dataset('iris')
X = dataSet.drop (columns = ['species'])
y= dataSet ['species']

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(X,y,random_state=12,train_size=0.7)

#SVC
from sklearn.svm import LinearSVC
model = LinearSVC()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(ytest, ypred)
print(f'The accuracy is {accuracy}')

##Using scalar
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
XtrainScaled = scaler.fit_transform(xtrain.astype(np.float32))
XtestScaled = scaler.fit_transform(xtest.astype(np.float32))

model.fit(XtrainScaled,ytrain)
ypred2 = model.predict(XtestScaled)
accuracy2 = accuracy_score(ytest,ypred2)
print(f'The accuracy after scaling is {accuracy2}')

from sklearn.svm import SVC
model = SVC(kernel = 'linear',C =0.2)
model.fit(xtrain,ytrain)
ypred2 = model.predict(xtest)
accuracy2 = accuracy_score(ytest,ypred2)
print(f'The accuracy after radial is {accuracy2}')

from sklearn.model_selection import GridSearchCV
parameters = {'gamma':[0,1,10,0.0001],'C':[0,1,2,3,4],'kernel':['linear','rbf','poly']}
gridSearch = GridSearchCV(model,param_grid =parameters,cv =10)
gridSearch.fit(xtrain,ytrain)

print(f'The best parameter is {gridSearch.best_params_}')
print(f'The best score is {gridSearch.best_score_}')
print(f'The best estimator is {gridSearch.best_estimator_}')

bestModel = gridSearch.best_estimator_
bestModel.fit(xtrain,ytrain)
ypred3 = bestModel.predict(xtest)
print(f'The accuracy is {accuracy_score(ypred3,ytest)}')

