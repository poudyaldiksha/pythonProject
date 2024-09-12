import numpy as np
from sklearn.linear_model import LinearRegression

url = 'xAPI-Edu-Data.csv'
A = VisITedResources [:,np.newaxis]
B =raisedhands [:,np.newaxis]

model = LinearRegression(fit_intecept = True)
model.fit(X,y)

model2 = LinearRegression(fit_intercept= True)
model2.fit(Z,y)
print(f'Slope of Visited Resources {model.coef_}')
print(f'Slope of Raisehands {model.coef_}')

print(f'Y intercept of Visited Resources {model.intercept_}')
print(f'Y Intercept of Raisehands {model2.intercept_}')

