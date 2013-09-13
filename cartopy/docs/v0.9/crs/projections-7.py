import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(6.0, 3))
ax = plt.axes(projection=ccrs.Mollweide())
ax.coastlines(resolution='110m')
ax.gridlines()