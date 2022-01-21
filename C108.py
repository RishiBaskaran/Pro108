import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("C108.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Mobile Brand"], show_hist = False)
fig.show()
