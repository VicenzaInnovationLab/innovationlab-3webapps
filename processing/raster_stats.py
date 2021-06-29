from pathlib import Path

import numpy as np
import geopandas as gpd
import rasterio

from main import get_zonal_stats, RASTERS

print("apro i confini comunali")
com_file = Path.cwd() / ".." / "data" / "istat_com_pop" / "istat_com_pop.shp"
com = gpd.read_file(com_file)

print("apro i raster tematici")
rast = list()
for r in RASTERS:
    rpath = Path.cwd() / ".." / "data" / f"{r}.tif"
    robj = rasterio.open(rpath)
    raff = robj.transform
    rdic = dict(name=r, path=rpath, obj=robj.read(1), affine=raff)
    rast.append(rdic)

print("calcolo delle statistiche zonali")
for r in rast:
    print(f"raster {r['name']}")
    vect_ = get_zonal_stats(com,
                            r["obj"],
                            ["std", "mean", "median"],
                            np.nan,
                            r["affine"])
    vect = vect_.loc[:, vect_.columns != "geometry"]
    save_path = Path.cwd() / ".." / "webapp" / "data" / f"stats_{r['name']}.csv"
    vect.to_csv(save_path)

print("finito")
