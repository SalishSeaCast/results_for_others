# # Boundary Pass Central Node Model Results Slab
#
# Assemble time series from a model results slab for Rich:
#
# * NEMO-3.6 nowcast-green runs
# * full water column
# * hourly average results at Boundary Pass location of ONC mooring
# * hourly average results at ONC central node
# * 13-26 Jul-2016
#

import os
import pathlib

import arrow
import cmocean
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import xarray as xr


# ONC description of central node location:
# Depth: 297 m
# Latitude: 49.040066666
# Longitude: -123.425825
central_ji = (424, 266)
# ONC description of Boundary Pass mooring location:
# Depth: 230 m
# Latitude: 48.7665
# Longitude: -123.039556
boundary_ji = (343, 289)
# ## Region of Interest
offsets = {'north': 0, 'south': 5, 'east': 25, 'west': 15}


# ## Dataset
#
# * Index ranges in the `y` and `x` directions that define the region of interest above
# * Results date range
# * Time origin for the dataset we are building
# * Results archive storage path
# * List of dataset paths to process
y_slice = slice(boundary_ji[0] - offsets['south'], central_ji[0] + offsets['north'])
x_slice = slice(central_ji[1] - offsets['west'], boundary_ji[1] + offsets['east'])

start_date = arrow.get('2016-08-09')
start_yyyymmdd = start_date.format('YYYYMMDD')
end_date = arrow.get('2016-08-22')
end_yyyymmdd = end_date.format('YYYYMMDD')
time_origin = start_date.format('YYYY-MM-DD HH:mm:ss')

results_archive = pathlib.Path('/results/SalishSea/nowcast-green/')


def build_datasets_list(grid):
    datasets = []
    for a in arrow.Arrow.range('day', start_date, end_date):
        ddmmmyy = a.format('DDMMMYY').lower()
        yyyymmdd = a.format('YYYYMMDD')
        results_dir = f'{ddmmmyy}'
        grid_T_1h = f'SalishSea_1h_{yyyymmdd}_{yyyymmdd}_grid_{grid}.nc'
        datasets.append(os.fspath(results_archive/results_dir/grid_T_1h))
    return datasets

creation_time = arrow.now().format('YYYY-MM-DD HH:mm:ss ZZ')
start_yyyymmdd = start_date.format('YYYYMMDD')
end_yyyymmdd = end_date.format('YYYYMMDD')


grid = 'T'
datasets = build_datasets_list(grid)

with xr.open_mfdataset(datasets) as results:
    slab = results.isel(y=y_slice, x=x_slice)

    ds = xr.Dataset(
        data_vars={
            'nav_lon': slab.nav_lon,
            'nav_lat': slab.nav_lat,
            'vosaline': slab.vosaline,
            'votemper': slab.votemper,
        },
        attrs={
            'name': f'SalishSea_1h_{start_yyyymmdd}_{end_yyyymmdd}_grid_{grid}',
            'title': 'SalishSeaCast Boundary Pass and ONC Central Node Temperature and Salinity Results',
            'conventions': 'CF-1.5',
            'source_code': 'https://bitbucket.org/salishsea/results/src/tip/BoundaryPassCentralNodeForRich/BoundaryPassCentralNodeResultsTimeSeries.py',
            'rendered_notebook': 'https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/results/raw/tip/BoundaryPassCentralNodeForRich/BoundaryPassCentralNodeResultsSlab.ipynb',
            'history': f'{creation_time}: Processed from results files in /results/SalishSea/nowcast-green/',
        },
    )

    ds.vosaline.attrs['standard_name'] = 'sea_water_reference_salinity'
    ds.vosaline.attrs['units'] = 'g kg-1'
    ds.time_centered.attrs['time_origin'] = f'hours since {time_origin}'
    ds.time_counter.attrs['time_origin'] = f'hours since {time_origin}'

    ds.to_netcdf(
        f'SalishSea_1h_{start_yyyymmdd}_{end_yyyymmdd}_grid_{grid}.nc',
        format='netCDF4', engine='netcdf4',
        encoding={
            'time_counter': {'units': f'hours since {time_origin}'},
            'time_centered': {'units': f'hours since {time_origin}'},
        },
        unlimited_dims='time_counter',
    )


grid = 'U'
datasets = build_datasets_list(grid)

with xr.open_mfdataset(datasets) as results:
    slab = results.isel(y=y_slice, x=x_slice)

    ds = xr.Dataset(
        data_vars={
            'nav_lon': slab.nav_lon,
            'nav_lat': slab.nav_lat,
            'vozocrtx': slab.vozocrtx,
        },
        attrs={
            'name': f'SalishSea_1h_{start_yyyymmdd}_{end_yyyymmdd}_grid_{grid}',
            'title': 'SalishSeaCast Boundary Pass and ONC Central Node u Velocity Component Results',
            'conventions': 'CF-1.5',
            'source_code': 'https://bitbucket.org/salishsea/results/src/tip/BoundaryPassCentralNodeForRich/BoundaryPassCentralNodeResultsTimeSeries.py',
            'rendered_notebook': 'https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/results/raw/tip/BoundaryPassCentralNodeForRich/BoundaryPassCentralNodeResultsSlab.ipynb',
            'history': f'{creation_time}: Processed from results files in /results/SalishSea/nowcast-green/',
        },
    )

    ds.time_centered.attrs['time_origin'] = f'hours since {time_origin}'
    ds.time_counter.attrs['time_origin'] = f'hours since {time_origin}'

    ds.to_netcdf(
        f'SalishSea_1h_{start_yyyymmdd}_{end_yyyymmdd}_grid_{grid}.nc',
        format='netCDF4', engine='netcdf4',
        encoding={
            'time_counter': {'units': f'hours since {time_origin}'},
            'time_centered': {'units': f'hours since {time_origin}'},
        },
        unlimited_dims='time_counter',
    )

grid = 'V'
datasets = build_datasets_list(grid)

with xr.open_mfdataset(datasets) as results:
    slab = results.isel(y=y_slice, x=x_slice)

    ds = xr.Dataset(
        data_vars={
            'nav_lon': slab.nav_lon,
            'nav_lat': slab.nav_lat,
            'vomecrty': slab.vomecrty,
        },
        attrs={
            'name': f'SalishSea_1h_{start_yyyymmdd}_{end_yyyymmdd}_grid_{grid}',
            'title': f'SalishSeaCast Boundary Pass and ONC Central Node {grid.lower()} Velocity Component Results',
            'conventions': 'CF-1.5',
            'source_code': 'https://bitbucket.org/salishsea/results/src/tip/BoundaryPassCentralNodeForRich/BoundaryPassCentralNodeResultsTimeSeries.py',
            'rendered_notebook': 'https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/results/raw/tip/BoundaryPassCentralNodeForRich/BoundaryPassCentralNodeResultsSlab.ipynb',
            'history': f'{creation_time}: Processed from results files in /results/SalishSea/nowcast-green/',
        },
    )

    ds.time_centered.attrs['time_origin'] = f'hours since {time_origin}'
    ds.time_counter.attrs['time_origin'] = f'hours since {time_origin}'

    ds.to_netcdf(
        f'SalishSea_1h_{start_yyyymmdd}_{end_yyyymmdd}_grid_{grid}.nc',
        format='netCDF4', engine='netcdf4',
        encoding={
            'time_counter': {'units': f'hours since {time_origin}'},
            'time_centered': {'units': f'hours since {time_origin}'},
        },
        unlimited_dims='time_counter',
    )

grid = 'W'
datasets = build_datasets_list(grid)

with xr.open_mfdataset(datasets) as results:
    slab = results.isel(y=y_slice, x=x_slice)

    ds = xr.Dataset(
        data_vars={
            'nav_lon': slab.nav_lon,
            'nav_lat': slab.nav_lat,
            'vovecrtz': slab.vovecrtz,
        },
        attrs={
            'name': f'SalishSea_1h_{start_yyyymmdd}_{end_yyyymmdd}_grid_{grid}',
            'title': f'SalishSeaCast Boundary Pass and ONC Central Node {grid.lower()} Velocity Component Results',
            'conventions': 'CF-1.5',
            'source_code': 'https://bitbucket.org/salishsea/results/src/tip/BoundaryPassCentralNodeForRich/BoundaryPassCentralNodeResultsTimeSeries.py',
            'rendered_notebook': 'https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/results/raw/tip/BoundaryPassCentralNodeForRich/BoundaryPassCentralNodeResultsSlab.ipynb',
            'history': f'{creation_time}: Processed from results files in /results/SalishSea/nowcast-green/',
        },
    )

    ds.time_centered.attrs['time_origin'] = f'hours since {time_origin}'
    ds.time_counter.attrs['time_origin'] = f'hours since {time_origin}'

    ds.to_netcdf(
        f'SalishSea_1h_{start_yyyymmdd}_{end_yyyymmdd}_grid_{grid}.nc',
        format='netCDF4', engine='netcdf4',
        encoding={
            'time_counter': {'units': f'hours since {time_origin}'},
            'time_centered': {'units': f'hours since {time_origin}'},
        },
        unlimited_dims='time_counter',
    )
