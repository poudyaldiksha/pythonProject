import numpy as np
import matplotlib.pyplot as plt

x = np.array ([1,2,3,4,5])
y = np.array ([4,2,1,3,7])

plt.scatter(x,y)
plt.title('Scatter Plot')
plt.show()

from sklearn.linear_model import LinearRegression
model = LinearRegression (fit_intercept = True)
X = x[:,np.newaxis]
model.fit(X,y)
ypred = model.predict(X)

plt.scatter(x,y)
plt.title('Scatter Plot')
plt.plot(x,ypred)
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=10)
X2= poly.fit_transform(X)
print(X2)

model.fit(X2,y)
ynew = model.predict(X2)
plt.scatter(x,y)
plt.title('Scatter Plot')
plt.plot(x,ynew)
plt.show()


#Pipeline
from sklearn.pipeline import make_pipeline
pipe = make_pipeline( PolynomialFeatures(degree=10),LinearRegression())
pipe.fit(X,y)
ynew2 = pipe.predict(X)