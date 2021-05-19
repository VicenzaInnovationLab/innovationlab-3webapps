import os

from pathlib import Path

import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import pandas as pd
import plotly.express as px

from content import body


# apri il dataset
app_list = ["pvout", "viirs", "ghm"]
app_name = app_list[1]
bd = body[app_name]
csv_path = Path.cwd() / ".." / "data" / "output" / f"stats_{app_name}.csv"
df = pd.read_csv(csv_path, sep=",", na_filter=False, index_col=0)
df["median"] = df["median"].apply(pd.to_numeric)
df["std"] = df["std"].apply(pd.to_numeric)
df["pop"].replace(-1, np.NaN, inplace=True)

df_vi = df.loc[(df["cod_prov"] == 24)]
df_100k = df.loc[(df["pop"] >= 100000)]
df_reg = df.loc[(df["cod_com"].isin([
        42002,  # Ancona
        7003,   # Aosta
        72006,  # Bari
        37006,  # Bologna
        92009,  # Cagliari
        70006,  # Campobasso
        79023,  # Catanzaro
        48017,  # Firenze
        10025,  # Genova
        66049,  # L'Aquila
        15146,  # Milano
        63049,  # Napoli
        82053,  # Palermo
        54039,  # Perugia
        76063,  # Potenza
        58091,  # Roma
        1272,   # Torino
        22205,  # Trento
        32006,  # Trieste
        27042,  # Venezia
]))]

# web app
app = dash.Dash(name=__name__,
                title=bd["title"]
                )

pop_st = df["pop"].describe()  # statistiche descrittive per marker size

fig_vi = px.scatter(df_vi, title=app_name, x="median", y="std", color="pop",
                 hover_data=df_vi,
                 size=np.where(
                         df_vi["pop"].isna(),
                         1,
                         df_vi["pop"].apply(lambda x: x - (pop_st["mean"] / pop_st["std"])
                                         )
                 )
                 )

fig_100k = px.scatter(df_100k, title=app_name, x="median", y="std", color="pop",
                 hover_data=df_100k,
                 size=np.where(
                         df_100k["pop"].isna(),
                         1,
                         df_100k["pop"].apply(lambda x: x - (pop_st["mean"] / pop_st["std"])
                                         )
                 )
                 )

fig_reg = px.scatter(df_reg, title=app_name, x="median", y="std", color="pop",
                 hover_data=df_reg,
                 size=np.where(
                         df_reg["pop"].isna(),
                         1,
                         df_reg["pop"].apply(lambda x: x - (pop_st["mean"] / pop_st["std"])
                                         )
                 )
                 )

"""
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
"""
app.layout = html.Div([
        html.H1(bd["title"]),
        dcc.Markdown(bd["bando"]),
        dcc.Markdown("![Logos di creatori](assets/logos.png)"),
        dcc.Markdown(bd["intro"]),
        dcc.Markdown("## Comuni in provincia di Vicenza"),
        dcc.Markdown(bd["filler"]),
        dcc.Graph(figure=fig_vi),
        dcc.Markdown(bd["filler"]),
        dcc.Markdown("## Comuni italiani con più di 100000 abitanti"),
        dcc.Graph(figure=fig_100k),
        dcc.Markdown(bd["filler"]),
        dcc.Markdown("## Capoluoghi regionali"),
        dcc.Graph(figure=fig_reg),
        dcc.Markdown(bd["filler"]),
        dcc.Markdown("## Descrizione della metodica"),
        dcc.Markdown(bd["filler"]),
        dcc.Markdown(bd["icons"])
])

if __name__ == '__main__':
    app.run_server(debug=True)
