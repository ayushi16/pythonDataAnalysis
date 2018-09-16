import numpy as np
import pandas as pd
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv("data/winequality-red.csv",sep=';')
display(np.round(data.describe()))


fig, axs = plt.subplots(ncols=1,figsize=(10,6))
sns.barplot(x='quality', y='volatile acidity', data=pd.read_csv("data/winequality-red.csv",sep=';'), ax=axs)
plt.title('quality VS volatile acidity')
plt.tight_layout()
plt.show()
plt.gcf().clear()







#ts = pd.plotting.scatter_matrix(data, alpha = 0.3, figsize = (40,40), diagonal = 'kde');
#pd.show()


#correlation = data.corr()
# display(correlation)
#plt.figure(figsize=(14, 12))
#heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")


#import plotly.plotly as py
#py.plot(heatmap,filename='heatmap',sharing='public')
