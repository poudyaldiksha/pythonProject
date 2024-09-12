from fontTools.varLib.plot import plotModelFromMasters
from seaborn import scatterplot

from TimeSeriesandanalysis import difference

url = 'Ecommerce.py'
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#Load the data
ecommerce = pd.read_csv(url)
df = pd.DataFrame(ecommerce)
#Check the head
print(ecommerce.head().to_string())#head will retrieve 5 items
#is null ,dtypes
#mean ,med ustai cha-- no difference
#get info
print(ecommerce.info())
#Describe the data
print(ecommerce.describe(include = 'all'))

#Visualize time on website and yearly amount spent

sns.scatterplot( x='Time on Website',y='Yearly Amount Spent',data ='commerce',color='g')
plt.title('Yearly Amount Spent Vs Time on Website')
plt.xlabel('Time on Website')
plt.ylabel('Yearly Amount Spent')
plt.show()



