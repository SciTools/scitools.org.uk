import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()

x, y = np.meshgrid(np.arange(-179, 181), np.arange(-90, 91))
data = np.sqrt(x**2 + y**2)
ax.hexbin(x.flatten(), y.flatten(), C=data.flatten(),
          gridsize=20, transform=ccrs.PlateCarree())
plt.show()