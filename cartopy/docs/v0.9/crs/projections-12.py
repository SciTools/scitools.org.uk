import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(6.92280629527, 3))
ax = plt.axes(projection=ccrs.InterruptedGoodeHomolosine())
ax.coastlines(resolution='110m')
ax.gridlines()