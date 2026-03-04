import pandas as pd
import matplotlib.pyplot as plt

#load csv file into data frame
df = pd.read_csv('study_results.csv', delimiter=';')
print(df.head())

columns = ['Eingabegerät A','Eingabegerät B']

plt.figure(figsize= (12,8))
boxplot = df.boxplot(column=columns, showfliers=True)

plt.title('Boxplot')
plt.xlabel('Eingabegeräte')
plt.ylabel('Werte')
plt.xticks(ticks=[1, 2], labels=['Eingabegerät A', 'Eingabegerät B'])

plt.savefig('boxplot.png')
plt.show()