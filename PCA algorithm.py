import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
rng = np.random.RandomState(seed=101)
X= rng.randn(2,200).T
print("Original Dataset")
#print(X)
print(X.shape)
####Dimension.reduction
#Reduces higher dimension data to lower dimension
#Higher feature count
#Low feature count
#but keeps the context same
#------------------------
#Colummn1 Column2  Columm3  Column4
#PCA ncomponents=2 changes the dimension or reduces the dimension
#NewColumn1 NewColumn2 Target
model = PCA(n_components=1)
model.fit(X)
newPca = model.transform(X)
print("New Data")
print(newPca.shape)
#Inversetranform gets original size dataset from PCA
Xtransformed = model.inverse_transform(newPca)
plt.scatter(X[:,0],X[:,1],alpha=0.4)
plt.scatter(Xtransformed[:,0],Xtransformed[:,1])
plt.show()








