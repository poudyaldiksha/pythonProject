#load_digits dataset from sklearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits =load_digits()
X= digits.data
y= digits.target

def plot_digits(data):
    fig,ax = plt.subplots(4,10,
                         figsize=(10,4),
                         subplot_kw={'xticks':[],'yticks':[]},
                         gridspec_kw=dict(hspace=0.1,wspace=0.2)
                         )

    for i, ax in enumerate(ax.flat):
     ax.imshow(data[i].reshape(8,8),cmap='binary')

plot_digits(X)
plt.title("Original Dataset")
plt.show()













