import pandas as pd
import plotly.express as pe

ppy = pd.read_csv("project.csv")

pro = pe.scatter(ppy, x = "date", y = "cases", color = "country")

pro.show()









