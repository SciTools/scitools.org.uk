import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(5.91496607667, 3))
ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines(resolution='110m')
ax.gridlines()