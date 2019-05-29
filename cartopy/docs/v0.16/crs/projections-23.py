import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3.0066, 3))
ax = plt.axes(projection=ccrs.LambertAzimuthalEqualArea())
ax.coastlines(resolution='110m')
ax.gridlines()