import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3.5091, 3))
ax = plt.axes(projection=ccrs.Mercator())
ax.coastlines(resolution='110m')
ax.gridlines()