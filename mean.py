import csv
import pandas as pd
import plotly.express as px


df = pd.read_csv('ice.csv')
end = df.groupby('level')['attempt'].mean()
print(end)

graph = px.bar(df, x = end, y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'])

graph.show()