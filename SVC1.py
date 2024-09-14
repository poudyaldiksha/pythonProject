#Support Vector Classification

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets._samples_generator import make_blobs

feature,target = make_blobs(n_samples =50, centers =2, random_state =0, cluster_std=0.60)
print(feature)
print(target)
plt.scatter(feature[:,0],feature[:,1],c = target, s= 50, cmap = 'autumn')
plt.show()

xfit = np.linspace(-1,3.5)
plt.scatter(feature[:,0],feature[:,1],c=target,s=50,cmap = 'autumn')
plt.plot([0.6],[2.1],'x',color='green',markeredgewidth =2, markersize =10)

for slope,yIntercept in [(1,0.65),(0.5,1.6),(-0.2,2.9)]:
    y = slope * xfit +yIntercept
    plt.plot(xfit,y,'-k')
plt.xlim(-1,3.5)
plt.show()


