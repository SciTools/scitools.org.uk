import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(2.4323374137753486, 3))
ax = plt.axes(projection=ccrs.OSNI())
ax.coastlines(resolution='10m')
ax.gridlines()