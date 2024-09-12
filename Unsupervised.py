import pandas as pd


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
sns.set_palette('pastel')


irisData = sns.load_dataset('iris')
print(irisData.head())
y = irisData['species']
X = irisData.drop(columns = ['species'])


##PCA
from sklearn.decomposition import PCA
model = PCA (n_components=2)
model.fit(X)
X2D = model.transform(X)


print(X2D)


irisData['PCA1'] = X2D[:,0]
irisData['PCA2'] = X2D[:,1]


print(irisData.sample(10).to_string())


#Clustering Alogoithm
from sklearn.mixture import GaussianMixture
model = GaussianMixture(n_components =2)
model.fit(X)
predictedCluster = model.predict(X)

irisData['cluster'] = predictedCluster
print(irisData.sample(20).head().to_string())

sns.lmplot(data = irisData,x='PCA1',y='PCA2',hue = 'species',col = 'cluster',fit_reg = False)
plt.show()


model.fit(xtrain,ytrain)
predicted = model.predict(xtest)
accuracy = accuracy_score(ytest,predicted)
print(f'The accuracy score is {accuracy*100}')