import plotly.plotly as py

import pandas as pd

df = pd.read_csv('data/winequality-red.csv', sep=';')
dfgood = df[df.quality>=6]
dfpoor = df[df.quality<6]
df.head(2)

fig = {
    'data': [
		{
  			'x': dfgood.density,
        	'y': dfgood.pH  
		},
        {
        	'x': dfgood.density, 
        	'y': dfgood.pH 
     	}
    ],
    'layout': {
        'xaxis': {'title': 'Alcohol Content', 'type': 'log'},
        'yaxis': {'title': "pH value"}
    }
}

py.plot(fig, filename='wine-scatter',sharing='public')


