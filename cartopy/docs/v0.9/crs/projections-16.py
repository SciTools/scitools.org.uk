import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(2.99893683337, 3))
ax = plt.axes(projection=ccrs.Geostationary())
ax.coastlines(resolution='110m')
ax.gridlines()