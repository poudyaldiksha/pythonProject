import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime= pd.read_csv(url,parse_dates = ['Year'],index_col ='Year')#this is for tab separator
print(crime.head().to_string())#head will retrieve 5 items



print(crime.head().to_string())
print(crime.dtypes)
print(crime.index.dtype)


grouped = crime.resample('10YS').sum()
print(grouped.head(100).to_string())

print("====Most Dangerous Decade====")
most_dan_decade = grouped['Total'].idxmax()
print(grouped.loc[most_dan_decade])

terror = crime['Violent']
print(f'The number is days is {np.sum(terror > 100)}')



#Visualize time on app and yearly amount spent sns plot
sns.scatterplot(x='Time on Website',y='Yearly Amount Spent',data ='commerce',color='g')
plt.title('Yearly Amount Spent Vs Time on Website')
plt.xlabel('Time on Website')
plt.ylabel('Yearly Amount Spent')
plt.show()


# plot two columns using Seaborn
sns.lineplot(data=df[['Time on App', 'Yearly Amount Spent']])
plt.xlabel('Time on App')
plt.ylabel('Yearly Amount Spent')
plt.title('Yearly Amount Spent Vs Time on App')
plt.show()

#visualize session and yearly amount spent sns plot
sns. scatterplot(x='Avg. Session Length', y='Yearly Amount Spent')
plt.xlabel('Avg. Session Length')
plt.ylabel('Yearly Amount Spent')
plt.title('Yearly Amount Spent Vs Avg. Session Length')
plt.show()



