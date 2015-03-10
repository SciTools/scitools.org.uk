import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(2.61538461538, 3))
ax = plt.axes(projection=ccrs.EuroPP())
ax.coastlines(resolution='50m')
ax.gridlines()