import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3.00656806014, 3))
ax = plt.axes(projection=ccrs.LambertAzimuthalEqualArea())
ax.coastlines(resolution='110m')
ax.gridlines()