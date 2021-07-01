import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd

from source.istat_codes import *
from source.content import *


colors = dict(primary="#303f9f", accent="#ffc107",
              primary_t="#212121", secondary_t="#757575")
tooltip_col = ["den_com", "den_prov", "pop", "mean", "std"]


def pop_size(dataframe: pd.DataFrame) -> np.ndarray:
    """Estimate a size for a graph point based on city population"""
    pop_st = dataframe["pop"].describe()  # statistiche per marker size
    output = np.where(
            dataframe["pop"].isna(),
            1,
            dataframe["pop"].apply(
                    lambda x: (x - pop_st["mean"]) / pop_st["std"])
    )
    return 2 + output


def prepare_data(csv_path) -> dict:
    df = pd.read_csv(csv_path, sep=",", na_filter=False, index_col=0)
    df["mean"] = df["mean"].apply(pd.to_numeric)
    df["std"] = df["std"].apply(pd.to_numeric)
    df["pop"].replace(-1, np.NaN, inplace=True)
    df["m_size"] = pop_size(df)  # marker size for visualization

    # Separare il dataset in livello provinciale, regionale, ecc.

    # Provincia VI
    df_vi = df.loc[(df["cod_prov"] == istat_prov_vi)].copy()
    df_vi["is_labeled"] = np.where(df_vi["cod_com"].isin(istat_5com), True,
                                   False)

    # Comuni italiani > 100k abitanti
    df_100k = df.loc[(df["pop"] >= 100000)].copy()
    df_100k["is_labeled"] = np.where(df_100k["cod_reg"] == istat_reg_ven, True,
                                     False)

    # Capoluoghi regionali
    df_reg = df.loc[(df["cod_com"].isin(istat_capoluoghi))].copy()
    df_reg["is_labeled"] = np.where(df_reg["cod_com"] == istat_venezia, True,
                                    False)
    result = dict(df_vi=df_vi, df_100k=df_100k, df_reg=df_reg)
    return result


def text_label(dataframe: pd.DataFrame, col: str = "is_labeled"):
    """Estimate a size for a graph point based on city population"""
    return np.where(dataframe[col] == 1, dataframe["den_com"], "")


def make_graph(dataframe: pd.DataFrame,
               graph_name: str,
               unit_name: str,
               unit: str) -> px.scatter:
    """Add a scatter plot with fixed parameters"""
    f = px.scatter(
            dataframe, title="", x="mean", y="std",
            size=pop_size(dataframe), color=dataframe["is_labeled"],
            color_discrete_sequence=[colors["primary"], colors["accent"]],
            text=text_label(dataframe),
            custom_data=tooltip_col)

    f.update_layout(
            title_x=0.5,
            font_family='"Roboto Condensed", sans-serif',
            font_color=colors["primary_t"],
            title_font_family='"Roboto Medium", sans-serif',
            title_font_color=colors["primary"],
            showlegend=False,
            # legend_y=-0.3,
            # legend_x=0.4,
            legend_title="Colori",
            legend_title_font_color=colors["secondary_t"],
            legend_orientation="h",
            # autosize=True,
            # dragmode="zoom",
            separators=",",
            hoverlabel=dict(bgcolor="white",
                            namelength=0)
    )

    f.update_xaxes(title_font_family='"Roboto", sans-serif',
                   title_text=f"Valore medio {unit}")
    f.update_yaxes(title_font_family='"Roboto", sans-serif',
                   title_text=f"Deviazione standard {unit}")

    f.update_traces(
            hovertemplate="<br>".join([
                    "<b>%{customdata[0]}</b>",
                    "Provincia: %{customdata[1]}",
                    "Popolazione: %{customdata[2]}",
                    f"{unit_name} {unit}:",
                    "  media %{customdata[3]:.1f}",
                    "  std %{customdata[4]:.1f}"]),
            textposition="top center",
            hoverlabel=dict(font_family="Roboto Condensed Light",
                            namelength=0)
    )
    return f


def app_content(app, fig_vi, fig_100k, fig_reg):
    page = html.Div(className="container", children=[
            html.Div(className="central-align", children=[
                    dcc.Link("ritorna alla Homepage", href="/", )
            ]),
            html.H1([html.I(className=app["fa_icon"]), " ", app["title"]]),
            dcc.Markdown(bando),
            dcc.Markdown(children="![Logos di creatori](static/img/logos.png)",
                         className="img-logo"),
            dcc.Markdown(className="right-align",
                         children=">A cura del [Digital Innovation Hub Vicenza](https://digitalinnovationhubvicenza.it/)"),
            html.Hr(),
            dcc.Markdown(
                    children=app["first_img"],
                    className="img-right"),
            dcc.Markdown(app["intro1"]),
            dcc.Markdown(
                children=app["second_img"],
                className="img-left"),
            dcc.Markdown(app["intro2"]),
            html.Hr(className="clear-float"),
            dcc.Markdown("## Come intrerpretare i grafici?"),
            dcc.Markdown(app["interp"]),
            html.Div(className="pagebreak"),
            dcc.Tabs([
                    dcc.Tab(className="custom-tab",
                            selected_className="custom-tab--selected",
                            label=("Comuni in provincia di Vicenza"),
                            children=[
                                    dcc.Graph(figure=fig_vi),
                                    dcc.Markdown(app["comment1"])
                            ]
                    ),
                    dcc.Tab(className="custom-tab",
                            selected_className="custom-tab--selected",
                            label="Comuni italiani con più di 100.000 abitanti",
                            children=[
                                    dcc.Graph(figure=fig_100k),
                                    dcc.Markdown(app["comment2"])
                            ]
                    ),
                    dcc.Tab(className="custom-tab",
                            selected_className="custom-tab--selected",
                            label="Capoluoghi regionali",
                            children=[
                                    dcc.Graph(figure=fig_reg),
                                    dcc.Markdown(app["comment3"])
                            ]
                    )
            ]),
            html.Div(className="pagebreak"),
            dcc.Markdown("## Metodologia"),
            dcc.Markdown(app["workflow"]),
            dcc.Markdown("## Riferimenti"),
            dcc.Markdown(app["refs"]),
            dcc.Markdown("## Crediti"),
            dcc.Markdown(app["credits"])
    ])
    return page
