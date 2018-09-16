import plotly.plotly as py

import pandas as pd

df = pd.read_csv('data/winequality-red.csv', sep=';')
dfgood = df[df.quality>=6].head(20)
dfpoor = df[df.quality<6].head(20)
