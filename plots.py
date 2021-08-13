import pandas as pd
import plotly.express as px
df = pd.read_csv("Covid.csv")

fig = px.line(df, x = "date", y = "cases", color = "country")
fig.show()
fig = px.bar(df, x = "date", y = "cases", color = "country")
fig.show()
fig = px.scatter(df, x = "date", y = "cases", color = "country")
fig.show()