import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(100)

x = np.arange(10, 20)
y = np.arange(0, 10)
x, y = np.meshgrid(x, y)

img = np.random.randint(low=0, high=255, size=(10, 10, 4)) / 255

projection = ccrs.Mollweide()
transform = ccrs.PlateCarree()
ax = plt.axes(projection=projection)
ax.set_global()
ax.coastlines()

ax.pcolormesh(np.linspace(0, 120, 11), np.linspace(0, 80, 11), img, transform=transform)

plt.show()