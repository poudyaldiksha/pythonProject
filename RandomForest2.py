import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits

digits = load_digits()
print(digits.keys())

x= digits['data']
y = digits['target']

fig = plt.figure(figsize=(6,6))
fig.subplots_adjust()
for i in range(64):
    ax = fig.add_subplot(8,8,i+1)
    ax.imshow(digits.images[i],cmap = plt.cm.binary)
    ax.text(0,7,str(digits.target[i]))
plt.show()



