from pathlib import Path

import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import pandas as pd
import plotly.express as px

from content import body
from functions import pop_size, text_label

####################
# PARAMETRI INIZIALI
####################

colors = dict(primary="#303f9f", accent="#ffc107",
              primary_t="#212121", secondary_t="#757575")
app_list = ["pvout", "viirs", "ghm"]
app_name = app_list[1]

list_5com = [
        24036,  # Creazzo
        24103,  # Sovizzo
        24004,  # Altavilla Vicentina
        24108,  # Torri di Quartesolo
        24116,  # Vicenza
]

list_regcom = [
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
]

tooltip_col = ["den_com", "sigla", "pop", "median", "std"]

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
df_vi = df.loc[(df["cod_prov"] == 24)].copy()
df_vi["is_labeled"] = np.where(df_vi["cod_com"].isin(list_5com), True, False)

# Comuni italiani > 100k abitanti
df_100k = df.loc[(df["pop"] >= 100000)].copy()
df_100k["is_labeled"] = np.where(df_100k["cod_com"] == 24116, True, False)

# Capoluoghi regionali
df_reg = df.loc[(df["cod_com"].isin(list_regcom))].copy()
df_reg["is_labeled"] = np.where(df_reg["cod_com"] == 27042, True, False)

#########
# WEB APP
#########

# Google Fonts
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
                external_stylesheets=ext_stylesheets
                )

# Grafico per i comuni in provincia di Vicenza
fig_vi = px.scatter(
        df_vi, title="Comuni in provincia di Vicenza",
        x="median", y="std",
        size=pop_size(df_vi), color=df_vi["is_labeled"],
        color_discrete_sequence=[colors["primary"], colors["accent"]],
        text=text_label(df_vi),
        custom_data=tooltip_col)

# Grafico per i comuni con più di 100000 abitanti
fig_100k = px.scatter(
        df_100k, title="Comuni italiani con più di 100000 abitanti",
        x="median", y="std",
        size=df_100k["m_size"], color=df_100k["is_labeled"],
        color_discrete_sequence=[colors["primary"], colors["accent"]],
        text=text_label(df_100k),
        custom_data=tooltip_col)

# Grafico per i capoluoghi regionali
fig_reg = px.scatter(
        df_reg, title="Capoluoghi regionali",
        x="median", y="std",
        size=df_reg["m_size"], color=df_reg["is_labeled"],
        color_discrete_sequence=[colors["primary"], colors["accent"]],
        text=text_label(df_reg),
        custom_data=tooltip_col)

# Aggiornare lo stile di grafici
for f in [fig_vi, fig_100k, fig_reg]:
    f.update_layout(
            title_x=0.5,
            font_family='"Roboto Condensed", sans-serif',
            font_color=colors["primary_t"],
            title_font_family='"Roboto Medium", sans-serif',
            title_font_color=colors["primary"],
            showlegend=False,
            legend_title_font_color=colors["secondary_t"],
            autosize=True,
            dragmode=False,
            separators=",",
            hoverlabel=dict(bgcolor="white",
                            namelength=0)
    )
    f.update_xaxes(title_font_family='"Roboto", sans-serif',
                   title_text="Valore mediano",
                   )
    f.update_yaxes(title_font_family='"Roboto", sans-serif',
                   title_text="Scarto quadratico medio")
    f.update_traces(
            hovertemplate="<br>".join([
                    "<b>%{customdata[0]} (%{customdata[1]})</b>",
                    "Popolazione: %{customdata[2]}",
                    "Brillanza (nW/cm²×sr):",
                    "  mediana %{customdata[3]:.1f}",
                    "  std %{customdata[4]:.1f}"
            ]),
            textposition="top center",
            hoverlabel=dict(font_family="Roboto Condensed Light",
                            namelength=0)
    )

# App content
app.layout = html.Div(className="container", children=[
        html.H1(bd["title"]),
        dcc.Markdown(bd["bando"]),
        dcc.Markdown("![Logos di creatori](assets/logos.png)"),
        dcc.Markdown(bd["intro"]),
        dcc.Graph(figure=fig_vi),
        dcc.Markdown(bd["filler"]),
        dcc.Graph(figure=fig_100k),
        dcc.Markdown(bd["filler"]),
        dcc.Graph(figure=fig_reg),
        dcc.Markdown(bd["filler"]),
        dcc.Markdown("## Descrizione della metodica"),
        dcc.Markdown(bd["filler"]),
        dcc.Markdown(bd["icons"])
])

if __name__ == '__main__':
    app.run_server(debug=True)
