import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(2.43233741378, 3))
ax = plt.axes(projection=ccrs.OSNI())
ax.coastlines(resolution='10m')
ax.gridlines()