import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(4.9603, 3))
ax = plt.axes(projection=ccrs.EquidistantConic())
ax.coastlines(resolution='110m')
ax.gridlines()