from pathlib import Path

import numpy as np
import geopandas as gpd
import pandas as pd
import rasterio

from main import get_zonal_stats

# confini comunali Istat
com_file = Path.cwd() / ".." / "data" / "input" / "istat_comuni2021.zip"
com = gpd.read_file(com_file)
com.columns = map(str.lower, com.columns)
com = com[["comune", "pro_com", "cod_prov", "cod_reg", "geometry"]]

# statistiche zonali per riempire la popolazione
worldpop_file = Path.cwd() / ".." / "data" / "input" / "worldpop.tif"
worldpop_ = rasterio.open(worldpop_file)
affine = worldpop_.transform
worldpop = worldpop_.read(1)

print("preparazione del dataset con i confini comunali...")

com = get_zonal_stats(com, worldpop, ["sum"], np.nan, affine)
com.rename(columns={"sum": "pop"}, inplace=True)
com["pop"] = com["pop"].fillna(0).astype(int)

# censimento della popolazione Istat
pop_file = Path.cwd() / ".." / "data" / "input" / "istat_pop2019.csv"
pop = pd.read_csv(pop_file, sep="\t")
pop.columns = map(str.lower, pop.columns)
pop = pop[["itter107", "territorio", "value"]]
pop.rename(columns={"itter107": "pro_com",
                    "territorio": "comune",
                    "value": "pop"
                    },
           inplace=True)

# dataset unito
com_pop = com.join(pop.set_index("pro_com"),
                   lsuffix="_com",
                   rsuffix="_cens",
                   on="pro_com").set_index("pro_com")
print("com:", len(pop))
print("com_pop:", len(com_pop))
com_pop["diff_cens_com"] = com_pop["pop_cens"] - com_pop["pop_com"]
com_pop["pop"] = np.where(com_pop["pop_cens"].isnull,
                          com_pop["pop_cens"],
                          com_pop["pop_com"])

# aggiungere nomi di provincie e regioni
prov_file = Path.cwd() / ".." / "data" / "input" / "istat_codici_prov.csv"
prov = pd.read_csv(prov_file, sep=";", na_filter=False)
prov.columns = map(str.lower, prov.columns)
prov = prov[["cod_reg", "den_reg", "cod_prov_storico",
             "den_uts", "sigla automobilistica"]]
prov.rename(columns={"sigla automobilistica": "sigla",
                     "cod_prov_storico": "cod_prov",
                     "den_uts": "den_prov"}, inplace=True)
reg = prov[["cod_reg", "den_reg"]].drop_duplicates().set_index("cod_reg")
prov[["cod_reg", "cod_prov"]] = prov[["cod_reg", "cod_prov"]].astype(int)
com_pop_pr = com_pop.join(prov.set_index("cod_prov"),
                          rsuffix="_",
                          on="cod_prov")
com_pop_pr["cod_com"] = com_pop_pr.index
com_pop_pr.rename(columns={"comune_com": "den_com",
                           "pro_com": "cod_com"},
                  inplace=True)
com_geog = com_pop_pr[["den_com", "sigla", "cod_prov",
                       "den_prov", "cod_reg", "den_reg", "pop", "geometry"]]
com_geog.index.names = ["cod_com"]
com_geog["pop"].fillna(-1, inplace=True)
com_geog["pop"] = com_geog["pop"].astype(int)
com_f_nogeog = com_geog.loc[:, com_geog.columns != "geometry"]

# salvare il file
com_geog_f = Path.cwd() / ".." / "data" / "output" / "istat_com_pop"
com_geog.to_file(com_geog_f, driver="ESRI Shapefile")

com_f_nogeog.to_csv(f"{com_geog_f}.csv")
