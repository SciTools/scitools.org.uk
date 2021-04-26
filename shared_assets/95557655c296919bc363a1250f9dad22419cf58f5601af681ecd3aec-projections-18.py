import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(1.6154, 3))
ax = plt.axes(projection=ccrs.OSGB(
                        approx=False))
ax.coastlines(resolution='50m')
ax.gridlines()