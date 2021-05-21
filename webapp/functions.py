import numpy as np
import pandas as pd


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
