import pandas as pd
import csv
import plotly.express as go

df = pd.read_csv("dat.csv")
mean = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
print(df.groupby("level")["attempt"].mean())


fig = go.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")

fig.show()