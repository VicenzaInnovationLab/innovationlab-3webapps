from datetime import datetime as dt
from pathlib import Path

import geopandas as gpd
import pandas as pd
import rasterio
from rasterstats import zonal_stats

import config as cfg

def get_zonal_stats(vector, raster, stats, nodata, affine_):
    """Esegue le statistiche zonali e salva il risultato in Geopandas DataFrame"""
    result = zonal_stats(vector, raster,
                         nodata=nodata, stats=stats,
                         affine=affine_, geojson_out=True)
    geostats = gpd.GeoDataFrame.from_features(result, crs=vector.crs)
    return geostats

now_str = dt.now().strftime("%Y%m%d-%H%M%S")  # il marcatempo

# STEP 1. LEGGERE IL VETTORE

adm_file = Path.cwd() / ".." / "data" / "input" / "istat_comuni2021.zip"
adm = gpd.read_file(adm_file)

# Mappare la funzione Lowercase per tutti i nomi delle colonne
adm.columns = map(str.lower, adm.columns)

adm = adm[["comune", "pro_com", "cod_prov", "cod_reg"]]
print(f"ci sono {len(adm)} poligoni dei comuni")
print(adm.head())
