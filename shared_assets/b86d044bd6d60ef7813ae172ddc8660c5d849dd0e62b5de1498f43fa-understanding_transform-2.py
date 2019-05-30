import cartopy.crs as ccrs
import matplotlib.pyplot as plt


# The projection keyword determines how the plot will look
plt.figure(figsize=(6, 3))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()
ax.coastlines()

ax.contourf(lon, lat, data)  # didn't use transform, but looks ok...
plt.show()