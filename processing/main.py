from rasterstats import zonal_stats
import geopandas as gpd


def get_zonal_stats(vector, raster, stats, nodata, affine_):
    """Esegue le statistiche zonali
    e salva il risultato in Geopandas DataFrame
    stats_list = ['min', 'max', 'mean', 'count',
                  'sum', 'std', 'median', 'majority',
                  'minority', 'unique', 'range']"""
    result = zonal_stats(vector, raster,
                         nodata=nodata, stats=stats,
                         affine=affine_, geojson_out=True)
    geostats = gpd.GeoDataFrame.from_features(result, crs=vector.crs)
    return geostats


RASTERS = ["pvout", "viirs", "ghm"]
