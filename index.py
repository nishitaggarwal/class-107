import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
Fmean = df.groupby("level")["attempt"].mean()
print(Fmean)

fig = px.scatter(df,x = "student_id",y ="level" ,color = "attempt")
fig.show()
