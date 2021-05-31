from pathlib import Path

import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import pandas as pd


from content import *
from istat_codes import *
from functions import pop_size, make_graph, colors

####################
# PARAMETRI INIZIALI
####################
app_list = ["viirs", "ghm", "pvout"]
app_name = app_list[0]
if app_name == "viirs":
    fa_icon = "fa fa-moon-o"
elif app_name == "pvout":
    fa_icon = "fa fa-solar-panel"
elif app_name == "ghm":
    fa_icon = "fa fa-globe-europe"

####################
# IMPLEMENTAZIONE
####################

# Aprire il dataset e fare pre-elaborazione
bd = body[app_name]
csv_path = Path.cwd() / ".." / "data" / "output" / f"stats_{app_name}.csv"
df = pd.read_csv(csv_path, sep=",", na_filter=False, index_col=0)
df["median"] = df["median"].apply(pd.to_numeric)
df["std"] = df["std"].apply(pd.to_numeric)
df["pop"].replace(-1, np.NaN, inplace=True)
df["m_size"] = pop_size(df)  # marker size for visualization

# Separare il dataset in livello provinciale, regionale, ecc.

# Provincia VI
df_vi = df.loc[(df["cod_prov"] == istat_prov_vi)].copy()
df_vi["is_labeled"] = np.where(df_vi["cod_com"].isin(istat_5com), True, False)

# Comuni italiani > 100k abitanti
df_100k = df.loc[(df["pop"] >= 100000)].copy()
df_100k["is_labeled"] = np.where(df_100k["cod_com"] == istat_vicenza, True, False)

# Capoluoghi regionali
df_reg = df.loc[(df["cod_com"].isin(istat_capoluoghi))].copy()
df_reg["is_labeled"] = np.where(df_reg["cod_com"] == istat_venezia, True, False)

#########
# WEB APP
#########

# Google Fonts
ext_scripts = [{"src": "https://kit.fontawesome.com/798fa6dddc.js",
                "crossorigin": "anonymous"}]
ext_stylesheets = [
        {"href": "https://fonts.gstatic.com", "rel": "preconnect"},
        {"href": "https://fonts.googleapis.com/css2?family=Roboto+Condensed:"
                 "wght@300;400;700&family=Roboto:wght@300;400;700&display=swap",
         "rel": "stylesheet"}
]

app = dash.Dash(name=__name__,
                title=bd["title"],
                update_title="Caricamento...",
                meta_tags=[
                        # A description for search engines
                        {
                                "name": "description",
                                "content": bd["meta_description"]
                        },
                        # For IE, use the latest renderer available (e.g. Edge)
                        {
                                "http-equiv": "X-UA-Compatible",
                                "content": "IE=edge"
                        },
                        # A tag necessary for "true" mobile support.
                        {
                                "name": "viewport",
                                "content": "width=device-width, initial-scale=1.0"
                        }
                ],
                external_stylesheets=ext_stylesheets,
                external_scripts=ext_scripts
                )

# Grafici
fig_vi = make_graph(df_vi, "Comuni in provincia di Vicenza")
fig_100k = make_graph(df_100k, "Comuni italiani con più di 100000 abitanti")
fig_reg = make_graph(df_reg, "Capoluoghi regionali")

# App content
app.layout = html.Div(className="container", children=[
        html.H1([html.I(className=fa_icon), " ", bd['title']]),
        dcc.Markdown(bando),
        dcc.Markdown(children="![Logos di creatori](assets/logos.png)",
                     className="img-logo"),
        dcc.Markdown(">A cura del [Digital Innovation Hub Vicenza](https://digitalinnovationhubvicenza.it/)"),
        html.Hr(),
        dcc.Markdown(
            children="![Light pollution](assets/light-pollution.jpg)",
            className="img-right"),
        dcc.Markdown(bd["intro1"]),
        dcc.Markdown(children="![NASA - Immagine notturna dell'Italia](assets/italy-night-200px.jpg)",
                     className="img-left"),
        dcc.Markdown(bd["intro2"]),
        html.Hr(className="clear-float"),
        dcc.Markdown("## Come intrerpretare i grafici?"),
        dcc.Markdown(bd["interp"]),
        dcc.Graph(figure=fig_vi),
        dcc.Graph(figure=fig_100k),
        dcc.Graph(figure=fig_reg),
        dcc.Markdown("## Descrizione della metodica"),
        dcc.Markdown(bd["workflow"]),
        dcc.Markdown("## Riferimenti"),
        dcc.Markdown(bd["refs"]),
        dcc.Markdown("## Credits"),
        dcc.Markdown(bd["credits"])
])

if __name__ == '__main__':
    app.run_server(debug=True)
