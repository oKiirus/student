import csv
import pandas as pd
import plotly.express as px


df = pd.read_csv('ice.csv')
student = df.loc[df['id'] == 'TRL_abc']
end = student.groupby('level')['attempt'].mean()
print(end)

graph = px.bar(student, x = end, y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'])

graph.show()