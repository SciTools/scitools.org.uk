import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(4.0915, 3))
ax = plt.axes(projection=ccrs.Miller())
ax.coastlines(resolution='110m')
ax.gridlines()