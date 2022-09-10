import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

dy, dx = (4, 10)
rgba = np.linspace(0, 255*31, dx*dy*4, dtype=np.uint8).reshape((dy, dx, 4))
rgba[:, :, 3]  = np.linspace(0, 255, dx, dtype=np.uint8).reshape(1, dx)

fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.Orthographic(central_latitude=45))
ax.imshow(rgba, transform=ccrs.PlateCarree())

plt.show()