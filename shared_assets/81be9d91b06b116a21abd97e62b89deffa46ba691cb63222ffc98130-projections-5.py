import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(4.2897, 3))
ax = plt.axes(projection=ccrs.LambertConformal())
ax.coastlines(resolution='110m')
ax.gridlines()