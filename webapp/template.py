from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px

# apri il dataset
app_list = ["pvout", "viirs", "ghm"]
app_name = app_list[0]
csv_path = Path.cwd() / ".." / "data" / "output" / f"stats_{app_name}.csv"
df = pd.read_csv(csv_path, sep=",", na_filter=False, index_col=0)
df["median"] = df["median"].apply(pd.to_numeric)
df["std"] = df["std"].apply(pd.to_numeric)
df["pop"].replace(-1, np.NaN, inplace=True)

# web app
pop_st = df["pop"].describe()  # statistiche descrittive per marker size

fig = px.scatter(df, title=app_name, x="median", y="std", color="median",
                 hover_data=df,
                 size=np.where(
                         df["pop"].isna(),
                         1,
                         df["pop"].apply(lambda x: x - (pop_st["mean"] / pop_st["std"])
                                         )
                 )
                 )

"""
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
"""
fig.show()
