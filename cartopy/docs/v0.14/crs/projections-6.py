import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(9.42477796076938, 3))
ax = plt.axes(projection=ccrs.LambertCylindrical())
ax.coastlines(resolution='110m')
ax.gridlines()