import seaborn as sns
sns.set_style('whitegrid')
import numpy as np

#Simple function to generate a data
def makeData(N):
        rng = np.random.RandomState(seed =123)
        #Creating two dimensional data because skit take nfeatures,nsample for X which is 2 dimensional
        X = rng.rand(N,1)**2
        y=10-1.0/(X.ravel()+0.1)
        return X,y

#Calling a function makedata that returns X and Y setting them into variable
XTrain,yTrain = makeData(100)

#Creating a simple linearspaced data and giving it a new axis
xtest = np.linspace(-0.1,1.1,500)[:,np.newaxis]

#Importing necessary modules
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def myPolynomialRegression(degree=2)
    pipe = make_pipeline(PolynomialFeatures(degree),LinearRegression)(fit_intercept = True))
    return pipe





