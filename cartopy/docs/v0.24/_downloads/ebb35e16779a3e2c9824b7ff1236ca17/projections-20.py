import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3.2687, 3))
ax = plt.axes(projection=ccrs.LambertZoneII())
ax.coastlines(resolution='10m')
ax.gridlines()