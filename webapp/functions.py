import numpy as np
import pandas as pd
import plotly.express as px

colors = dict(primary="#303f9f", accent="#ffc107",
              primary_t="#212121", secondary_t="#757575")
tooltip_col = ["den_com", "den_prov", "pop", "median", "std"]


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


def text_label(dataframe: pd.DataFrame, col: str = "is_labeled"):
    """Estimate a size for a graph point based on city population"""
    return np.where(dataframe[col] == 1, dataframe["den_com"], "")


def make_graph(dataframe: pd.DataFrame, graph_name: str) -> px.scatter:
    """Add a scatter plot with fixed parameters"""
    f = px.scatter(
            dataframe, title=graph_name, x="median", y="std",
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
            legend_title_font_color=colors["secondary_t"],
            autosize=True,
            dragmode=False,
            separators=",",
            hoverlabel=dict(bgcolor="white",
                            namelength=0)
    )

    f.update_xaxes(title_font_family='"Roboto", sans-serif',
                   title_text="Valore mediano (nW/cm²·sr)")
    f.update_yaxes(title_font_family='"Roboto", sans-serif',
                   title_text="Deviazione standard (nW/cm²·sr)")

    f.update_traces(
            hovertemplate="<br>".join([
                    "<b>%{customdata[0]}</b>",
                    "Provincia: %{customdata[1]}",
                    "Popolazione: %{customdata[2]}",
                    "Brillanza (nW/(cm²·sr):",
                    "  mediana %{customdata[3]:.1f}",
                    "  std %{customdata[4]:.1f}"
            ]),
            textposition="top center",
            hoverlabel=dict(font_family="Roboto Condensed Light",
                            namelength=0)
    )
    return f
