import numpy as np
billAmount = np.array([100,200,300,400,1000,230])#feature
tips = np.array ([23,10,22,31,32,33])#target
#Predict the tips amount for the following bill
billToPredict = np.array([2500,230])

#1 Import necessary model
from sklearn.linear_model import LinearRegression
#Instantiate the model using hyperparameter
model = LinearRegression(fit_intercept=True)
#changing the data into feature and target matrix
X= billAmount[:,np.newaxis]
y= np.array(tips)
#Fit the model
model.fit(X,y)
#Predict the model in new data
XPred = billToPredict[:,np.newaxis]
preditedTips = model.predict(XPred)
print(preditedTips)