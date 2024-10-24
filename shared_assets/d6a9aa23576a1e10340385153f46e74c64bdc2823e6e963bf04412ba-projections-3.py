import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3.0101, 3))
ax = plt.axes(projection=ccrs.AzimuthalEquidistant(
                        central_latitude=90))
ax.coastlines(resolution='110m')
ax.gridlines()