import matplotlib.pyplot as plt
from scipy.io import netcdf

from cartopy import config
import cartopy.crs as ccrs


# get the path of the file. It can be found in the repo data directory.
fname = config["repo_data_dir"] / 'netcdf' / 'HadISST1_SST_update.nc'

dataset = netcdf.netcdf_file(fname, maskandscale=True, mmap=False)
sst = dataset.variables['sst'][0, :, :]
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]

ax = plt.axes(projection=ccrs.PlateCarree())

plt.contourf(lons, lats, sst, 60,
             transform=ccrs.PlateCarree())

ax.coastlines()

plt.show()